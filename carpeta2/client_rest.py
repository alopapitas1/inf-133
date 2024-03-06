import requests


url = "http://localhost:8000/"

ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)


ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", 
                                    url=ruta_eliminar)
print(eliminar_response.text)


ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)
