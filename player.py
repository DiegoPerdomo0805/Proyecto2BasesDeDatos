import conexion
import pywhatkit

def player(id):
    while(True):

         print("1. Ver \n2. Agregar a favoritos \n3. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                videoPlayer(id)

            elif(userDataInt == 2):
                # MOMO: QUERY PARA AGREGAR EL CONTENIDO A FAVORITOS
                # query = ("select * from titulos where id=%s;")
                # data = (id,)
                # resultadoQ = conexion.executeQuery(query,data,True)

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

    # pywhatkit.playonyt(link)

    while(True):
         print("Termino el contenido? \n1. Yes \n2. No")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                print("SI")
                # MOMO: PARA PONER SI EL USUARIO REALMENTE TERMINO EL CONTENIDO O NO
                # query = ("select * from titulos where id=%s;")
                # data = (id,)
                # resultadoQ = conexion.executeQuery(query,data,True)

            elif(userDataInt == 2):
                print("NO")
                # MOMO: PARA PONER SI EL USUARIO REALMENTE TERMINO EL CONTENIDO O NO
                # query = ("select * from titulos where id=%s;")
                # data = (id,)
                # resultadoQ = conexion.executeQuery(query,data,True)

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")
    

    