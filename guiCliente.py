from tkinter import *
#Importar customtkinter
import customtkinter
from accesoApi import acciones

#Colores por defecto!!
customtkinter.set_default_color_theme("green")

#Funciones
def mostrarOpcionesBusqueda():
    #Limpiar ventana
    for widget in root.winfo_children():
        widget.destroy()

    #Crear botones busqueda
    searchAuthor = customtkinter.CTkButton(master=root, text="Buscar por autor", command=buscarPorAutor)
    searchTitle = customtkinter.CTkButton(master=root, text="Buscar por titulo")
    searchLanguage = customtkinter.CTkButton(master=root, text="Buscar por idioma")
    searchYear = customtkinter.CTkButton(master=root, text="Buscar por año")
    back = customtkinter.CTkButton(master=root, text="Volver", command=crearVentanaPrincipal)

    #Colocar los botones o widgets
    searchAuthor.place(relx=0.5, rely=0.3, anchor = CENTER)
    searchTitle.place(relx=0.5, rely=0.4, anchor = CENTER)
    searchLanguage.place(relx=0.5, rely=0.5, anchor = CENTER)
    searchYear.place(relx=0.5, rely=0.6, anchor = CENTER)
    back.place(relx=0.5, rely=0.7, anchor = CENTER)

def buscarPorAutor():
    #Limpiar ventana
    for widget in root.winfo_children():
        widget.destroy()

    #input dialog
    def ingresarNombre():
        dialog = customtkinter.CTkInputDialog(text="Ingrese un autor: ", title="Busqueda por autor")
        global autor
        autor = dialog.get_input()
        
        ventanaEmergente = customtkinter.CTkToplevel(root)
        texto = str(acciones.buscarPorAutor(autor))s
        respuesta = customtkinter.CTkLabel(master=ventanaEmergente, text=texto)
        respuesta.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    ingresarAutor = customtkinter.CTkButton(master = root, text="Presionar para ingresar un autor", command=ingresarNombre)
    ingresarAutor.place(relx=0.5, rely=0.5, anchor=CENTER)

def crearVentanaPrincipal():
    #Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    #Setear los botones
    #Crear un button widget
    #mybutton=Button(root, text="HolaMundo", font=("Inter",14)) TK
    searchBook = customtkinter.CTkButton(master=root, text="Buscar libro", command=mostrarOpcionesBusqueda)
    addBook = customtkinter.CTkButton(master=root, text="Añadir un libro")
    deleteBook = customtkinter.CTkButton(master=root, text="Eliminar un libro")
    editBook = customtkinter.CTkButton(master=root, text="Editar un libro")

    #mostrar en el centro de la pantalla
    searchBook.place(relx=0.5, rely=0.4, anchor = CENTER)
    addBook.place(relx=0.5, rely=0.5, anchor=CENTER)
    deleteBook.place(relx=0.5, rely=0.6, anchor=CENTER)
    editBook.place(relx=0.5, rely=0.7, anchor = CENTER)

#Crear la ventana de la app
#root = Tk() con tkinter
root = customtkinter.CTk() #con CTk

#Setear el tamaño
root.geometry('300x400')

crearVentanaPrincipal()

#Correr la app
root.mainloop()