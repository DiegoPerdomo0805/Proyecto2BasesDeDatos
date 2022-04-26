from hashlib import md5
import time

userName = ""
userProfile = ""
userType = ""
adTime = 15

#funcion de encriptado usando md5
def encryption(psswrd):
    cntr = psswrd
    c_e = md5()
    c_e.update(cntr.encode())
    return c_e.digest()

def passlen(psswrd):
    if len(psswrd)>7 and len(psswrd)<50:
        return True
    else:
        return False

#SET GET DE LA INFO DE LA CUENTA
def setSession(user = ""):
    global userName
    userName = user

def getSession():
    return userName

#SET GET DEL TIPO DE CUENTA
def setType(type):
    global userType
    userType = type

def getType():
    return userType

#SET GET DE LA INFO DEL PERFIL
def setProfile(profile = ""):
    global userProfile
    userProfile = profile

def getProfile():
    return userProfile

def range(x, l):
    if x > 0 and x<= l:
        return True
    else:
        return False

      
def setTime(time = 15):
    global adTime
    adTime = time

def getTime():
    return adTime

def menus(opciones):
    """Crea menú con las opciones dadas por el usario
    en una lista y verifica que esten en el rango especificado"""
    for i in range(len(opciones)):
        print(i+1, ". ",opciones[i])
   
    ciclo=True
    while ciclo==True:
        op=input('Ingrese una opcion: ')
        try:
            op=int(op)
            if op <1 or op>len(opciones):
                print('Numero invalido')
            else:
                ciclo=False
                return op
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