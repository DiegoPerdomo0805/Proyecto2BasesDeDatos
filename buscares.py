from scipy.fft import idst
import conexion, player, utilities
from datetime import date
from utilities import menus

def busquedas():
    bandera = True
    while(bandera):

         print("Busqueda por:")
         print("1. Nombre \n2. Director \n3. Actor \n4. Genero \n5. Categoria \n6. Estreno \n 7. Premios \n8. Regresar")

         userData  =  input()

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
               bandera = False

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")

def nombre():
    print("Ingrese el nombre del contenido")

    userData  =  input()
    registerSearch(userData)
    userData = "%" + userData + "%"


    sql = ("SELECT t.nombre from titulos t where lower(t.nombre) like lower(%s);")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True) 
    sql = ("SELECT t.id from titulos t where lower(t.nombre) like lower(%s);")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results0 = conexion.executeQuery(sql, args, True) 
    if(len(results) == 0):
        print("No hay títulos que cumplan el requisito")
    else:
        resultado(results0, results)

def director():
    print("Ingrese el nombre del director")

    userData  =  input()
    registerSearch(userData)
    userData = "%" + userData + "%"

    sql = ("SELECT t.nombre from titulos t where t.id in(SELECT td.id from titulo_director td inner join director d on td.director = d.id_director where lower(d.nombre) like  lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True)
    sql = ("SELECT td.id from titulo_director td inner join director d on td.director = d.id_director where lower(d.nombre) like  lower(%s);")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results0 = conexion.executeQuery(sql, args, True) 

    if(len(results) == 0):
        print("No hay títulos que cumplan el requisito")
    else:
        resultado(results0, results)

def stelar():
    print("Ingrese el nombre de uno de los actores o actrices principales")

    userData  =  input()
    registerSearch(userData)
    userData = "%" + userData + "%"

    sql = ("SELECT t.nombre from titulos t where t.id in( SELECT ta.id from titulo_actores ta inner join actor a on ta.actor = a.id_actor where lower(a.nombre) like  lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    results = conexion.executeQuery(sql, args, True) 
    sql = ("SELECT ta.id from titulo_actores ta inner join actor a on ta.actor = a.id_actor where lower(a.nombre) like  lower(%s);")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA
    results0 = conexion.executeQuery(sql, args, True)

    if(len(results) == 0):
        print("No hay títulos que cumplan el requisito")
    else:
        resultado(results0, results)

def genero():
    print("Ingrese el genero del contenido")

    userData  =  input()
    registerSearch(userData)

    sql = ("SELECT t.nombre from titulos t where t.id in(SELECT td.id from titulo_details td inner join generos g on td.genero = g.id_genero where lower(g.nombre) like  lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    names = conexion.executeQuery(sql, args, True)
    sql = ("SELECT td.id from titulo_details td inner join generos g on td.genero = g.id_genero where lower(g.nombre) like  lower(%s);")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    ids = conexion.executeQuery(sql, args, True)
    
    if(len(names) == 0):
        print("No hay títulos que cumplan el requisito")
    else:
        resultado(names, ids)
     
def categoria():
    print("Ingrese si se desea ver películas o series")
    print("1. Peliculas\n2.Series")

    flag = True
    while(flag):
        try:
            userData  =  input()
            registerSearch(userData)
            op = int(userData)
            if(op in range(2)):
                if op==1:
                    sql = ("SELECT t.nombre from titulos t where t.id in(SELECT p.id from peliculas p);")
                    args = ("")#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
                    names = conexion.executeQuery(sql, args, True) 
                    sql = ("SELECT p.id from peliculas p;")
                    args = ("")#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
                    ids = conexion.executeQuery(sql, args, True) 
                    resultado(ids, names)
                else:
                    sql = ("SELECT t.nombre from titulos t where t.id in(SELECT s.id from series s);")
                    args = ("")#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
                    names = conexion.executeQuery(sql, args, True) 
                    sql = ("SELECT p.id from series p;")
                    args = ("")#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
                    ids = conexion.executeQuery(sql, args, True) 
                    resultado(ids, names)

        except:
            print("opción no válida")


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
                    names = conexion.executeQuery(sql, args, True) 
                    sql = ("SELECT t.id from titulos t where t.id in(SELECT td.id from titulo_details td where td.release_date between %s and %s;")
                    args = (de,hasta,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE 
                    ids = conexion.executeQuery(sql, args, True) 
                    resultado(ids, names)
                    flag = False
        except:
            print("Formato no aceptado\n")
          

    

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def premios():
    print("Ingrese el nombre del contenido")

    userData  =  input()
    registerSearch(userData)
    
    sql = ("SELECT t.nombre from titulos t where t.id in( SELECT p.id_titulo from premiados p inner join premios p2 on p.id_premio = p2.id where lower(p2.nombre) like lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    names = conexion.executeQuery(sql, args, True) 
    sql = ("SELECT t.id from titulos t where t.id in( SELECT p.id_titulo from premiados p inner join premios p2 on p.id_premio = p2.id where lower(p2.nombre) like lower(%s));")
    args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    ids = conexion.executeQuery(sql, args, True) 
    resultado(ids, names)


def resultado(ids, names):

    opcion = utilities.menu3(ids, names)
    opcion = utilities.cleanSingle2(opcion)
    player.videoPlayer(opcion)


def registerSearch(search):
    sql = ("INSERT into historial (busqueda) values (%s);")
    args = (search,)
    conexion.executeQuery(sql, args)