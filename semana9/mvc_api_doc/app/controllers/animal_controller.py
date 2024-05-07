from flask import Blueprint, request, jsonify
from models.animal_model import Animal
from views.animal_view import render_animal_list, render_animal_detail

# Crear un blueprint para el controlador de animales
animal_bp = Blueprint("animal", __name__)


# Ruta para obtener la lista de animales
@animal_bp.route("/animals", methods=["GET"])
def get_animals():
    animals = Animal.get_all()
    return jsonify(render_animal_list(animals))


# Ruta para obtener un animal específico por su ID
@animal_bp.route("/animals/<int:id>", methods=["GET"])
def get_animal(id):
    animal = Animal.get_by_id(id)#obtener a un solo animal, mandarle el id de la solcitud que esta en el "link"
    if animal:#valor de verdad de un objeto es verdad o falso
        return jsonify(render_animal_detail(animal))#jsonify devuelve formato json
    return jsonify({"error": "Animal no encontrado"}), 404


# Ruta para crear un nuevo animal
@animal_bp.route("/animals", methods=["POST"])#definir la ruta por post asociada a la funcion create_animal, es @animal:bp un decorador esta haceidno unaruta mediante post y asociado a una funcion
def create_animal():
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    # Validación simple de datos de entrada
    if not name or not species or age is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400#en el caso de no existan los campos

    # Crear un nuevo animal y guardarlo en la base de datos
    animal = Animal(name=name, species=species, age=age)#creo el modelo y una unstancia, creamos un objeto , la clase animal tiene funcion save, que es save, con eso insertamos 
    animal.save()

    return jsonify(render_animal_detail(animal)), 201#lo renderizamos en formato json y enviamos junto con el 201


# Ruta para actualizar un animal existente
@animal_bp.route("/animals/<int:id>", methods=["PUT"])#la ruta siguie siendo la musma, loq ue cambia es el metodod, es una API por eso tulizamos los metodos, esta asociado a update animal
def update_animal(id):
    animal = Animal.get_by_id(id)#el id viene del link

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    data = request.json#recuperamos la informacion y los datos del animal lo enviamos a la funcion uptdate 
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    # Actualizar los datos del animal
    animal.update(name=name, species=species, age=age)

    return jsonify(render_animal_detail(animal))


# Ruta para eliminar un animal existente
@animal_bp.route("/animals/<int:id>", methods=["DELETE"])#ruta no cambia lo unico que cambia es el metodo el verbo en http
def delete_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404#404 no encuentra, 

    # Eliminar el animal de la base de datos
    animal.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
