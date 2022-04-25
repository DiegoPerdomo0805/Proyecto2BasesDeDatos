import psycopg2

con=psycopg2.connect(user="postgres", password="NYARLATHOTEP", host="localhost", port="5432", database="proyecto2")

con.autocommit = True
cursor = con.cursor()

def executeQuery(query, args, fetch = False):
    cursor.execute(query, args)
    
    if(fetch):
        return(cursor.fetchall())