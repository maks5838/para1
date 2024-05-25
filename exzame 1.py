# class Vehicle:
#     def __init__(self, make, model, mileage):
#         self.make = make
#         self.model = model
#         self.mileage = mileage
#
#     def display_info(self):
#         print(f"Make: {self.make}, Model: {self.model}, Mileage: {self.mileage} miles")
#
#     def drive(self, miles):
#         self.mileage += miles
#
#     def maintenance_needed(self):
#         return self.mileage > 100000
#
#     def reset_mileage(self):
#         self.mileage = 0
#
#
# if __name__ == "__main__":
#     car = Vehicle("Toyota", "Camry", 50000)
#     car.display_info()
#
#     car.drive(60000)
#     car.display_info()
#
#     print(car.maintenance_needed())
#
#     car.reset_mileage()
#     car.display_info()
