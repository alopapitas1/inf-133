# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)


# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"





# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})



#sumar
@app.route("/sumar", methods=["GET"])
def sumar():
    # Obtener el nombre de los argumentos de la URL.
    num1=request.args.get("num1")
    num2=request.args.get("num2")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not num1 and num2:
        return (
            jsonify({"error": "Se requiere datos para sumar."}),400,)
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    dat1=int(num1)
    dat2=int(num2)
    res=dat1+dat2
    return jsonify({"mensaje": f"la suma es, {res}!"})




#palindromo
@app.route("/palindromo", methods=["GET"])
def verificar():
    # Obtener el nombre de los argumentos de la URL.
    palabra=request.args.get("cadena")

    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not palabra:
        return (
            jsonify({"error": "Se requiere datos para verificar."}),400,)
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    
    palabra1=palabra
    cadena1=list(palabra)
    cadena2=list(palabra1)
    cadena2.reverse()

    if cadena1==cadena2:    
        return jsonify({"mensaje": f"es palindromo 1{cadena1} 2{cadena2}"})
    else:
        return jsonify({"mensaje": f"NO es palindromo 1{cadena1} 2{cadena2}"})




# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":
    app.run()
