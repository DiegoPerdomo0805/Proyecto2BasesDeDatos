import main, utilities, conexion

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
    print("AGREGAR CONTENIDOS:")

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
    # conexion.executeQuery(sql, args) 

    # sql = ("SELECT id_contenido from contenido where nombre = %s;")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 
    # id = results[0]

    terminar = True

    while(terminar == True):
        print("Agregue un genero ")
        genero = input()
        # sql = ("INSERT INTO generos values (%s,%s);")
        # args = (categoria,id)
        # conexion.executeQuery(sql, args) 

        print("Quiere agrgar otro genero? \n1. Si \n2. No")
        seguir = input()
        if(seguir == '1'):
            terminar = True
        elif(seguir == '2'):
            terminar = False
        else:
            print("Debe seleccionar una de las posibles respuestas")

    while(terminar == True):

        print("Agregue un premio? \n1. Si \n2. No")
        seguir = input()

        if(seguir == '1'):
            terminar = True
            # sql = ("INSERT INTO premios values (%s,%s);")
            # args = (premio,id)
            # databaseModule.executeQuery(sql, args) 
        elif(seguir == '2'):
            terminar = False
        else:
            print("Debe seleccionar una de las posibles respuestas")


def modificar():
    print("MODIFICAR CONTENIDOS:")

    print("Nombre del contenido para modificar")
    nombre = input()

    # sql = ("SELECT id_contenido from contenido where nombre = %s;")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 

    print("Nombre nuevo del contenido")
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
    # conexion.executeQuery(sql, args) 

    # sql = ("SELECT id_contenido from contenido where nombre = %s;")
    # args = (name,)
    # results = conexion.executeQuery(sql, args, True) 
    # id = results[0]

    terminar = True

    while(terminar == True):
        print("Agregue un genero ")
        genero = input()
        # sql = ("INSERT INTO generos values (%s,%s);")
        # args = (categoria,id)
        # conexion.executeQuery(sql, args) 

        print("Quiere agrgar otro genero? \n1. Si \n2. No")
        seguir = input()
        if(seguir == '1'):
            terminar = True
        elif(seguir == '2'):
            terminar = False
        else:
            print("Debe seleccionar una de las posibles respuestas")

    while(terminar == True):

        print("Agregue un premio? \n1. Si \n2. No")
        seguir = input()

        if(seguir == '1'):
            terminar = True
            # sql = ("INSERT INTO premios values (%s,%s);")
            # args = (premio,id)
            # databaseModule.executeQuery(sql, args) 
        elif(seguir == '2'):
            terminar = False
        else:
            print("Debe seleccionar una de las posibles respuestas")

def eliminar():
    print("Ingrese el nombre del contenido a eliminar")

    userData = input()

    # sql = ("SELECT id_contenido from contenido where nombre = %s;")
    # args = (name,)
    # results = databaseModule.executeQuery(sql, args, True) 
    # id = results[0]

    # if(len(results) == 0):
    #     print("\n\tNo se encontro contenido con ese nombre. Verifique que este escrito correctamente")
    # else:
    #     sql = ("delete from contenido where id_contenido = %s;")
    #     args = (id,)
    #     databaseModule.executeQuery(sql, args) 

    #     sql = ("delete from generos where id_contenido = %s;")
    #     args = (id,)
    #     databaseModule.executeQuery(sql, args)

    #     sql = ("delete from premios where id_contenido = %s;")
    #     args = (id,)
    #     databaseModule.executeQuery(sql, args)

    #     print("Contenido removido exitosamente")

def mostrar():
    print("mostrar contenido")
    # sql = ("SELECT * from contenido;")
    # results = databaseModule.executeQuery(sql, (), True) 

    # content = []
    # for item in results:
    #     contentTemp = []
    #     contentTemp.append(str(item[1]))
    #     contentTemp.append(str(item[2]))
    #     contentTemp.append(str(item[3]))
    #     contentTemp.append(str(item[4]))
    #     contentTemp.append(str(item[5]))
    #     content.append(contentTemp)

    # print(tabulate(content, headers=['Nombre', 'Director','Fecha Estreno','Link','Categoria']))

