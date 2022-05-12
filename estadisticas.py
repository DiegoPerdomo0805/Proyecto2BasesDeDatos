import main, utilities, conexion

def estadisticas():
    while(True):

         print("1. El top 10 de géneros de contenido más visto, y los minutos consumidos \n2. Cantidad de reproducciones por cada categoría, por tipo de cuenta \n3. El top 10 de los directores y actores principales de las películas que los perfiles estándar y avanzados han visto \n4. La cantidad de cuentas avanzadas que se han creado en los últimos 6 meses \n5. Para una fecha específica, ¿cuál es la hora pico donde el servicio es más utilizado? \n6. Regresar")

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
               main.menu()

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")

def opcion1():
    print("\nPelículas")
    sql = ("SELECT (select g.nombre from generos g where g.id_genero = td.genero) as genero, sum(p.duracion * wa.times_watched) as minutos from titulo_details td inner join peliculas p on p.id = td.id inner join watch_again wa on wa.id_titulo = p.id group by genero order by minutos desc limit 10;")
    args = ("",)
    results = conexion.executeQuery(sql, args, True) 
    i = 1
    for e in results:
      print(i, " . ", e)
      i = i + 1

    print("\nSeries")
    sql = ("SELECT (select g.nombre from generos g where g.id_genero = td.genero) as genero, sum(s.episodios * 40 * wa.times_watched) as minutos from titulo_details td inner join series s on s.id = td.id inner join watch_again wa on wa.id_titulo = s.id group by genero order by minutos desc limit 10;")
    args = ("",)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    i = 1
    for e in results:
      print(i, " . ", e)
      i = i + 1 


    #MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer

def opcion2():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer

def opcion3():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer

def opcion4():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer

def opcion5():
    print("jaja")

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Tambien como antes, solo imprimi y aqui lo que toque hacer
