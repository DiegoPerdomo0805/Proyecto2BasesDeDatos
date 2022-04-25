import conexion, busqueda, main, player

def favoritos():
    while(True):

         print("Busqueda por:")
         print("1. Ver lista \n2. Ver contenido \n3. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                verL()

            elif(userDataInt == 2):
               ver()

            elif(userDataInt == 3):
               main.menu

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")

def verL():
    print("\nCONTENIDO!")

def ver():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: aqui hay que mandarle el id para que pueda reproducir el video, el id del contenido
    player.videoPlayer(id)

def quitar():
    print("Ingrese el nombre del contenido que desea eliminar")

    userData = input()

    # sql = ("SELECT nombre from nombre where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    #MOMO: Aqui solo vayamos eliminando las cosas de favoritos
    

