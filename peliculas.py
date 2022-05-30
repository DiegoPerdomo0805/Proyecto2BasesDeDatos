# importing csv module
from calendar import month
import csv
from dataclasses import dataclass
from encodings import utf_8
from sys import prefix
from matplotlib.pyplot import title
import psycopg2
import uuid
import random
import time


def clean_date(single):
    single = str(single)
    begin = -1
    end = 0
    acu = 0
    for e in single:
        if e == "2" and begin < end:
            temp = acu
            temp2 = single[temp:temp+4]
            if temp2 == "2022":
                begin = acu + 1
        else:
            acu = acu + 1
    begin = begin + 3 + 1
    end = len(single)

    return single[begin:end]


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
######
######i = 0
# while i < 9:
######    tttt = random_date("1/4/2022 12:30 AM", "1/5/2022 12:00 AM", random.random())
# print(tttt)
# print(clean_date(tttt))
######    i = i +1


con = psycopg2.connect(user="postgres", password="NYARLATHOTEP",
                       host="localhost", port="5432", database="proyecto2")

con.autocommit = True
cursor = con.cursor()


# En caso de reading, True
# En caso de escritura, modificación y borrado, False
def executeQuery(query, args, fetch=False):
    con = psycopg2.connect(user="postgres", password="NYARLATHOTEP",
                           host="localhost", port="5432", database="proyecto2")
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute(query, args)

    if(fetch):
        return(cursor.fetchall())


def createID(l):
    _id = uuid.uuid1()
    _id = str(_id)
    return _id[0:l]


def cleanSingle2(single):
    single = str(single)
    begin = -1
    end = 0
    acu = 0
    for e in single:
        if e == "'" and begin < end:
            begin = acu + 1
        elif e == "'":
            end = acu
        acu = acu + 1
    return single[begin:end]


# csv file name
filename = r"C:\Users\DIEGO\Documents\UVG 2022\semestre 1\Base de datos 1\proyecto2\movies.csv"
filename = r"C:\Users\DIEGO\Documents\UVG 2022\semestre 1\Base de datos 1\proyecto2\all-series-ep-average.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, "rt", encoding="utf_8") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows

# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))
#
# printing first 5 rows
#print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#	# parsing each column of a row
#	for col in row:
#		print("%10s"%col,end=" "),
#	print('\n')
#
print("\n\npito\n\n")
for row in rows:
    # parsing each column of a row
    temp = "* " + str(row[1]) + "   -   " + str(row[2])
    #print(temp, "")


series = []
for row in rows:
    series.append(str(row[1]))

#print("\n\n\n", series)
# !!!!!!!!!!!!!!!!!NO DESCOMENTAR POR NADA DEL MUNDO!!!!!!!!!!!!!!!!!!!!!!
########l = len(series)
########
# print(l)
########
########i = 0
# while i < l:
########    unready = True
########    codigo = ""
# while(unready):
########        codigo  = createID(6)
########        query = ("SELECT id from titulos t where id like %s")
########        data = (codigo,)
########        resultadoQ = executeQuery(query, data, True)
# if(len(resultadoQ) == 0):
########            unready = False
########    query = ("INSERT INTO titulos (id, nombre, tipo) VALUES (%s, %s, %s);")
########    data = (codigo, series[i],"S",)
# executeQuery(query, data)    ####PELIGRO
########    i = i +1
########


query = ("SELECT p.perfil_id from perfiles p where p.cuenta in (select cuenta_id from cuenta c where nivel_cuenta > 0 and cuenta_id > 13)")
data = ("",)
resultadoQ = executeQuery(query, data, True)
perfiles = []
for e in resultadoQ:
    perfiles.append(cleanSingle2(e))
query = ("SELECT t.id from titulos t ")
data = ("",)
resultadoQ = executeQuery(query, data, True)
titulos = []
for e in resultadoQ:
    titulos.append(cleanSingle2(e))


