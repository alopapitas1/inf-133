from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def sumar(a,b):
    return f'{a} + {b} = {(a+b)}'

def palindromo(pal):
    pal=pal.replace(" ", "").lower()
    if (pal==pal[::-1]):
        return True
    else:
        return False

dispatcher=SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo":str},
    args={"nombre":str},
)

dispatcher.register_function(
    "Sumar",
    suma_dos_numeros,
    returns={"suma_dos_numeros":str},
    args={"a":int,"b":int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    pal,
    returns={"pal":bool},
    args={"pal":str},
)

server=HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher=dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
