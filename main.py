from ctypes import util
from sympy import true
import conexion, busqueda, fav, utilities, extra, contenidos, estadisticas, uuid
from datetime import datetime

def main():
       
   print("BIENVENIDO A YOUTUBE NARANJA 2.0")
   #65d443ea-Gimli
   utilities.setProfile('-')
   utilities.setSession("-")
   utilities.setType("-")

   #query = ("SELECT p.perfil from perfiles p where p.cuenta = %s;")
   #data = ("16", )
   #resultadoQ = conexion.executeQuery(query,data,True)
   #nombres = resultadoQ
   #query = ("SELECT p.perfil_id from perfiles p where p.cuenta = %s;")
   #data = ("16", )
   #resultadoQ = conexion.executeQuery(query,data,True)
   #ids = resultadoQ
   #utilities.setProfile(utilities.cleanSingle(utilities.menu3(ids, nombres)))

   while(True):

      print("1. Iniciar seccion \n2.Crear cuenta")

      userData = input()

      try:
         userDataInt = int(userData)
         if(userDataInt == 1):
            logIn()

         elif(userDataInt == 2):
            SignIn()

         else:
            print("El valor debe ser una de las opciones dadas")

      except:
         print("El valor debe ser una de las opciones dadas")

def logIn():
   print("Ingrese el email de su usuario")
   email = input()

   query = ("SELECT * from cuenta where correo=%s;")
   data = (email,)
   resultadoQ = conexion.executeQuery(query,data,True)

   if(len(resultadoQ) == 0):
      print("correo invalido")
      main()
   else:
      print("Ingrese la contrasena del usuario")
      password = input()

      query = ("SELECT * from cuenta where pssword=%s and correo=%s;")
      data = (utilities.encryption(password), email)
      resultadoQ = conexion.executeQuery(query,data,True)

      if(len(resultadoQ) == 0):
         print("password invalida")
      else:
         query = ("SELECT nivel_cuenta from cuenta where correo=%s;")
         data = (email,)
         resultadoQ = conexion.executeQuery(query,data,True)
         #MOMO: aqui vamos a colocar el tipo de cuenta que es asi para tener el dato en utilities, ademas de datos de la cuenta que no sean utiles a futuro

         tier = utilities.tier(resultadoQ)
         utilities.setType(tier)

         query = ("SELECT cuenta_id from cuenta where correo=%s;")
         data = (email,)
         resultadoQ = conexion.executeQuery(query,data,True)
         utilities.setSession(utilities.cleanSingle(resultadoQ))
         cuenta_id = utilities.getSession()
         
         query = ("SELECT count(perfil_id) from perfiles p where p.active and p.cuenta =%s;")
         data = (cuenta_id,)
         resultadoQ = conexion.executeQuery(query, data, True)
         
         perfiles = int(utilities.cleanSingle(resultadoQ))
         utilities.setProfiles(perfiles)
         print(utilities.getProfiles())
         perfil()
         
         

def SignIn(): 
   print("Ingrese el email de su usuario")
   email = input()

   query = ("SELECT * from cuenta where correo=%s;")
   data = (email,)
   resultadoQ = conexion.executeQuery(query,data,True)

   if(len(resultadoQ) >= 0):
      print("correo invalido")
      SignIn()
   else:
          opciones = ["Básica","Estándar", "Premium"]
          tier = utilities.menus(opciones)
          psswrd = utilities.contra()
          sql = ("INSERT INTO cuenta (nivel_cuenta, pssword , correo) VALUES (%d, %s, %s);")
          args = (tier, psswrd, email, )#RECORDA SIEMPRE PONER LA COMA PARA QUE NO TRUENE
          results = conexion.executeQuery(sql, args, True) 
          print("\nCree su perfil principal")
          name = ""
          flag = True
          
          while(flag):
                 print("Ingrese el nombre de su perfil")
                 name = input()
                 if(name == ""):
                     print("No puede meter nombres vacíos")
                 else:
                     print("Su nombre es: ", name)
                     print("Está seguro de que desea que esta sea su nombre?")
                     choice = utilities.menus(["Sí", "No"])
                     if (choice == 1):
                            flag = False
         
                            
          
def createProfile():
   unready = True
   while(unready):
      print("Ingrese el nombre para su perfil")
      name = input()
      if (name.__len__() <= 10) and (name.__len__() > 0):
         perfil_id = utilities.createID(8)
         account = utilities.getSession()
         query = ("INSERT INTO perfiles (cuenta, perfil, active, perfil_id) VALUES (%s,%s,'True',%s);")
         data = (account, name, perfil_id, )
         conexion.executeQuery(query,data,True)
         unready = False
      else:
         print("El nombre del perfil no debe pasar de los 10 caracteres.\n")


         
             






def perfil():
   if(utilities.getProfiles() == 0):
       print("Debe crear un perfil")
       createProfile()
   else:
       print("Que perfil desea seleccionar?")
       query = ("SELECT p.perfil from perfiles p where p.cuenta = %s;")
       data = (utilities.getSession(), )
       resultadoQ = conexion.executeQuery(query,data,True)
       nombres = resultadoQ
       query = ("SELECT p.perfil_id from perfiles p where p.cuenta = %s;")
       data = (utilities.getSession(), )
       resultadoQ = conexion.executeQuery(query,data,True)
       ids = resultadoQ
       utilities.setProfile(utilities.cleanSingle2(utilities.menu3(ids, nombres)))
   menu()    

def menu():
   #AQUI HACER UN IF ELSE PARA SABER SI ES O NO UN ADMIN
   if(utilities.getType == "0"):

      while(True):

         print("Eliga una opcion")
         print("1. Estadísticas \n2. Modificacion de contenidos \n3. Modificar usuario \n4. Modificar anunciantes \n5. Cerrar sesión")
            
         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
               estadisticas.estadisticas()

            elif(userDataInt == 2):
               contenidos.contenidos()

            elif(userDataInt == 3):
               fav.quitar()

            elif(userDataInt == 4):
               extra.prog()

            elif(userDataInt == 5):
               main()

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")


   else:
      
      while(True):

         print("Eliga una opcion")
         print("1. Busqueda \n2. Ver favoritos \n3. Eliminar un contenido de favoritos \n4. Contenido con progreso \n5. Contenido finalizado \n6. Sugerencias \n 7. Seleccionar otro perfil \n8. Cerrar sesión")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
               print("Busqueda")
               busqueda.busqueda()

            elif(userDataInt == 2):
               print("Ver favoritos")
               fav.favoritos()

            elif(userDataInt == 3):
               print("Eliminar un contenido de favoritos")
               fav.quitar()

            elif(userDataInt == 4):
               print("Contenido con progreso")
               extra.prog()

            elif(userDataInt == 5):
               print("Contenido finalizado")
               extra.finalizado()

            elif(userDataInt == 6):
               print("Sugerencias")
               extra.sugerencia()

            elif(userDataInt == 7):
               print("Seleccionar otro perfil")
               perfil()

            elif(userDataInt == 8):
               print("Cerrar sesión")
               main()

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")

main()
