def render_animal_list(animals):#recibira una lista y los formateara en un diccionario, cada elemento lo convertira en un dcicionario 
    # Representa una lista de animales como una lista de diccionarios
    return [
        {#tiene fomrati de un json 
            "id": animal.id,
            "name": animal.name,
            "species": animal.species,
            "age": animal.age,
        }
        for animal in animals #for de compresion itera una lista al elemento de la izquierda 
    ]


def render_animal_detail(animal):#recibir solo 1 animal, dar formato de un dciionario 
    # Representa los detalles de un animal como un diccionario
    return {
        "id": animal.id,
        "name": animal.name,
        "species": animal.species,
        "age": animal.age,
    }
