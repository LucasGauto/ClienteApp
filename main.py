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
        elif accion == '2':
            title = input("Ingrese el titulo del libro que busca: ")
        elif accion == '3':
            laguage = input("Ingrese el idioma de los libros que busca: ")
        elif accion == '4':
            year = int(input("Ingrese el año del libro que busca: "))
        elif accion == '5':
            print(menu())
            accion = input(">>: ")
            continue
        else:
            print('Ingrese una opción válida')
            accion = input(">>: ")


    elif accion == '2':
        print("Bien. A continuación le pediremos que ignrese la información del libro a ingresar: ")
        author = input("Nombre del autor: ")
        title = input("Titulo: ")
        year = int(input("Año en que se escribió: "))

        #Accedo al modulo accesoApi, y ejecuto la funcion nuevoLibro
        acciones.nuevoLibro(author, title, year) #Pruebo con solo 3 campos porque los demás están seteados como None en la API como default

        print(menu())
        accion = input(">>: ")
        continue

    elif accion == '3':
        accion = input("Cuál es el titulo del libro que desea eliminar?: ")

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