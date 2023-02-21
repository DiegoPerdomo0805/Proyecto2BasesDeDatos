from hashlib import md5
import time
from unicodedata import name
import uuid
import time
import random

userName = ''
userProfile = ''
userType = ''
adTime = 15
userProfiles = 0

# Funciones para manejo de tiempo


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


def clean_date(single):
    single = str(single)
    begin = -1
    end = 0
    acu = 0
    for e in single:
        if e == "2" and begin < end:
            temp = acu
            temp2 = single[temp:temp+4]
            if temp2 == "2022":
                begin = acu + 1
        else:
            acu = acu + 1
    begin = begin + 3 + 1
    end = len(single)

    return single[begin:end]



# funcion de encriptado usando md5


def encryption(psswrd):
    cntr = psswrd
    c_e = md5()
    c_e.update(cntr.encode())
    return c_e.hexdigest()


def passlen(psswrd):
    if len(psswrd) > 7 and len(psswrd) < 50:
        return True
    else:
        return False

# SET GET DE LA INFO DE LA CUENTA


def setSession(user=""):
    global userName
    userName = user


def getSession():
    return userName

# SET GET DEL TIPO DE CUENTA


def setType(type):
    global userType
    userType = type


def getType():
    return userType

# SET GET DE LA INFO DEL PERFIL


def setProfile(profile=""):
    global userProfile
    userProfile = profile


def getProfile():
    return userProfile

# Profiles siendo la cantidad de perfiles que una cuenta tiene
# Sirve para tener en cuenta la cantiddad de perfiles que uno debería tener en función de su tipo de cuenta


def setProfiles(profiles):
    global userProfiles
    userProfiles = profiles


def getProfiles():
    return userProfiles

# def range(x, l):
#    if x > 0 and x<= l:
#        return True
#    else:
#        return False


def setTime(time=15):
    global adTime
    adTime = time


def getTime():
    return adTime


def menus(opciones):
    """Crea menú con las opciones dadas por el usario
    en una lista y verifica que esten en el rango especificado"""
    if len(opciones) > 1:
        length = len(opciones)
        for i in range(length):
            print(i+1, ". ", opciones[i])
    else:
        print("1. ", opciones[0])

    ciclo = True
    while ciclo:
        op = input('Ingrese una opcion: ')
        try:
            op = int(op)
            if op < 1 or op > len(opciones):
                print('Numero invalido')
            else:
                ciclo = False
                return op
        except:
            print('Porfavor ingresar solo numeros')


def menus2(opciones):
    """Crea menú con las opciones dadas por el usario
    en una lista y verifica que esten en el rango especificado"""
    if len(opciones) > 1:
        length = len(opciones)
        for i in range(length):
            print(i+1, ". ", opciones[i])
    else:
        print("1. ", opciones[0])

    ciclo = True
    while ciclo == True:
        op = input('Ingrese una opcion: ')
        try:
            op = int(op)
            if op < 1 or op > len(opciones):
                print('Numero invalido')
            else:
                ciclo = False
                return opciones[op-1]
        except:
            print('Porfavor ingresar solo numeros')


def contra():
    flag = True
    while(flag):
        print("Ingrese su nueva contraseña")
        contra = input()
        if(contra == ""):
            print("No puede meter contraseñas vacías")
        else:
            print("Su contrasña es: ", contra)
            print("Está seguro de que desea que esta sea su contraseña?")
            choice = menus(["Sí", "No"])
            if (choice == 1):
                return contra
                flag = False


def tier(nivel):
    nivel = str(nivel)
    swicth = {
        "[(0,)]": 0,
        "[(1,)]": 1,
        "[(2,)]": 2,
        "[(3,)]": 3
    }
    return swicth[nivel]


def cleanSingle(single):
    single = str(single)
    begin = 0
    end = 0
    acu = 0
    for e in single:
        if e == '(':
            begin = acu + 1
        elif e == ',':
            end = acu
        acu = acu + 1
    return single[begin:end]


def cleanSingle2(single):
    single = str(single)
    begin = -1
    end = 0
    acu = 0
    for e in single:
        if e == "'" and begin < end:
            begin = acu + 1
        elif e == "'":
            end = acu
        acu = acu + 1
    return single[begin:end]


def createID(l):
    _id = uuid.uuid1()
    _id = str(_id)
    return _id[0:l]


def createArray(data):
    arreglo = []
    for e in data:
        arreglo.append(e)
    return arreglo


def menu3(ids, names):
    nombres = createArray(names)
    codigos = createArray(ids)
    op = menus(nombres)
    return codigos[op-1]
