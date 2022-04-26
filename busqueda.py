import conexion, main, player, utilities
from datetime import date
from utilities import menus, range

def busqueda():
    while(True):

         print("Busqueda por:")
         print("1. Nombre \n2. Director \n3. Actor \n4. Genero \n5. Categoria \n6. Estreno \n 7. Premios \n8. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                nombre()

            elif(userDataInt == 2):
               director()

            elif(userDataInt == 3):
               stelar()

            elif(userDataInt == 4):
               genero()

            elif(userDataInt == 5):
               categoria()

            elif(userDataInt == 6):
               estreno()

            elif(userDataInt == 7):
               premios()

            elif(userDataInt == 8):
               main.menu()

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")

def nombre():
    print("Ingrese el nombre del contenido")

    userData = input()
    userData = "%" + userData + "%"


    sql = ("SELECT t.nombre from titulos t where lower(t.nombre) like lower(%s);")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True) 

    resultado(results)

def director():
    print("Ingrese el nombre del director")

    userData = input()
    userData = "%" + userData + "%"

    sql = ("SELECT t.nombre from titulos t where t.id in(SELECT td.id from titulo_director td inner join director d on td.director = d.id_director where lower(d.nombre) like  lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)

    resultado(results)

def stelar():
    print("Ingrese el nombre de uno de los actores o actrices principales")

    userData = input()
    userData = "%" + userData + "%"

    sql = ("SELECT t.nombre from titulos t where t.id in( select ta.id from titulo_actores ta inner join actor a on ta.actor = a.id_actor where lower(a.nombre) like  lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True) 

    resultado(results)

def genero():
    print("Ingrese el genero del contenido")

    userData = input()

    sql = ("SELECT t.nombre from titulos t where t.id in(select td.id from titulo_details td inner join generos g on td.genero = g.id_genero where lower(g.nombre) like  lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    
    resultado(results)
     
def categoria():
    print("Ingrese si se desea ver películas o series")
    print("1. Peliculas\n2.Series")

    flag = True
    while(flag):
        try:
            userData = input()
            op = int(userData)
            if(range(op, 2)):
                if op==1:
                    sql = ("SELECT t.nombre from titulos t where t.id in(select p.id from peliculas p);")
                    args = ("")#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
                    results = conexion.executeQuery(sql, args, True) 
                else:
                    sql = ("SELECT t.nombre from titulos t where t.id in(select s.id from series s);")
                    args = ("")#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
                    results = conexion.executeQuery(sql, args, True) 

        except:
            print("opción no válida")

    resultado(results)

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def estreno():
    flag = True 
    while(flag):
        print("Ingrese el año que el contenido se estrenó")
        try:
            userData=input()
            year = int(userData)
            now = date.today().year
            
            if year > now or year < 1900:
                    print("Año inválido")
            else:
                    de = userData + "-01-01"
                    hasta = userData + "-12-31"
                    sql = ("SELECT t.nombre from titulos t where t.id in(SELECT td.id from titulo_details td where td.release_date between %s and %s;")
                    args = (de,hasta,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE 
                    results = conexion.executeQuery(sql, args, True) 

                    flag = False
        except:
            print("Formato no aceptado\n")
    
    resultado(results)
      

    

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def premios():
    print("Ingrese el nombre del contenido")

    userData = input()

    sql = ("SELECT t.nombre from titulos t where t.id in( SELECT p.id_titulo from premiados p inner join premios p2 on p.id_premio = p2.id where lower(p2.nombre) like lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True) 

    resultado(results)


def resultado(results):

    opcion = utilities.menus2(results)

    player.videoPlayer(opcion)
