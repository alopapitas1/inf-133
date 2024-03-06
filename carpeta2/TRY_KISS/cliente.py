from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Pérez",
        "carrera": "Ingeniería Agronomica"
    },
    {
        "id": 2,
        "nombre": "Alain ",
        "apellido": "Huanca",
        "carrera": "Informatico"
    },
    
    {
        "id": 3,
        "nombre": "Carlos",
        "apellido": "Reyes",
        "carrera": "Exorcista",
    },
    {
        "id": 4,
        "nombre": "Isaac",
        "apellido": "Lampe",
        "carrera": "Doctor",
    },
    {
        "id": 5,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingenieria de Sistemas",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    
    def handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def find_estudent(self,id):
        return  next((estudiante for estudiante in estudiantes if estudiante["id"] == id),None,)
    
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    
    
    
    def do_GET(self):
        if self.path == "/estudiantes":
            self.handler(200,estudiantes)
            
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_estudent(id)
            if estudiante:
                self.handler(200,estudiante)
        else:
            self.handler(404,{"Error":"Ruta no existente"})

    def do_POST(self):
        if self.path == "/estudiantes":
            data=self.read_data()
            data["id"] = len(estudiantes) + 1
            estudiantes.append(data)
            self.handler(201,estudiantes)

        else:
            self.handler(404,{"Error":"Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/estudiantes"):
            data=self.read_data()
            id = data["id"]
            estudiante = self.find_estudent(id)
            if estudiante:
                estudiante.update(data)
                self.handler(200,estudiante)
        else:
            self.handler(404,{"Error":"Ruta no existente"})

    def do_DELETE(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.handler(404,{"Error":"Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
