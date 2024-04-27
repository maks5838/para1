class Human:
    def __init__(self,name="Human"):
        self .name = name

class Auto:
    def __init__(self, brand):
        self .brand = brand
        self. passengers = []
        self.passengers_names = ""

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers_names += passenger.name + ","
            self.passengers.append(passenger)

    def print_passenger_name(self):
        if self.passengers:
            print(self.passengers_names)
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("Ніхто, ще не сів у автомобіль")

maksun = Human("МаксимПРО")
bogdan = Human("БогданВОДІЛА")


auto = Auto("Tesla model X")
auto.add_passenger(bogdan)
auto.add_passenger(maksun)
auto.print_passenger_name()