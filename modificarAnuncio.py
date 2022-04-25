import main, utilities, conexion

def modificarAnuncio():
    while(True):

        print("1. Agregar anunciante\n2. Agregar anuncio\n3. Modificar anunciante \n4. Regresar")

        userData = input()

        try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                agregarAnunciante()

            elif(userDataInt == 2):
                agregarAnuncio()

            elif(userDataInt == 3):
                modificarAnunciante()

            elif(userDataInt == 4):
                main.menu()

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")
    
def modificarAnunciante():

    print("1. Ingrese el nombre del anunciante a modificar")

    userData = input()

    # while(True):
    #     sql = ("SELECT id_anunciante from anunciante where nombre_empresa= %s;")
    #     args = (userData,)
    #     results = conexion.executeQuery(sql, args, True) 
    
    #     id = str(results[0][0])

    #     if(len(results) == 0):
    #         print("\n\tNo se encontro anunaciante con ese nombre. Verifique que este escrito correctamente")
    #     else:
    #         break

    print("1. Ingrese el nombre modificado")

    userData = input()

    # name = utils.textInput("Ingrese el nuevo nombre para el Anunciante ")
    # sql = ("update anunciante set nombre_empresa= %s where id_anunciante = %s")
    # args = (name,id)
    # conexion.executeQuery(sql, args) 

    # print("Nombre cambiado exitosamente)

def agregarAnunciante():

    print("Ingrese el nombre del nuevo anunciante")
    userData = input()

    # sql = ("select id_anunciante from anunciante where nombre_empresa = %s")
    # args = (userData,)
    # results = conexion.executeQuery(sql, args, True)

    print("Ingrese el nombre del nuevo anuncio")
    userData = input()

    # sql = ("select id_anunciante from anunciante where nombre_empresa = %s")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 


def agregarAnuncio():

    print("Ingrese el nombre del nuevo anuncio")
    userData = input()

    # sql = ("select id_anunciante from anunciante where nombre_empresa = %s")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 