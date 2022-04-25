def estadisticas():
    while(True):

         print("Busqueda por:")
         print("1. Nombre \n2. Director \n3. Stelar \n4. Genero \n5. Categoria \n6. Estreno \n 7. Premios \n8. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userData == 1):
                nombre()

            elif(userData == 2):
               director()

            elif(userData == 3):
               stelar()

            elif(userData == 4):
               genero()

            elif(userData == 5):
               categoria()

            elif(userData == 6):
               main.menu()

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")