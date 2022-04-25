import main, utilities, conexion

def modificarUser():
    while(True):

        print("1. Modificar usuario\n2. dar de baja cuenta\n3. Regresar")

        userData = input()

        try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                modificar()

            elif(userDataInt == 2):
                eliminar()

            elif(userDataInt == 3):
                main.menu()

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")
    
def modificar():

    print("Ingrese el correo del usuario para modificar")

    userData = input()

    # while(True):
    #     sql = ("SELECT id_usuario from usuarios where email = %s;")
    #     args = (email,)
    #     results = conexion.executeQuery(sql, args, True) 
    
    #     id = str(results[0][0])

    #     if(len(results) == 0):
    #         print("Correo no encontrado")
    #     else:
    #         break

    print("Ingrese el nuevo tipo de cuenta del usuario. 1.Basica \n2. Estandar \n3.Avanzada")

    userData = input()
    # sql = ("update usuarios set tipo= %s where id_usuario = %s")
    # args = (selected, id)
    # databaseModule.executeQuery(sql, args) 

def eliminar():

    print("Ingrese el correo del usuario para modificar")

    userData = input()

    # while(True):
    #     sql = ("SELECT id_usuario from usuarios where email = %s;")
    #     args = (email,)
    #     results = databaseModule.executeQuery(sql, args, True) 
    
    #     id = str(results[0][0])

    #     if(len(results) == 0):
    #         print("\n\tNo se encontro usuario con ese nombre. Verifique que este escrito correctamente")
    #     else:
    #         break

    # sql = ("update usuarios set tipo= 'Desactivado' where id_usuario = %s")
    # args = (id,)
    # databaseModule.executeQuery(sql, args, False) 