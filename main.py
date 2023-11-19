#Este será el cliente de nuestro trabajo práctico sobre API's
from usuarios import acciones

#Menu
print("Bienvenido!")

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
    