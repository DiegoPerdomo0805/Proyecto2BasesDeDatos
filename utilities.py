from hashlib import md5

userName = ""
userProfile = ""
userType = ""

#funcion de encriptado usando md5
def encryption(psswrd) -> String:
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

