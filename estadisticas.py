def estadisticas():
    while(True):

         print("Busqueda por:")
         print("1. El top 10 de géneros de contenido más visto, y los minutos consumidos \n2. Cantidad de reproducciones por cada categoría, por tipo de cuenta \n3. El top 10 de los directores y actores principales de las películas que los perfiles estándar y avanzados han visto \n4. La cantidad de cuentas avanzadas que se han creado en los últimos 6 meses \n5. Para una fecha específica, ¿cuál es la hora pico donde el servicio es más utilizado? \n6. Regresar")

         userData = input()

         try:
            userDataInt = int(userData)
            if(userDataInt == 1):
                nombre()

            elif(userDataInt == 2):
               director()

            elif(userDataInt == 3):
               stelar()

            elif(userDataInt == 4):
               genero()

            elif(userDataInt == 5):
               categoria()

            elif(userDataInt == 6):
               main.menu()

            else:
               print("El valor debe ser una de las opciones dadas")

         except:
            print("El valor debe ser una de las opciones dadas")