CREATE TABLE cuentasTw (
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
	es_candado BOOL
);

CREATE TABLE notas (
	nickCuenta TEXT,
	botometerNotaBotMediaTotal FLOAT,
	botometerNotaBotPolitico FLOAT,
	botometerNotaBotSeguidor FLOAT,
	botometerNotaBotFinanzas FLOAT,
	botometerNotaBotOtros FLOAT,
	botometerNotaBotAutoProclamado FLOAT,
	botometerNotaBotSpam FLOAT,
	miNotaPersonalBot FLOAT,
	mediaNotaBot FLOAT
);

INSERT INTO cuentasTw (nickCuenta) VALUES ('RockstarGames');
INSERT INTO cuentasTw (nickCuenta) VALUES ('valvesoftware');
INSERT INTO cuentasTw (nickCuenta) VALUES ('CooLifeGame');
INSERT INTO cuentasTw (nickCuenta) VALUES ('arthurmorganbot');
INSERT INTO cuentasTw (nickCuenta) VALUES ('IbaiLlanos');
INSERT INTO cuentasTw (nickCuenta) VALUES ('Muzska89');
INSERT INTO cuentasTw (nickCuenta) VALUES ('CursedSetups');

INSERT INTO notas (nickCuenta) VALUES ('RockstarGames');
INSERT INTO notas (nickCuenta) VALUES ('valvesoftware');
INSERT INTO notas (nickCuenta) VALUES ('CooLifeGame');
INSERT INTO notas (nickCuenta) VALUES ('arthurmorganbot');
INSERT INTO notas (nickCuenta) VALUES ('IbaiLlanos');
INSERT INTO notas (nickCuenta) VALUES ('Muzska89');
INSERT INTO notas (nickCuenta) VALUES ('CursedSetups');