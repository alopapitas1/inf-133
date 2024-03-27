import requests
import json

url = "http://localhost:8000/deliveries"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocoalte_data = {
    "chocolate_type": "tableta",
    "peso": "pesado",
    "sabor": "rico"
}
response = requests.post(url=url, json=new_chocoalte_data, headers=headers)
print(response.json())

new_chocoalte_data = {
    "chocolate_type": "trufas",
    "peso": "pesado",
    "sabor": "rico",
    "relleno": "chocolate"
}
response = requests.post(url=url, json=new_chocoalte_data, headers=headers)
print(response.json())

new_chocoalte_data = {
    "chocolate_type": "bonbones",
    "peso": "pesado",
    "sabor": "rico",
    "relleno": "chocolate"
}
response = requests.post(url=url, json=new_chocoalte_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{choco_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "plate_number": "XYZ789"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("chocolate actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{vehicle_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())
