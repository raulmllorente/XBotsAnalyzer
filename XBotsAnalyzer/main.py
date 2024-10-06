import tweepy
import botometer
import sqlite3
import pandas as pd
import os
import config

db = sqlite3.connect("Databases/twitter.db")

authTweepy = tweepy.OAuthHandler(config.twitter_app_auth['consumer_key'], config.twitter_app_auth['consumer_secret'])
authTweepy.set_access_token(config.twitter_app_auth['access_token'], config.twitter_app_auth['access_token_secret'])
api = tweepy.API(authTweepy)

botom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=config.rapidapi_key, **config.twitter_app_auth)

os.system('python createDB.py')
os.system('python getCuentas.py')

cur = db.cursor()
cur.execute("SELECT nickCuenta FROM cuentasTw")
cuentasTw = cur.fetchall()

for cuentaTw in cuentasTw:
    try:
        usuarioTw = api.get_user(cuentaTw[0])

        id = usuarioTw.id_str
        nombre = usuarioTw.name
        seguidores = usuarioTw.followers_count
        siguiendo_a = usuarioTw.friends_count
        miembro_desde = usuarioTw.created_at
        descripcion_perfil = usuarioTw.description
        ubicacion_perfil = usuarioTw.location
        likes_dados = usuarioTw.favourites_count
        tweets_publicados = usuarioTw.statuses_count
        tiene_banner_predeterminado = usuarioTw.default_profile
        tiene_imagen_predeterminada = usuarioTw.default_profile_image
        es_verificada = usuarioTw.verified
        es_candado = usuarioTw.protected


        def comprobarCuentasBotometer():
            try:
                comprobarCuentaBotometer = botom.check_account('@' + cuentaTw[0])
                botometerNotas = comprobarCuentaBotometer["raw_scores"]["universal"]
            except botometer.NoTimelineError:
                print ("Cuenta sin timeline")
                botometerNotas = {"astroturf": 0, "fake_follower": 1, "financial": 0, "other": 0, "overall": 1, "self_declared": 0, "spammer": 0}

            except botometer.TweepError:
                print ("Cuenta protegida")
                botometerNotas = {"astroturf": 0, "fake_follower": 0, "financial": 0, "other": 0, "overall": 0, "self_declared": 0, "spammer": 0}
                
            return botometerNotas

        botometerNotas = comprobarCuentasBotometer()

        cur.execute("""UPDATE cuentasTw SET id = ?, nombre = ?, seguidores = ?, siguiendo_a = ?, miembro_desde = ?,
        descripcion_perfil = ?, ubicacion_perfil = ?, likes_dados = ?, tweets_publicados = ?, tiene_banner_predeterminado = ?,
        tiene_imagen_predeterminada = ?, es_verificada = ?, es_candado = ? where nickCuenta = ?""", (id, nombre, seguidores, siguiendo_a, miembro_desde, descripcion_perfil,
        ubicacion_perfil, likes_dados, tweets_publicados, tiene_banner_predeterminado, tiene_imagen_predeterminada, es_verificada,
        es_candado, cuentaTw[0]))

        cur.execute("""UPDATE notas SET botometerNotaBotMediaTotal = ?, botometerNotaBotPolitico = ?,
        botometerNotaBotSeguidor = ?, botometerNotaBotFinanzas = ?, botometerNotaBotOtros = ?, botometerNotaBotAutoProclamado = ?,
        botometerNotaBotSpam = ? where nickCuenta = ?""", (botometerNotas["overall"], botometerNotas["astroturf"], botometerNotas["fake_follower"], botometerNotas["financial"],
        botometerNotas["other"], botometerNotas["self_declared"], botometerNotas["spammer"], cuentaTw[0]))

        db.commit()
        
    except Exception as e:
        raise tweepy.TweepError(e)

os.system('python ratios.py')

print(pd.read_sql_query("select * from cuentasTw", db))
print(pd.read_sql_query("select * from notas", db))

os.system('python generateExcel.py')