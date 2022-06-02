import psycopg2

####con=psycopg2.connect(user="postgres", password="NYARLATHOTEP", host="localhost", port="5432", database="proyecto2")
con=psycopg2.connect(user="jose", password="AVNS_jSwbXXReHJ_sRzV", host="db-postgresql-nyc3-01635-do-user-11158832-0.b.db.ondigitalocean.com", port="25060", database="joseProyecto")

con.autocommit = True
cursor = con.cursor()


#En caso de reading, True
#En caso de escritura, modificación y borrado, False
def executeQuery(query, args, fetch = False):
    cursor.execute(query, args)
    
    if(fetch):
        return(cursor.fetchall())