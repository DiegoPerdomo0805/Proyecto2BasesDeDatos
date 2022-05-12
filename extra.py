import utilities
import conexion
import player


def prog():
    print("Contenido en progreso")

    sql = ("SELECT t.nombre from titulos t where t.id in (SELECT f.id_titulo from viendo f where f.perfil like %s);")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)

    sql = ("SELECT f.id_titulo from viendo f where f.perfil like %s;")
    args = (utilities.getProfile(),)  # RECORDA SIEMPRE PO
    ids = conexion.executeQuery(sql, args, True)

    choice = utilities.menu3(ids, nombres)
    print(choice)


def finalizado():
    print("Contenido finalizado")

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


def sugerencia():
    print("Contenido sugerido")

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
