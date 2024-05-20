from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.animal_model import Animal
from views import animal_view

# Importamos el decorador de roles
from utils.decorators import role_required

animal_bp = Blueprint("animal", __name__)


@animal_bp.route("/animals")
@login_required
def list_animals():
    animals = Animal.get_all()
    return animal_view.list_animals(animals)


@animal_bp.route("/animals/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_animal():
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = float(request.form["peso"])
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            animal = Animal(marca=marca, peso=float(peso), sabor=sabor,origen=origen)
            animal.save()
            flash("Animal creado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.create_animal()


@animal_bp.route("/animals/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = float(request.form["peso"])
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            animal.update(marca=marca, peso=peso, sabor=sabor,origen=origen)
            flash("Animal actualizado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.update_animal(animal)


@animal_bp.route("/animals/<int:id>/delete")
@login_required
@role_required("admin")
def delete_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if current_user.has_role("admin"):
        animal.delete()
        flash("Animal eliminado exitosamente", "success")
        return redirect(url_for("animal.list_animals"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
