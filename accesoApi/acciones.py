import requests

api_url = 'http://127.0.0.1:8000'

def nuevoLibro(author, title, year, country, imageLink, language, link, pages): #El put no anda

    # Datos que deseas enviar en la solicitud PUT
    datos_a_enviar = {
	    "author": author,
        "title": title,
        "year": year,
	    "country": country,        
        "imageLink": imageLink,
        "language": language,
        "link": link,
        "pages": pages

    }

    # Realizar una solicitud HTTP PUT con los datos en el cuerpo
    response = requests.put(api_url+"/add", params=datos_a_enviar)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        print(f"Solicitud exitosa. Código de estado: {response.status_code}")
    else:
        # Imprimir un mensaje de error si la solicitud no fue exitosa
        print(f"Error: {response.status_code}, {response.reason}")
        #Devuelve Error: 402, y no se por qué

def buscarPorAutor(author: str): #esto funciona
    #captar los espacios en el main!!
    parametros = {'nombreAutor':author}
    response = requests.get(api_url+"/searchAuthor", params=parametros)
    for libro in response.json():
        print(libro)

def buscarPorTitulo(title:str): #Funciona, capturar errores
    parametros = {'titulo':title}
    response = requests.get(api_url+"/searchTitle", params=parametros)
    for libro in response.json():
        print(libro)

def buscarPorIdioma(language:str):#Funciona, capturar errores
    #Mostrar una lista de los idiomas elegibles
    parametros={'idioma':language}
    response = requests.get(api_url+"/searchLanguage", params=parametros)
    for libro in response.json():
        print(libro)

def buscarPorAnio(year:int): #funciona, capturar errores
    parametros = {'anio':year}
    response = requests.get(api_url+"/searchYear", params=parametros)
    for libro in response.json():
        print(libro)

def eliminarLibro(title:str): #Funciona
    parametros ={'titulo':title}
    response = requests.delete(api_url+"/delete", params=parametros)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        print("La eliminación fue exitosa.")
    else:
        print("Error en la solicitud:", response.status_code, response.text)

def misLibros(): #Funciona
    response = requests.get(api_url + "/json")
    for libro in response.json():
        print('------------------------')
        for campo, dato in libro.items():
            print(campo,": ",dato)
        print("\n")

nuevoLibro("Lucas","LibrodeLucas",2023,"Argentina","link","Español","link2",5)