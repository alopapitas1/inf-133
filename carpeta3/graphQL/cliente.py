import requests

# Definir la consulta GraphQL
query = """
    {
        Goodbye
        hello 
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query}) #query valor y clave en query hay solo una cadena xd
print(response.text)
response = requests.post(url, json={'query': query}) #query valor y clave en query hay solo una cadena xd
print(response.text)
