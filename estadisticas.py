from matplotlib.style import use
from numpy import empty
import main
import utilities
import conexion
from datetime import date


def estadisticas():
    crea = True
    while(crea == True):

        print("1. El top 10 de géneros de contenido más visto, y los minutos consumidos \n2. Cantidad de reproducciones por cada categoría, por tipo de cuenta \n3. El top 10 de los directores y actores principales de las películas que los perfiles estándar y avanzados han visto \n4. La cantidad de cuentas avanzadas que se han creado en los últimos 6 meses \n5. Para una fecha específica, ¿cuál es la hora pico donde el servicio es más utilizado? \n6. El top 5 de contenido visto en cada hora, de 9:00 a.m a 1:00 a.m para un mes dado.\n7. El top 10 de los términos que los usuarios buscan (no necesariamente debe estar el contenido, actores, etc., en la plataforma), esto le sirve a los administradores para saber qué contenido se debe ir añadiendo al servicio. Ej: las últimas películas de Marvel.\n8. El top 5 de los administradores que más modificaciones realizan en las cuentas de usuario para un rango de fechas dado\n9. El top 20 de películas que comenzaron a verse pero que llevan más de 20 días sin finalizarse, para un rango de fechas dado.\n10. Regresar")

        userData = input()

        try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                opcion1()

            elif(userDataInt == 2):
                opcion2()

            elif(userDataInt == 3):
                opcion3()

            elif(userDataInt == 4):
                opcion4()

            elif(userDataInt == 5):
                opcion5()

            elif(userDataInt == 6):
                opcion6()

            elif(userDataInt == 7):
                opcion7()

            elif(userDataInt == 8):
                opcion8()

            elif(userDataInt == 9):
                opcion9()

            elif(userDataInt == 10):
                crea = False

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")


def opcion1():
    print("\nPelículas")
    sql = ("SELECT (SELECT g.nombre from generos g where g.id_genero = td.genero) as genero, sum(p.duracion * wa.times_watched) as minutos from titulo_details td inner join peliculas p on p.id = td.id inner join watch_again wa on wa.id_titulo = p.id group by genero order by minutos desc limit 10;")
    args = ("",)
    results = conexion.executeQuery(sql, args, True)
    i = 1
    for e in results:
        print(i, " . ", e)
        i = i + 1

    print("\nSeries")
    sql = ("SELECT (SELECT g.nombre from generos g where g.id_genero = td.genero) as genero, sum(s.episodios * 40 * wa.times_watched) as minutos from titulo_details td inner join series s on s.id = td.id inner join watch_again wa on wa.id_titulo = s.id group by genero order by minutos desc limit 10;")
    args = ("",)  # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    i = 1
    for e in results:
        print(i, " . ", e)
        i = i + 1

    # MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer


def opcion2():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True)

    # MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer


def opcion3():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True)

    # MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer


def opcion4():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True)

    # MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer


def opcion5():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True)

    # MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer


def opcion6():
    crea = True
    while(crea):

        print("ingrese un mes en numeros")
        userData = input()

        try:
            userDataInt = int(userData)

            if(userDataInt <= 12 or userDataInt >= 1):
                crea = False

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")

    sql = ("SELECT (SELECT t.nombre from titulos t where t.id like wa.id_titulo) ,  sum(wa.times_watched) as reproducciones from watch_again wa where wa.hour_watched not between '01:00:01' and '08:59:59' and extract(month from wa.date_watched) = %s group by wa.id_titulo order by reproducciones desc limit 5")
    args = (userData,)  # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    if results is None:
        print("Vacio")
    else:
        if results.__len__() > 1 :
            i = 1
            for e in results:
                print(i, " . ", e)
                i = i + 1
            print("\n")
        else:
            print(results,"\n")


def opcion7():
    sql = ("SELECT lower(busqueda) as termino , count(*) as times from historial h group by lower(busqueda) limit 10 ")
    results = conexion.executeQuery(sql, True)
    if results is None:
        print("Vacio")
    else:
        if results.__len__() > 1 :
            i = 1
            for e in results:
                print(i, " . ", e)
                i = i + 1
            print("\n")
        else:
            print(results,"\n")


def opcion8():
    print("jaja")
    crea = True
    f1 = ""
    f2 = ""
    while(crea):

        print("Va a ingresar dos fechas en orden cronológico; la segunda debe ser la más reciente")
        userData = input()

        try:
            date_entry = input('Ingrese la primera fecha en formato YYYY-MM-DD / año-mes-dia: ')
            year, month, day = map(int, date_entry.split('-'))
            f1 = date_entry
            try:
                date_entry = input('Ingrese la primera fecha en formato YYYY-MM-DD / año-mes-dia: ')
                year, month, day = map(int, date_entry.split('-'))
                f2 = date_entry
                crea = False
            except:
                print("El valor debe ser el formato dado")
        except:
            print("El valor debe ser el formato dado")
    sql = ("SELECT a.email, count(*) as modificaciones from admins a where a.fecha between %s and %s  group by email limit 5")
    args = (f1, f2,)  # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    if results is None:
        print("Vacio")
    else:
        if results.__len__() > 1 :
            i = 1
            for e in results:
                print(i, " . ", e)
                i = i + 1
            print("\n")
        else:
            print(results,"\n")

    


def opcion9():
    print("jaja")

    today = date.today()

    sql = ("SELECT (SELECT t.nombre from titulos t where t.id like v.id_titulo) as nombre, v.fecha from viendo v where extract(epoch from (%s::timestamp - fecha::timestamp))/86400 > 20 limit 20")
    args = (today,)  # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    if results is None:
        print("Vacio")
    else:
        if results.__len__() > 1 :
            i = 1
            for e in results:
                print(i, " . ", e)
                i = i + 1
            print("\n")
        else:
            print(results,"\n")
