import conexion, main

def busqueda():
    while(True):

         print("Busqueda por:")
         print("1. Nombre \n2. Director \n3. Stelar \n4. Genero \n5. Categoria \n6. Estreno \n 7. Premios \n8. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userData == 1):
                nombre()

            elif(userData == 2):
               director()

            elif(userData == 3):
               stelar()

            elif(userData == 4):
               genero()

            elif(userData == 5):
               categoria()

            elif(userData == 6):
               estreno()

            elif(userData == 7):
               premios()

            elif(userData == 8):
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

def director():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

def stelar():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

def genero():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 
def categoria():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

def estreno():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 

def premios():
    print("Ingrese el nombre del contenido")

    userData = input()

    # sql = ("SELECT nombre, link from contenido where nombre = %s;")
    # args = (userData,)#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    # results = conexion.executeQuery(sql, args, True) 
