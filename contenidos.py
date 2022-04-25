import main, utilities

def contenidos():
    while(True):

        print("Busqueda por:")
        print("1. Agregar contenido\n2. Modificar contenido\n3. Eliminar contenido\n4. Mostrar contenido actual\n5. Regresar")

        userData = input()

        try:

            userDataInt = int(userData)
            if(userDataInt == 1):
                agregar()

            elif(userDataInt == 2):
                modificar()

            elif(userDataInt == 3):
                eliminar()

            elif(userDataInt == 4):
                mostrar()

            elif(userDataInt == 5):
                main.menu()

            else:
                print("El valor debe ser una de las opciones dadas")

        except:
            print("El valor debe ser una de las opciones dadas")

def agregar():
    print("AGREGAR PERSONAJES:")

    print("Nombre del contenido")
    nombre = input()

    print("Nombre del director")
    director = input()

    print("Fecha de estreno (DAY-MOUNTH-YEAR)")
    fecha = input()

    print("Link del contenido")
    link = input()

    print("Categoria del contenido")
    categoria = input()

    # sql = ("insert into contenido (nombre, director, fecha_estreno, link, categoria) values (%s, %s, %s,%s,%s)")
    # args = (name, director, date, link, category)
    # databaseModule.executeQuery(sql, args) 

    # sql = ("SELECT id_contenido from contenido where nombre = %s;")
    # args = (name,)
    # results = databaseModule.executeQuery(sql, args, True) 
    # id = results[0]

    terminar = True

    while(terminar == True):
        print("Agregue un genero ")

def modificar():
    print("modificar")

def eliminar():
    print("eliminar")

def mostrar():
    print("mostrar")
