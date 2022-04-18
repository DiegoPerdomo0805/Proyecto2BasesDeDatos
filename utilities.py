from hashlib import md5

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

