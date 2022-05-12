import conexion
import buscares
import main
import player
import utilities


def favoritos():
    crea = True
    while(crea == True):

        print("1. Ver lista \n2. Regresar")

        userData = input()

        try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                verL()

            elif(userDataInt == 2):
                crea = False

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")


def verL():
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
