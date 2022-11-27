class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def __str__(self):
        return f"{self.color} {self.type} {self.year}"

    def start(self):
        return "Автомобиль заведен"

    def finish(self):
        return "Автомобиль заглушен"

car_1 = Car(color="Black", type="Limousine", year="2017")
print(car_1)
