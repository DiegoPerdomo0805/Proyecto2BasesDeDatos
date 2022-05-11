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
    userData = "%" + userData + "%"
    id = ""

    while(True):
        sql = ("SELECT id from anunciantes a  where lower(a.nombre) like  lower(%s);")
        args = (userData,)
        results = conexion.executeQuery(sql, args, True) 

        if(len(results) == 0):
            print("\n\tNo se encontro anunaciante con ese nombre. Verifique que este escrito correctamente")
        else:
            id = utilities.cleanSingle2(utilities.menus2(utilities.createArray(results)))
            break

    print("Ingrese el nombre modificado")

    userData = input()

    sql = ("UPDATE anunciantes set nombre = %s where id = %s")
    args = (userData,id,)
    conexion.executeQuery(sql, args, False) 

    print("Nombre cambiado exitosamente")

def agregarAnunciante():
    unready  = True
    while unready:
        print("Ingrese el nombre del nuevo anunciante")
        userData = input()
        userData = "%" + userData + "%"

        sql = ("SELECT id from anunciantes a  where lower(a.nombre) like  lower(%s)")
        args = (userData,)
        results = conexion.executeQuery(sql, args, True)
        if(len(results) == 0):
            print("Ya hay anunciante con ese nombre")
        else:
            userData = input()
            codigo = utilities.createID(5)
            sql = ("INSERT into anunciantes (id, nombre) values (%s, %s)")
            args = (id, userData,)
            conexion.executeQuery(sql, args) 
            unready = False
    # sql = ("select id_anunciante from anunciante where nombre_empresa = %s")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 


def agregarAnuncio():

    print("Ingrese el nombre del nuevo anuncio")
    userData = input()

    # sql = ("select id_anunciante from anunciante where nombre_empresa = %s")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 