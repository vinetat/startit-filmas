import os
import psycopg2
from flask import g


# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
ELEPHANT_HOST = os.getenv("balarama.db.elephantsql.com")
ELEPHANT_NAME = os.getenv("poowmrnk")
ELEPHANT_PASSWORD = os.getenv("HGu4YyfKk5Ug0T2XgdL0fynihci1p9pm")

# Pieslēguma konfigurācija
dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)


# DB savienojuma izveide
def connect_db():
    """Connects to the database."""
    conn = psycopg2.connect(dsn)
    return conn


# Saglabā DB savienojumu lietošanai atkārtoti
# g ir Flask iebūvēts objekts
# informācijas saglabāšanai viena pieprasījuma ietvaros
def get_db():
    if 'db' not in g:
        g.db = connect_db()
    return g.db


def get_one(sql, params):
    conn = get_db()
    c = conn.cursor()
    c.execute(sql, params)
    atbilde = c.fetchone()
    print("Vaicājums:\n{}\nAtbilde: {}".format(c.query, atbilde))
    c.close()
    return(atbilde)


def get_all(sql, params):
    conn = get_db()
    c = conn.cursor()
    c.execute(sql, params)
    atbilde = c.fetchall()
    print("Vaicājums:\n{}\nAtbilde: {}".format(c.query, atbilde))
    c.close()
    return(atbilde)


