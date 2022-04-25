import conexion, busqueda, main, player

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
    
    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: aqui vamos a imprimir todos los contenidos en favoritos

    #hacer un for

    print("Ingrese el numero del contenido que desea ver: ")

    userData = input()

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    player.videoPlayer(id)

def quitar():
    print("Ingrese el nombre del contenido que desea eliminar")

    userData = input()

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Aqui solo vayamos eliminando las cosas de favoritos
    

