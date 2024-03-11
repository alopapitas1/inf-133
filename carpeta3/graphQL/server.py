from http.server import HTTPServer, BaseHTTPRequestHandler #http se aloja el server,  bese se encarha de resolver solicitudes get post
import json 
from graphene import ObjectType, String, Int, List, Schema



class Query(ObjectType):
    Goodbye = String()
    hello = String()
    
    def resolve_Goodbye(root, info):
        return "bye bye"
    def resolve_hello(root, info):
        return "menudo asco"


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
        server_address = ("", port) #tupla
        httpd = HTTPServer(server_address, GraphQLRequestHandler) #donde vive el server
        print(f"Iniciando servidor web en http://localhost:{port}/") 
        httpd.serve_forever() #corra todo el tiempo
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server() #ejecuta 
