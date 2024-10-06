import sqlite3
import datetime
import pandas as pd

db = sqlite3.connect("Databases/twitter.db")

cur = db.cursor()
cur.execute("SELECT * FROM cuentasTw")
cuentasTw = cur.fetchall()

cur.execute("SELECT * FROM notas")
botometerNotasBotMediaTotal = cur.fetchall()

notaSeguidores = 0
notaSeguidos = 0
notaRatioSeguidoresSeguidos = 0
notaAntiguedad = 0
notaDescripcionPerfil = 0
notaUbicacion = 0
notaLikes = 0
notaTweets = 0
notaBannerPred = 0
notaFotoPred = 0
notaVerificado = 0

for cuentaTw, botometerNotaBotMediaTotal in zip(cuentasTw, botometerNotasBotMediaTotal): #para poder iterar dos conjuntos de datos de forma simultanea se emplea la función zip
    #Nota seguidores
    if cuentaTw[3] > 500:
        notaSeguidores = 0
    elif 100 <= cuentaTw[3] <= 500:
        notaSeguidores = 0.5
    elif cuentaTw[3] < 100:
        notaSeguidores = 1

    #Nota seguidos
    if cuentaTw[4] > 500:
        notaSeguidos = 0
    elif 100 <= cuentaTw[4] <= 500:
        notaSeguidos = 0.5
    elif cuentaTw[4] < 100:
        notaSeguidos = 1

    #Nota ratio seguidores - seguidos
    if cuentaTw[4] == 0:
        ratioSeguidoresSeguidos = 2
    else:
        ratioSeguidoresSeguidos = round((cuentaTw[3] / cuentaTw[4]), 2)
        
    if ratioSeguidoresSeguidos > 1.75:
        notaRatioSeguidoresSeguidos = 0.5
    elif 0.75 <= ratioSeguidoresSeguidos <= 1.75:
        notaRatioSeguidoresSeguidos = 0
    elif ratioSeguidoresSeguidos < 0.75:
        notaRatioSeguidoresSeguidos = 1

    #Nota antiguedad
    conversionTextoAFecha = datetime.datetime.strptime(cuentaTw[5], '%Y-%m-%d %H:%M:%S')
    fechaCreacion = conversionTextoAFecha.date()
    fechaActual = datetime.datetime.now().date()

    diasPasados = fechaActual - fechaCreacion
    
    if diasPasados.days >= 365:
        notaAntiguedad = 0
    elif 182 < diasPasados.days < 365:
        notaAntiguedad = 0.5
    elif diasPasados.days <= 182:
        notaAntiguedad = 1
    
    #Nota descripcion perfil
    if len(cuentaTw[6]) > 0:
        notaDescripcionPerfil = 0
    elif len(cuentaTw[6]) == 0:
        notaDescripcionPerfil = 1
    
    #Nota ubicacion
    if len(cuentaTw[7]) > 0:
        notaUbicacion = 0
    elif len(cuentaTw[7]) == 0:
        notaUbicacion = 1
    
    #Nota likes dados
    if cuentaTw[8] >= 1000:
        notaLikes = 0
    elif 0 < cuentaTw[8] < 1000:
        notaLikes = 0.5
    elif cuentaTw[8] == 0:
        notaLikes = 1
    
    #Nota tweets publicados
    if cuentaTw[9] >= 100:
        notaTweets = 0
    elif 0 < cuentaTw[9] < 100:
        notaTweets = 0.5
    elif cuentaTw[9] == 0:
        notaTweets = 1
    
    #Nota banner perfil predeterminado
    if cuentaTw[10] == 0:
        notaBannerPred = 0
    elif cuentaTw[10] == 1:
        notaBannerPred = 1
    
    #Nota foto perfil predeterminada
    if cuentaTw[11] == 0:
        notaFotoPred = 0
    elif cuentaTw[11] == 1:
        notaFotoPred = 1
    
    #Nota usuario verificado
    if cuentaTw[12] == 1:
        notaVerificado = 0
    elif cuentaTw[12] == 0:
        notaVerificado = 1
    
    miNotaPersonalBot = (notaSeguidores + notaSeguidos + notaRatioSeguidoresSeguidos + notaAntiguedad + notaDescripcionPerfil + notaUbicacion + notaLikes + notaTweets + notaBannerPred + notaFotoPred + notaVerificado) / 11

    mediaNotaBot = (miNotaPersonalBot + botometerNotaBotMediaTotal[1]) / 2

    cur.execute("""UPDATE notas SET miNotaPersonalBot = ?, mediaNotaBot = ? where nickCuenta = ?""", (miNotaPersonalBot, mediaNotaBot, cuentaTw[0]))

    db.commit()