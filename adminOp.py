from ctypes import util
import conexion
import buscares
import main
import player
import utilities


def modificarUsuario(): 

    print("Ingrese el correo del usuario para modificar")

    email = input()
    id = ""

    while(True):
        sql = ("SELECT c.cuenta_id from cuenta c where c.correo like %s;")
        args = (email,)
        results = conexion.executeQuery(sql, args, True) 

        id = utilities.cleanSingle2(results)

        if(len(results) == 0):
            print("Correo no encontrado\n")
            print("Ingrese el correo del usuario para modificar")
            email = input()
        else:
            break

    mail = input("Ingrese su nuevo correo electrónico: ")
    print("\nIngrese el nuevo tipo de cuenta del usuario.")
    opciones = ["Básica", "Estándar", "Premium"]
    contra = utilities.encryption(utilities.contra())
    tier = utilities.menus(opciones)
    sql = ("UPDATE cuenta set correo = %s, nivel_cuenta = %s, pssword = %s where cuenta_id = %s;")
    args = (mail, tier, contra, id)
    conexion.executeQuery(sql, args) 


def quitarUsuario():

    print("Ingrese el correo del usuario para eliminar")

    email = input()
    cuenta = ""

    while(True):
        sql = ("SELECT c.cuenta_id from cuenta c where c.correo like %s;")
        args = (email,)
        results = conexion.executeQuery(sql, args, True) 

        cuenta = utilities.cleanSingle2(results)

        if(len(results) == 0):
            print("Correo no encontrado\n")
            print("Ingrese el correo del usuario para eliminar")
            email = input()
        else:
            break
    sql = ("UPDATE perfiles set active = false where cuenta = %s")
    args = (cuenta,)
    conexion.executeQuery(sql, args, False)

    sql = ("DELETE from cuenta where cuenta_id = %s;")
    args = (cuenta,)
    conexion.executeQuery(sql, args, False)



def modificarPerfil():  # FALTA MOMO

    print("Ingrese la cuenta del perfil que desea modificar")
    email = input()
    id = ""

    while(True):
        sql = ("SELECT c.cuenta_id from cuenta c where c.correo like %s;")
        args = (email,)
        results = conexion.executeQuery(sql, args, True) 

        id = utilities.cleanSingle2(results)

        if(len(results) == 0):
            print("Correo no encontrado\n")
            print("Ingrese la cuenta del perfil que desea modificar")
            email = input()
        else:
            break
    print("Que perfil desea seleccionar?")
    query = ("SELECT p.perfil from perfiles p where p.cuenta = %s  and p.active ;")
    data = (id, )
    resultadoQ = conexion.executeQuery(query, data, True)
    nombres = resultadoQ
    query = ("SELECT p.perfil_id from perfiles p where p.cuenta = %s  and p.active ;")
    data = (id, )
    resultadoQ = conexion.executeQuery(query, data, True)
    ids = resultadoQ
    perfil = utilities.cleanSingle2(utilities.menu3(ids, nombres))

    nombre = input("ingrese el nombre nuevo del perfil: ")
    active = (True if utilities.menus(["Activo", "No activo"]) == 1 else False)

    query = ("UPDATE perfiles set perfil = %s, active = %s where cuenta = %s and perfil_id = %s;")
    data = (nombre, active, id, perfil, )
    conexion.executeQuery(query, data)

    

def quitarPerfil():  # FALTA MOMO

    print("Ingrese la cuenta del perfil que desea modificar")
    email = input()
    id = ""

    while(True):
        sql = ("SELECT c.cuenta_id from cuenta c where c.correo like %s;")
        args = (email,)
        results = conexion.executeQuery(sql, args, True) 

        id = utilities.cleanSingle2(results)

        if(len(results) == 0):
            print("Correo no encontrado\n")
            print("Ingrese la cuenta del perfil que desea modificar")
            email = input()
        else:
            break
    print("Que perfil desea seleccionar?")
    query = ("SELECT p.perfil from perfiles p where p.cuenta = %s  and p.active ;")
    data = (id, )
    resultadoQ = conexion.executeQuery(query, data, True)
    nombres = resultadoQ
    query = ("SELECT p.perfil_id from perfiles p where p.cuenta = %s  and p.active ;")
    data = (id, )
    resultadoQ = conexion.executeQuery(query, data, True)
    ids = resultadoQ
    perfil = utilities.cleanSingle2(utilities.menu3(ids, nombres))
    query = ("UPDATE perfiles set active = false where cuenta = %s and perfil_id = %s")
    data = (id, perfil, )
    conexion.executeQuery(query, data)




def nuevoAnuncio():
    print("\nEscoja un contenido para ver de la lista de favoritos")

    sql = ("SELECT t.nombre from titulos t where t.id in (SELECT f.id_titulo from favoritos f where f.perfil like %s);")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)

    sql = ("SELECT f.id_titulo from favoritos f where f.perfil like %s;")
    args = (utilities.getProfile(),)  # RECORDA SIEMPRE PO
    ids = conexion.executeQuery(sql, args, True)

    choice = utilities.menu3(ids, nombres)
    print(choice)

    player.videoPlayer(choice)


def quitar():
    print("\Escoja un contenido para borrar de la lista de favoritos")

    sql = ("SELECT t.nombre from titulos t where t.id in (SELECT f.id_titulo from favoritos f where f.perfil like %s);")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)

    sql = ("SELECT f.id_titulo from favoritos f where f.perfil like %s;")
    args = (utilities.getProfile(),)  # RECORDA SIEMPRE PO
    ids = conexion.executeQuery(sql, args, True)

    choice = utilities.menu3(ids, nombres)
    print(choice)

    sql = ("DELETE from favoritos where perfil = %s and id_titulo = %s;")
    args = (utilities.getProfile(), choice,)  # RECORDA SIEMPRE PO
    ids = conexion.executeQuery(sql, args, True)
