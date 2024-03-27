from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de Chocolates
chocolatess = {}


class cChocolateD:
    def __init__(self, chocolate_type, peso, sabor, relleno):
        self.chocolate_type = chocolate_type
        self.peso = peso
        self.sabor = sabor
        self.relleno = relleno


class tableta(cChocolateD):
    def __init__(self ,peso, sabor, relleno):
        super().__init__("tableta", peso , sabor, None)


class trufas(cChocolateD):
    def __init__(self , peso, sabor, relleno):
        super().__init__("trufas", peso ,sabor, relleno)


class bonbones(cChocolateD):
    def __init__(self,peso, sabor, relleno):
        super().__init__("bonbones",peso, sabor, relleno)



class DeliveryFactory:
    @staticmethod
    def create_chocolate(chocolate_type, peso, sabor, relleno):
        if chocolate_type == "trufas":
            return trufas(peso, sabor, relleno)
        elif chocolate_type == "tableta":
            return tableta(peso ,sabor, None)
        elif chocolate_type == "bonbones":
            return bonbones(peso ,sabor, relleno)
        else:
            raise ValueError("Tipo de Chocolate de entrega no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class DeliveryService:#constructor
    def __init__(self):
        self.factory = DeliveryFactory()

    def add_chocolate(self, data): #gestiona datos de los veiculos, utlizamos un diccionario en el examen 
        chocolate_type = data.get("chocolate_type", None)
        peso =data.get("peso" , None)
        sabor = data.get("sabor", None)
        relleno = data.get("relleno", None)

        delvery_chocolate = self.factory.create_chocolate( #enviamos a la fabrica, lo tenemos en aqui,
            chocolate_type, peso, sabor, relleno
        )
        chocolatess[len(chocolatess) + 1] = delvery_chocolate #todos los veiculos tienen 
        return delvery_chocolate

    def list_chocolatess(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolatess.items()} #

    def update_chocolate(self, chocolate_id, data): #body que me dan en la solicitud 
        if chocolate_id in chocolatess:
            chocolate = chocolatess[chocolate_id] #verificamos si exsiste 
            peso = data.get("peso" , None)
            sabor = data.get("sabor", None)
            relleno = data.get("relleno", None)
            if peso:
                chocolate.relleno = peso
            if sabor: #trutines si un 0 cadena vasia es false---------
                chocolate.sabor = sabor
            if relleno:
                chocolate.relleno = relleno
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id): #en el bulider existe el pop, aqui es otra forma, lo borramos si exisite el id
        if chocolate_id in chocolatess:
            del chocolatess[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None # si no exisiste el id


class DeliveryRequestHandler(BaseHTTPRequestHandler): #lo que no puede camboar es BaseHTTPRequestHandler
    def __init__(self, *args, **kwargs):
        self.delivery_service = DeliveryService() #esto es un servicio de deliberi , viviara aqui
        super().__init__(*args, **kwargs) #args se enivan liosta ed parametros , en lo0s qkwars se ...


    def do_POST(self):  #crea un recurso
        if self.path == "/deliveries":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_chocolate(data) #este llama a la fabrica y crea el veiculo
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/deliveries":
            response_data = self.delivery_service.list_chocolatess() #lista los veiculos
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/deliveries/"): #pregunto si exisite algo, es el id
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_chocolate(chocolate_id, data) #update recibe los veiculos 
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/deliveries/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
