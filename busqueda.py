import conexion, main, player

def busqueda():
    while(True):

         print("Busqueda por:")
         print("1. Nombre \n2. Director \n3. Stelar \n4. Genero \n5. Categoria \n6. Estreno \n 7. Premios \n8. Regresar")

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

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def director():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True)

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id) 

def stelar():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def genero():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True)
     
    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)
     
def categoria():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def estreno():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)

def premios():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

    # MOMO: aqui consigamos el id
    # player.videoPlayer(id)