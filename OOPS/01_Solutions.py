class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model
        Car.total_cars += 1

    def full_name(self):
        return f"Car full name is {self.__brand} {self.model}"   

    def get_brand(self):
        return self.__brand + " !"
    # polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    

# inheritence- ElectricCar is a child class of Car
class ElectricCar(Car): 
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity=battery_capacity

# polymorphism
    def fuel_type(self):
        return "Electric"

my_car=Car("Toyota","Corolla")
# print(my_car.__brand)
print(my_car.get_brand())

my_new_car=Car("Tata","Punch")
print(my_new_car.model)
print(my_new_car.full_name())
print(my_new_car.fuel_type())

my_electric_car=ElectricCar("Tesla","Model 3",100)
print(my_electric_car.battery_capacity)
print(my_electric_car.full_name())
print(my_electric_car.fuel_type())
print(f"Total cars created: {Car.total_cars}")