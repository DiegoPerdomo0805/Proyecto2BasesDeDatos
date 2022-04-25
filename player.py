def player():
    while(True):

         print("Busqueda por:")
         print("1. Ver lista \n2. Ver contenido \n3. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userData == 1):
                verL()

            elif(userData == 2):
               ver()

            elif(userData == 3):
               main.menu

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")