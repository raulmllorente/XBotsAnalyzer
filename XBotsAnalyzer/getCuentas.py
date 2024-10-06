import sqlite3
import tweepy
import config

db = sqlite3.connect("Databases/twitter.db")

authTweepy = tweepy.OAuthHandler(config.twitter_app_auth['consumer_key'], config.twitter_app_auth['consumer_secret'])
authTweepy.set_access_token(config.twitter_app_auth['access_token'], config.twitter_app_auth['access_token_secret'])
api = tweepy.API(authTweepy)

cur = db.cursor()

screen_name = "Xbox"

for follower in tweepy.Cursor(api.followers, screen_name).items(100):
    cur.execute("""INSERT INTO cuentasTw (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "Xbox"))
    cur.execute("""INSERT INTO notas (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "Xbox"))
    db.commit()

screen_name = "PlayStation"

for follower in tweepy.Cursor(api.followers, screen_name).items(100):
    cur.execute("""INSERT INTO cuentasTw (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "PlayStation"))
    cur.execute("""INSERT INTO notas (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "PlayStation"))
    db.commit()

screen_name = "NintendoAmerica"

for follower in tweepy.Cursor(api.followers, screen_name).items(100):
    cur.execute("""INSERT INTO cuentasTw (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "NintendoAmerica"))
    cur.execute("""INSERT INTO notas (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "NintendoAmerica"))
    db.commit()

screen_name = "Steam"

for follower in tweepy.Cursor(api.followers, screen_name).items(100):
    cur.execute("""INSERT INTO cuentasTw (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "Steam"))
    cur.execute("""INSERT INTO notas (nickCuenta, cuentaMuestraQueSigue) VALUES (?,?)""", (follower.screen_name, "Steam"))
    db.commit()