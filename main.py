import conexion

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
   data = (password)
   resultadoQ = conexion.executeQuery(query,data,True)

   if(len(resultadoQ) == 0):
      print("password invalida")
   else:
      perfil()


def perfil():
   print("Que perfil desea seleccionar?")
