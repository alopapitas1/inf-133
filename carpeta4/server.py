from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field


class Estudiante(ObjectType):    
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()


class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id = Field(Estudiante, id=Int())
    estudiante_nom_ape= Field(Estudiante,nombre=String(),apellido=String())
    estudiante_carrera= Field(Estudiante,carrera=String())

    def resolve_estudiantes(root, info):
        print(estudiantes)
        return estudiantes

    def resolve_estudiante_por_id(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None
    
    def resolve_estudiante_carrera(root, info, carrera):
        for estudiante in estudiantes:
            if estudiante.carrera == carrera:
                return estudiante
        return None
    
    def resolve_estudiante_nom_ape(root,info,nombre,apellido):
        for estudiante in estudiantes:
            if estudiante.nombre== nombre:
                if estudiante.apellido ==apellido:
                    return estudiante
        return None

estudiantes = [
    Estudiante( #instancia de estudiantes
        id=1, nombre="Pedrito", apellido="García", carrera="Ingeniería de Sistemas"
    ),
    Estudiante(id=2, nombre="Jose", apellido="Lopez", carrera="Arquitectura"),
]

schema = Schema(query=Query)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
