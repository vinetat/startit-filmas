import os
import psycopg2

# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
# Vienkāršam testam var nomainīt šīs vērtības pret konkrētiem lielumiem

ELEPHANT_HOST = os.getenv("balarama.db.elephantsql.com") # "balarama.db.elephantsql.com"
ELEPHANT_NAME = os.getenv("poowmrnk") # "manadb"
ELEPHANT_PASSWORD = os.getenv("HGu4YyfKk5Ug0T2XgdL0fynihci1p9pm") # "managaraparole"


def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result