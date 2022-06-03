from ctypes import util
import conexion
import buscares
import main
import player
import utilities
import datetime


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

    print("Ingrese el correo de la cuenta del perfil que desea modificar")
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

    query = (
        "UPDATE perfiles set perfil = %s, active = %s where cuenta = %s and perfil_id = %s;")
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


def simulacion():
    print("\nIngrese la información con la que desea simluar las reproducciones.\nIngrese la fecha en la que se generarán las reproducciones")
    stop = True
    y = 0
    m = 0
    d = 0
    while(stop):
        try:
            print("Ingrese el año de la fecha, a partir del 2010 hasta el actual")
            y1 = input()
            y = int(y1)
            print("Ingrese el mes de la fecha, no puede exceder a la fecha actual si eligió 2022")
            m1 = input()
            m = int(m1)
            print("Ingrese el día de la fecha, no puede exceder a la fecha actual si eligió 2022")
            d1 = input()
            d = int(d1)
            if datetime.date(y,m,d) > datetime.date.today() or datetime.date(y,m,d) < datetime.date(2010,1,1):
                print("Fecha inválida\n")
            else:
                print("Fecha elegida: " , datetime.date(y,m,d), "\n")
                stop = False
        except:
            print("Siga el formato indicado\n")

    q = 0
    stop = True
    print("Ingrese la cantidad de visualizaciones que desea generar\n¡ADVERTENCIA! Generar más de 400 visualizaciones puede resultar tardado y todas serán generadas como terminadas de ver, sin importar la cantidad.")
    while(stop):
        try:
            print("Ingrese la cantidad de visualizaciones")
            q1 = input()
            q = int(q1)
            if(q>0 and q<401):
                print("Se generarán ", q1, " visualizaciones\n")
                stop = False
            elif (q<=0):
                print("No se puede generar una cantidad negativa o nula\n")
            elif(q>1499):
                print("Generar 1500 visualizaciones en adelante puede ser demasiado tardado y puede causar problemas")
            else:
                print("ESTÁ A PUNTO DE GENERAR MÁS DE 400 VISUALIZACIONES, ESTE PROCESOS PUEDE SER TARDADO. GENERARÁ ", q1, " VISUALIZACIONES.\n")
                stop = False
        except:
            print("Debe ingresar un número\n")

    generarVisualizaciones(d, m, y, q)



def generarVisualizaciones(d, m, y, q):
    query = ("SELECT p.perfil_id from perfiles p where p.cuenta in (select cuenta_id from cuenta c where nivel_cuenta > 0 and cuenta_id > 13)")
    data = ("",)
    resultadoQ = conexion.executeQuery(query, data, True)
    perfiles = []
    for e in resultadoQ:
        perfiles.append(utilities.cleanSingle2(e))
    query = ("SELECT t.id from titulos t ")
    data = ("",)
    resultadoQ = conexion.executeQuery(query, data, True)
    titulos = []
    for e in resultadoQ:
        titulos.append(utilities.cleanSingle2(e))
    day = str(d)
    month = str(m)
    year = str(y)
    fecha = year + "-" + month + "-" + day
    i = 0
    while i < q:
        hora = utilities.random_date("1/4/2022 12:00 AM", "1/5/2022 12:00 AM", utilities.random.random())
        hora = utilities.clean_date(hora)
        l1 = len(perfiles)
        l2 = len(titulos)
        user = perfiles[utilities.random.randint(0, l1-1)]
        title = titulos[utilities.random.randint(0, l2-1)]
        query = (
            "SELECT * from watch_again wa where perfil like %s and id_titulo like %s")
        data = (user, title, )
        resultadoQ = conexion.executeQuery(query, data, True)
        if(len(resultadoQ) == 0):
            query = (
                "INSERT into watch_again (perfil, id_titulo, times_watched, date_watched, hour_watched) VALUES (%s, %s, %s, %s, %s);")
            data = (user, title, 1, fecha, hora, )
            conexion.executeQuery(query, data, False)
        else:
            query = ("UPDATE watch_again set times_watched = times_watched + 1, date_watched = %s, hour_watched = %s  where perfil like %s and id_titulo like %s;")
            data = (fecha, hora, user, title, )
            conexion.executeQuery(query, data, False)
        i = i + 1
    print("Visualizaciones generadas\n")




def modificaciones(cuenta, fecha):
    sql = ("INSERT into admins (email, fecha) values(%s, %s);")
    args = (cuenta, fecha, )
    conexion.executeQuery(sql, args, False)