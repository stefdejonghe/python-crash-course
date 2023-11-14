from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car("volkswagen", "beetle", 1985)
print(my_beetle.get_descriptive_name())

my_honda = EC("honda", "e", 2023)
print(my_honda.get_descriptive_name())
