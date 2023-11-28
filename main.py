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
print(menu())
accion = input(">>: ")

while accion != '5':
    
    if accion == '1':
        print("""Bien, las opciones de obtención de datos son las siguientes:
            1 - Buscar por autor.
            2 - Buscar por titulo.
            3 - Buscar por idioma.
            4 - Buscar por año.
            5 - Volver.
            """)
        accion = input('>>: ')

        if accion == '1':
            author = input("Ingrese el nombre del autor por el que desea buscar: ")
            acciones.buscarPorAutor(autor=author)

        elif accion == '2':
            title = input("Ingrese el titulo del libro que busca: ")
            acciones.buscarPorTitulo(title=title)

        elif accion == '3':
            language = input("Ingrese el idioma de los libros que busca: ")
            acciones.buscarPorIdioma(language=language)

        elif accion == '4':
            year = int(input("Ingrese el año del libro que busca: "))
            acciones.buscarPorAnio(year=year)

        elif accion == '5':
            print(menu())
            accion = input(">>: ")
            continue
        else:
            print('Ingrese una opción válida')
            accion = input(">>: ")


    elif accion == '2':
        print("Bien. A continuación le pediremos que ignrese la información del libro a ingresar: ")
        autor = input("Nombre del autor: ")
        titulo = input("Titulo: ")
        anio = int(input("Año en que se escribió: "))
        pais = input("¿En que pais?: ")
        linkImagen = input("Ingresa un link de imagen: ")
        idioma=input("En qué idioma fue escrito?: ")
        link=input("Ingresa el link donde encontrar el libro: ")
        paginas= int(input("Cuantas paginas tiene?: "))
        #Accedo al modulo accesoApi, y ejecuto la funcion nuevoLibro
        acciones.nuevoLibro(autor,titulo,anio,pais,linkImagen,idioma,link,paginas) #Pruebo con solo 3 campos porque los demás están seteados como None en la API como default

        print(menu())
        accion = input(">>: ")
        continue

    elif accion == '3':
        accion = input("Cuál es el titulo del libro que desea eliminar?: ")
        acciones.eliminarLibro(accion)

    elif accion == '4':
        print("Bien, actualicemos un libro.")

    else:
        print("Ingrese una opción válida.")
        accion = input(">>: ")
'''
print("""
Qué desea hacer?
    1 - Crear un usuario
    2 - Ingresar

""")

hacer = acciones.Acciones()
accion = input(">>: ")

if accion == "1":
    hacer.registro()
elif accion == "2":
    hacer.login()
else:
    print("Ingrese una opción válida.")
'''