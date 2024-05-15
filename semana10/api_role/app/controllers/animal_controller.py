from flask import Blueprint, request, jsonify
from models.animal_model import Libro
from views.animal_view import render_animal_list, render_animal_detail
from utils.decorators import jwt_required, roles_required

# Crear un blueprint para el controlador de animales
libro_bp = Blueprint("libro", __name__)


# Ruta para obtener la lista de animales
@libro_bp.route("/libros", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_animals():
    animals = Libro.get_all()
    return jsonify(render_animal_list(animals))


# Ruta para obtener un animal específico por su ID
@libro_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_animal(id):
    animal = Libro.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404


# Ruta para crear un nuevo animal
@libro_bp.route("/libros", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_animal():
    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad=data.get("disponibilidad")

    # Validación simple de datos de entrada
    if titulo is None or autor is None or edicion is None or disponibilidad is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo animal y guardarlo en la base de datos
    animal = Libro(titulo=titulo, autor=autor, edicion=int(edicion),disponibilidad=bool(disponibilidad))
    animal.save()

    return jsonify(render_animal_detail(animal)), 201


# Ruta para actualizar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_animal(id):
    animal = Libro.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad=data.get("disponibilidad")


    # Actualizar los datos del animal
    animal.update(titulo=titulo, autor=autor, edicion=edicion,disponibilidad=disponibilidad)

    return jsonify(render_animal_detail(animal))


# Ruta para eliminar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_animal(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Animal no encontrado"}), 404

    # Eliminar el animal de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
