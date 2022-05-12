import conexion
import busqueda
import main
import player
import utilities


def modificarUsuario():  # FALTA MOMO

    print("Ingrese la cuenta que desea remover")
    cuenta = input()
    sql = ("DELETE from perfiles where cuenta = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (cuenta,)
    nombres = conexion.executeQuery(sql, args, True)

    print("Ingrese el correo que desea remover")
    cuenta = input()
    sql = ("DELETE from cuenta where correo = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)


def quitarUsuario():

    print("Ingrese la cuenta que desea remover")
    cuenta = input()
    sql = ("DELETE from perfiles where cuenta = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (cuenta,)
    nombres = conexion.executeQuery(sql, args, True)

    print("Ingrese el correo que desea remover")
    cuenta = input()
    sql = ("DELETE from cuenta where correo = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)


def agrgarUsuario():

    print("Ingrese el email de su usuario")
    email = input()

    query = ("SELECT * from cuenta where correo=%s;")
    data = (email,)
    resultadoQ = conexion.executeQuery(query, data, True)

    if(len(resultadoQ) >= 0):
        print("correo invalido")
    else:
        opciones = ["Básica", "Estándar", "Premium"]
        tier = utilities.menus(opciones)
        psswrd = utilities.contra()
        psswrd = utilities.encryption(psswrd)
        sql = ("INSERT INTO cuenta (nivel_cuenta, pssword , correo) VALUES (%s, %s, %s);")
        # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
        args = (tier, psswrd, email, )
        conexion.executeQuery(sql, args, False)
        query = ("SELECT nivel_cuenta from cuenta where correo=%s;")
        data = (email,)
        resultadoQ = conexion.executeQuery(query, data, True)
        query = ("SELECT cuenta_id from cuenta where correo=%s;")
        data = (email,)
        resultadoQ = conexion.executeQuery(query, data, True)
        cuenta_id = utilities.getSession()

        query = (
            "SELECT count(perfil_id) from perfiles p where p.active and p.cuenta =%s;")
        data = (cuenta_id,)
        resultadoQ = conexion.executeQuery(query, data, True)


def modificarPerfil():  # FALTA MOMO

    print("Ingrese la cuenta que desea remover")
    cuenta = input()
    sql = ("DELETE from perfiles where cuenta = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (cuenta,)
    nombres = conexion.executeQuery(sql, args, True)

    print("Ingrese el correo que desea remover")
    cuenta = input()
    sql = ("DELETE from cuenta where correo = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)


def quitarPerfil():  # FALTA MOMO

    print("Ingrese la cuenta que desea remover")
    cuenta = input()
    sql = ("DELETE from perfiles where cuenta = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (cuenta,)
    nombres = conexion.executeQuery(sql, args, True)

    print("Ingrese el correo que desea remover")
    cuenta = input()
    sql = ("DELETE from cuenta where correo = %s;")
    # RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
    args = (utilities.getProfile(),)
    nombres = conexion.executeQuery(sql, args, True)


def agrgarPerfil():

    print("Ingrese la cuenta a la que desea agregar un perfil")
    cuenta = input()

    unready = True
    while(unready):
        print("Ingrese el nombre para su perfil")
        name = input()
        perfil_id = utilities.createID(8)
        if (name.__len__() <= 10) and (name.__len__() > 0):
            query = (
                "INSERT INTO perfiles (cuenta, perfil, active, perfil_id) VALUES (%s,%s,'True',%s);")
            data = (cuenta, name, perfil_id, )
            conexion.executeQuery(query, data, False)
            query = (
                "SELECT count(perfil_id) from perfiles p where p.active and p.cuenta =%s;")
            data = (utilities.getSession(),)
            resultadoQ = conexion.executeQuery(query, data, True)
            perfiles = int(utilities.cleanSingle(resultadoQ))
            unready = False
        else:
            print("El nombre del perfil no debe pasar de los 10 caracteres.\n")


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
