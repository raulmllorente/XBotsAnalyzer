import sqlite3

db = sqlite3.connect("Databases/twitter.db")

cur = db.cursor()

cur.execute("""DROP TABLE IF EXISTS cuentasTw""")
cur.execute("""DROP TABLE IF EXISTS notas""")

cur.execute("""CREATE TABLE cuentasTw (
	nickCuenta TEXT,
	id TEXT,
	nombre TEXT,
	seguidores INT,
	siguiendo_a INT,
  	miembro_desde TEXT,
	descripcion_perfil TEXT,
	ubicacion_perfil TEXT,
	likes_dados INT,
	tweets_publicados INT,
  	tiene_banner_predeterminado BOOL,
	tiene_imagen_predeterminada BOOL,
	es_verificada BOOL,
	es_candado BOOL,
	cuentaMuestraQueSigue TEXT
)""")

cur.execute("""CREATE TABLE notas (
	nickCuenta TEXT,
	botometerNotaBotMediaTotal FLOAT,
	botometerNotaBotPolitico FLOAT,
	botometerNotaBotSeguidor FLOAT,
	botometerNotaBotFinanzas FLOAT,
	botometerNotaBotOtros FLOAT,
	botometerNotaBotAutoProclamado FLOAT,
	botometerNotaBotSpam FLOAT,
	miNotaPersonalBot FLOAT,
	mediaNotaBot FLOAT,
	cuentaMuestraQueSigue TEXT
)""")

db.commit()