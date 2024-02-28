from zeep import Client
client=Client('http://localhost:8000')
result=client.service.Saludar(nombre="Alain")
sumar=client.service.Sumar(a=1,b=2)
pal=client.service.CadenaPalindromo(pal="Camilo")
print(result)
print(sumaDos)
print(palindromo)
