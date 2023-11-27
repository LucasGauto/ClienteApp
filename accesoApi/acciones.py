import requests

api_url = 'http://127.0.0.1:8000'

def nuevoLibro(author, title, year, country=None, imageLink=None, language=None, link=None, pages=None):
    # Definir la ruta de la API y el endpoint que deseas llamar
    api_endpoint = "/add"

    # Datos que deseas enviar en la solicitud PUT
    datos_a_enviar = {
	    "author": author,
	    "country": country,        
        "imageLink": imageLink,
        "language": language,
        "link": link,
        "pages": pages,
	    "title": title,
        "year": year
    }

    # Realizar una solicitud HTTP PUT con los datos en el cuerpo
    response = requests.put(f"{api_url}{api_endpoint}", json=datos_a_enviar)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        print(f"Solicitud exitosa. Código de estado: {response.status_code}")
    else:
        # Imprimir un mensaje de error si la solicitud no fue exitosa
        print(f"Error: {response.status_code}, {response.reason}")
        #Devuelve Error: 402, y no se por qué

# Llamada de ejemplo a la función para ver si funciona (no funciona)
#nuevoLibro(author="LucasGausto", title="ElLibro", year=50, country='asdflkjasd', imageLink='asdñflij',
#           language='espanol', link='asdlñjf',pages=50)


