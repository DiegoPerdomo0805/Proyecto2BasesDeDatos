import conexion, busqueda, main, player, utilities

def favoritos():
    while(True):

         print("1. Ver lista \n2. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                verL()

            elif(userDataInt == 2):
               main.menu

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")

def verL():
    print("\nCONTENIDO!")
    
    sql = ("SELECT t.nombre from titulos t where t.id in (SELECT f.id_titulo from favoritos f where f.perfil like %s);")
    args = (utilities.getProfile(),)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    nombres = conexion.executeQuery(sql, args, True) 

    sql = ("SELECT f.id_titulo from favoritos f where f.perfil like %s;")
    args =(utilities.getProfile(),)#RECORDA SIEMPRE PO
    ids = conexion.executeQuery(sql, args, True) 

    choice = utilities.menu3(ids, nombres)

    player.videoPlayer(choice)

def quitar():
    print("Ingrese el nombre del contenido que desea eliminar")

    userData = input()

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Aqui solo vayamos eliminando las cosas de favoritos
    

