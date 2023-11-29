#Este será el cliente de nuestro trabajo práctico sobre API's
from usuarios import acciones
import requests
from accesoApi import acciones

#Menu
print("Bienvenido!")
def menu():
    return """
    Qué desea hacer?
    1 - Obtener datos de libros.
    2 - Ingresar un libro.
    3 - Borrar un libro.
    4 - Editar un libro (hacer).
    5 - Salir.
    """

def menuBusqueda():
    return """
        1 - Buscar por autor.
        2 - Buscar por titulo.
        3 - Buscar por idioma.
        4 - Buscar por año.
        5 - Volver.
        """

print(menu())
accion = input(">>: ")

while accion != '5':

    if accion == '1':
        print("""Bien, las opciones de obtención de datos son las siguientes:""")

        print(menuBusqueda())

        opcion = input('>>: ')

        while opcion != '5':
            if opcion == '1':
                author = input("Ingrese el nombre del autor por el que desea buscar: ")

                print("######################################################\n")
                acciones.buscarPorAutor(author=author)
                print("\n#####################################################")
                print(menuBusqueda())
                opcion = input('>>: ')
                continue

            elif opcion == '2':
                title = input("Ingrese el titulo del libro que busca: ")

                print("######################################################\n")
                acciones.buscarPorTitulo(title=title)
                print("\n#####################################################")

                print(menuBusqueda())
                opcion = input('>>: ')
                continue

            elif opcion == '3':
                language = input("Ingrese el idioma de los libros que busca: ")

                print("\n#####################################################\n")
                acciones.buscarPorIdioma(language=language)
                print("\n#####################################################\n")

                print(menuBusqueda())
                opcion = input('>>: ')
                continue

            elif opcion == '4':
                while True:
                    try:
                        year = int(input("Ingrese el año del libro que busca: "))
                        break
                    except ValueError:
                        print("Ingrese un año válido por favor.")

                print("\n#####################################################\n")
                acciones.buscarPorAnio(year=year)
                print("\n#####################################################\n")

                print(menuBusqueda())
                opcion = input('>>: ')
                continue
            else:
                print('Ingrese una opción válida')
                opcion = input(">>: ")
                continue

        if opcion == '5':
            print(menu())
            accion = input(">>: ")
            print("\n")
            continue

    elif accion == '2':
        print("Bien. A continuación le pediremos que ignrese la información del libro a ingresar: ")
        autor = input("Nombre del autor: ")
        titulo = input("Titulo: ")

        while True: #verifica que sea numero
            try:
                anio = int(input("Año en que se escribió: "))
                break
            except ValueError:
                print("Ingrese un numero por favor.")

        pais = input("¿En que pais?: ")
        linkImagen = input("Ingresa un link de imagen: ")
        idioma=input("En qué idioma fue escrito?: ")
        link=input("Ingresa el link donde encontrar el libro: ")

        while True: #verifica que sea numero
            try:
                paginas= int(input("Cuantas paginas tiene?: "))
                break
            except ValueError:
                print("Ingrese un numero por favor.")

        acciones.nuevoLibro(autor,titulo,anio,pais,linkImagen,idioma,link,paginas)

        print(menu())
        accion = input(">>: ")
        continue

    elif accion == '3':
        accion = input("Cuál es el titulo del libro que desea eliminar?: ")
        acciones.eliminarLibro(accion)
        print(menu())
        accion = input(">>: ")
        continue

    elif accion == '4':
        print("Bien, actualicemos un libro.")

    else:
        print("Ingrese una opción válida.")
        accion = input(">>: ")
        continue

print("Nos vemos!")