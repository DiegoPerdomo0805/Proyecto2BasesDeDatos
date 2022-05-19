import pywhatkit
import time
from datetime import date
import threading

import conexion
import utilities


def player(id):
    while(True):

        print("1. Ver \n2. Agregar a favoritos \n3. Regresar")

        userData = input()

        try:
            userDataInt = int(userData)
            perfil = utilities.getProfile()
            if(userDataInt == 1):
                videoPlayer(id)

            elif(userDataInt == 2):

                query = ("insert into favoritos (perfil, id_titulo) values (%s, %s);")
                data = (perfil, id,)
                conexion.executeQuery(query, data, False)

                break

            elif(userDataInt == 3):
                break

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")


def videoPlayer(id):

    # MOMO: Esto de aqui es para venir agarrar el link y ponerlo en el player
    # query = ("select * from titulos where id=%s;")
    # data = (id,)
    # resultadoQ = conexion.executeQuery(query,data,True)

    link = 'https: // youtu.be/moJiZb_48kY'

    pywhatkit.playonyt(link)
    pywhatkit.playonyt()

    while(True):

        #anuncio()

        print("Termino el contenido? \n1. Yes \n2. No")

        userData = input()

        try:
            userDataInt = int(userData)
            dateToday = date.today()

            perfil = utilities.getProfiles
            if(userDataInt == 1):
                print("SI")
                query = (
                    "SELECT wa.times_watched from watch_again wa where perfil = %s and id_titulo = %s")
                data = (perfil, id,)
                resultadoQ = conexion.executeQuery(query, data, True)

                num = resultadoQ.__len__

                if(resultadoQ >= 0):
                    query = (
                        "UPDATE watch_again set times_watched = %s where  perfil = %s and id_titulo = %s")
                    data = (num, perfil, id,)
                    resultadoQ = conexion.executeQuery(query, data, True)
                    query = (
                        "UPDATE watch_again set date_watched = %s where  perfil = %s and id_titulo = %s")
                    data = (num, perfil, id,)
                    resultadoQ = conexion.executeQuery(query, data, True)
                    query = (
                        "DELETE from viendo  where perfil = %s and id_titulo = %s")
                    data = (perfil, id,)
                    resultadoQ = conexion.executeQuery(query, data, True)

                else:
                    query = (
                        "INSERT INTO watch_again (perfil, id_titulo, times_watched, date_watched) values (%s, %s, 1, %s)")
                    data = (perfil, id, num, dateToday)
                    resultadoQ = conexion.executeQuery(query, data, True)

            elif(userDataInt == 2):
                print("NO")
                query = ("INSERT INTO viendo (perfil, id_titulo) values (%s, %s);")
                data = (perfil, id,)
                resultadoQ = conexion.executeQuery(query, data, True)

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")


# def anuncio(ad):
#    now = time.time()
#    future = now + 15
#    while time.time() < future:
#        # do stuff
#        print("--------------------ANUNCIO--------------------")
#        pass

def anuncio():
    threading.Timer(15.0, anuncio).start()
    print(anuncio)
