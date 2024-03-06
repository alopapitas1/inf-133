import requests

url = "http://localhost:8000/"

ruta_get = url + "estudiantes"
print("ENTRO AL GET")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


# ruta_post = url + "estudiantes"
# print("ENTRO AL POST")
# nuevo_estudiante ={
#         "id": 5,
#         "nombre": "Pedrito",
#         "apellido": "García",
#         "carrera": "Ingenieria de Sistemas",
#     }
# post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
# print(post_response.text)


# ruta_filtrar_nombre = url + "estudiantes/1"
# print("ENTRO AL GET con id")
# filtrar_nombre_response = requests.request(method="GET", url=ruta_filtrar_nombre)
# print(filtrar_nombre_response.text)



# ruta_actualizar = url + "estudiantes"
# print("ENTRO AL PUT")
# estudiante_actualizado = {
#     "id": 1,
#     "nombre": "Juan",
#     "apellido": "Pérez",
#     "carrera": "Ingeniería Agronomica",
# }
# put_response = requests.request(method="PUT", url=ruta_actualizar, json=estudiante_actualizado)
# print(put_response.text)



# ruta_eliminar=url+"estudiantes"
# print("estudiantes eliminados")
# delete_response=requests.request(method="DELETE", url=ruta_eliminar)
# print(delete_response.text)
