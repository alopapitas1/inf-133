import requests

# URL del servidor Flask
url = 'http://localhost:5000/'

print("1--------------------------------------------------")
# Realizar una solicitud GET al servidor Flask
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)





# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
print("2---------------------------------------------------")

params = {'nombre': 'Alain'}
response = requests.get(url+'saludar', params=params)

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
    
    
    
    

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
print("3---------------------------------------------------")

params = {'num1': '1', 'num2':'2'}
response = requests.get(url+'sumar', params=params)

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
    
    
    

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
print("4---------------------------------------------------")

params = {'cadena':'reconocer'}
response = requests.get(url+'palindromo', params=params)

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
    
    


