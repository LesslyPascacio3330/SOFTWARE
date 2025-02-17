from car import Car
from account import Account
from uberX import UberX
from user import User 


if__name__ == "__main__" :
print("Inicializando las info de los carros")
print("Car")
car = Car("AMS256", Account("Andres Herrera", "ASD12365", "3375897@clases.edu.sv", "2563"))
print(vars(car))
print(vars(car.driver))

print("UberX")
uberX = UberX("KLO365", Account("Marco Solis", "SGHJ1236", 
"3375897@clases.edu.sv", "7856"), "Toyota", "Corolla")
print(vars(uberX))
print(vars(uberX.driver))

print("User")
user = User("Mariana Valle", "SDFG125F", "3375897@clases.edu.sv", "7856")
print(vars(user))