# !!!!!!!!!!!!!!!!!NO DESCOMENTAR POR NADA DEL MUNDO!!!!!!!!!!!!!!!!!!!!!!
################user =  "a87f85c0"
################title = "6f3827"
################fecha = "2022-5-31"
################hora =  "07:44 AM"
################query = ("UPDATE watch_again set times_watched = times_watched + 1, date_watched = %s, hour_watched = %s  where perfil like %s and id_titulo like %s;")
################data = (fecha, hora, user, title, )
################executeQuery(query, data, False)
# 6b7a1c - samurai x

year = 2022
mes = 3
dia = 1


# !!!!!!!!!!!!!!!!!NO DESCOMENTAR POR NADA DEL MUNDO!!!!!!!!!!!!!!!!!!!!!!
########i = 0
########limit = 750
# while mes < 5:
########    fecha = str(year) + "-" + str(mes) + "-" + str(dia)
# while i < limit:
########        hora = random_date("1/4/2022 12:30 AM", "1/5/2022 12:00 AM", random.random())
########        hora = clean_date(hora)
########        l1 = len(perfiles)
########        l2 = len(titulos)
########        user = perfiles[random.randint(0,l1-1)]
########        title = titulos[random.randint(0,l2-1)]
########        print(fecha ,  " - ", hora,  " - ",user,  " - ",title)
########        query = ("SELECT * from watch_again wa where perfil like %s and id_titulo like %s")
########        data = (user, title, )
########        resultadoQ = executeQuery(query, data, True)
# if(len(resultadoQ) == 0):
########            query = ("INSERT into watch_again (perfil, id_titulo, times_watched, date_watched, hour_watched) VALUES (%s, %s, %s, %s, %s);")
########            data = (user, title, 1, fecha, hora, )
########            executeQuery(query, data, False)
# else:
########            query = ("UPDATE watch_again set times_watched = times_watched + 1, date_watched = %s, hour_watched = %s  where perfil like %s and id_titulo like %s;")
########            data = (fecha, hora, user, title, )
########            executeQuery(query, data, False)
########        i = i + 1
# print("\n------------------------------------------------------------------------------------------------------\n")
########    i = 0
# print(str(year), "-", str(mes) , "-" , str(dia))
# if(dia == 31 and mes == 3):
########        dia = 1
########        mes = 4
# elif(dia == 30 and mes == 4):
########        mes = 5
# else:
########        dia = dia + 1


# Aqui ingresas el número del día, el número del mes, el número del año y la cantidad de reproducciones que quieres insertar
def generarVisualizaciones(d, m, y, q):
    query = ("SELECT p.perfil_id from perfiles p where p.cuenta in (select cuenta_id from cuenta c where nivel_cuenta > 0 and cuenta_id > 13)")
    data = ("",)
    resultadoQ = executeQuery(query, data, True)
    perfiles = []
    for e in resultadoQ:
        perfiles.append(cleanSingle2(e))
    query = ("SELECT t.id from titulos t ")
    data = ("",)
    resultadoQ = executeQuery(query, data, True)
    titulos = []
    for e in resultadoQ:
        titulos.append(cleanSingle2(e))
    day = str(d)
    month = str(m)
    year = str(y)
    fecha = year + "-" + month + "-" + day
    i = 0
    while i < q:
        hora = random_date("1/4/2022 12:30 AM",
                           "1/5/2022 12:00 AM", random.random())
        hora = clean_date(hora)
        l1 = len(perfiles)
        l2 = len(titulos)
        user = perfiles[random.randint(0, l1-1)]
        title = titulos[random.randint(0, l2-1)]
        query = (
            "SELECT * from watch_again wa where perfil like %s and id_titulo like %s")
        data = (user, title, )
        resultadoQ = executeQuery(query, data, True)
        if(len(resultadoQ) == 0):
            query = (
                "INSERT into watch_again (perfil, id_titulo, times_watched, date_watched, hour_watched) VALUES (%s, %s, %s, %s, %s);")
            data = (user, title, 1, fecha, hora, )
            executeQuery(query, data, False)
        else:
            query = ("UPDATE watch_again set times_watched = times_watched + 1, date_watched = %s, hour_watched = %s  where perfil like %s and id_titulo like %s;")
            data = (fecha, hora, user, title, )
            executeQuery(query, data, False)
        i = i + 1


generarVisualizaciones(8, 5, 2022, 15)
