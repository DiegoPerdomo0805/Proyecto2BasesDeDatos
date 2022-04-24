import conexion, busqueda

def main():
   print("BIENVENIDO A YOUTUBE NARANJA 2.0")

   while(True):

      print("1. Iniciar seccion \n2.Crear cuenta")

      userData = input()

      try:
         userDataInt = int(userData)
         if(userData == 1):
            print("INICIAR SECCION")
            logIn()

         elif(userData == 2):
            print("CREAR CUENTA")

         else:
            print("El valor debe ser una de las opciones dadas")

      except:
         print("El valor debe ser una de las opciones dadas")

def logIn():

   print("Ingrese el email de su usuario")
   email = input()

   query = ("select * from cuenta where correo=%s;")
   data = (email)
   resultadoQ = conexion.executeQuery(query,data,True)

   if(len(resultadoQ) == 0):
      print("correo invalido")
      main()

   print("Ingrese la contrasena del usuario")
   password = input()

   query = ("select * from cuenta where pssword=%s;")
   data = (password,)
   resultadoQ = conexion.executeQuery(query,data,True)

   if(len(resultadoQ) == 0):
      print("password invalida")
   else:
      perfil()


def perfil():
   print("Que perfil desea seleccionar?")

   #MOMO: aqui es de poner una forma de acceder a los diferentes perfiles que posee el usuario

   menu()

def menu():
   #AQUI HACER UN IF ELSE PARA SABER SI ES O NO UN ADMIN
   admin = False

   if(admin == True):
      print("Admin")
   else:
      
      while(True):

         print("Eliga una opcion")
         print("1. Busqueda \n2. Ver favoritos \n3. Eliminar un contenido de favoritos \n4. Contenido con progreso \n5. Contenido finalizado \n6. Sugerencias \n 7. Seleccionar otro perfil \n8. Cerrar sesión")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userData == 1):
               print("Busqueda")

            elif(userData == 2):
               print("Ver favoritos")

            elif(userData == 3):
               print("Eliminar un contenido de favoritos")

            elif(userData == 4):
               print("Contenido con progreso")

            elif(userData == 5):
               print("Contenido finalizado")

            elif(userData == 6):
               print("Sugerencias")

            elif(userData == 7):
               print("Seleccionar otro perfil")

            elif(userData == 8):
               print("Cerrar sesión")

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")
