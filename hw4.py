from datetime import datetime


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.S = x * y

    def __add__(self, other):
        return self.S + other.S

    def __sub__(self, other):
        return self.S - other.S

    def __mul__(self, other):
        return self.S * other.S

    def __truediv__(self, other):
        return self.S / other.S

    def __eq__(self, other):
        return self.S == other.S

    def __ne__(self, other):
        return self.S != other.S

    def __lt__(self, other):
        return self.S < other.S

    def __gt__(self, other):
        return self.S > other.S

    def __len__(self):
        return self.x + self.y


class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.S = x ** 2


q = Rectangle(2, 3)
s = Square(4)
print(q - s)
q = Rectangle(2, 2)
s = Square(2)
print(q == s)
print(q/s)

class Transport:
    def __init__(self, time, cost):
        self.time = time
        self.cost = cost
        self.type = 'Транспорт'

    def __add__(self, other):
        return self.time + other.time

    def __sub__(self, other):
        return self.time - other.time

    def __str__(self):
        return f"Час поїздки: {self.time} Годин\n" \
               f"Ціна поїздки: {self.cost}\n" \
               f"Тип транспорту: {self.type}\n" \
               f"Використай перегрузку метода."

    def compare(self, other):
        if self.time > other.time:
            return f"{self.type} прибуде на {self.time - other.time} швидше за {other.type}"
        elif self.time == other.time:
            return f"{self.type} та {other.type} прибудуть за {self.time}"
        elif self.time < other.time:
            return f"{other.type} прибуде на {other.time - self.time} швидше за {self.type}"
        else:
            print("HWAT?!")


class Plane(Transport):
    def __init__(self, time, cost, travel_class, registration=datetime.now()):
        super().__init__(time, cost)
        self.type = 'Літак'
        self.travel_class = travel_class
        self.registration = registration

    def __str__(self):
        return f"Час регістрації: {self.registration}\n" \
               f"Класс: {self.travel_class}\n" \
               f"Ціна за квиток: {self.cost} Грн.\n" \
               f"Час у літаку: {self.time} Годин\n" \
               f"Час у повітрі: {self.time_in_air()} Годин"

    def time_in_air(self):
        return self.time - 2

    def print_time_in_air(self):
        return f"Загальний час у повітрі: {self.time} годин"


class Car(Transport):
    def __init__(self, time, cost, passengers, distance):
        super().__init__(time, cost)
        self.passengers = passengers
        self.distance = distance
        self.type = 'Авто'

    def __str__(self):
        return f"Шлях: {self.distance} Км.\n" \
               f"Пасажири: {self.passengers}\n" \
               f"Вартість пального: {self.cost} Грн.\n" \
               f"Час поїздки: {self.time} Годин\n" \
               f"Загальні витрати на поїздку {self.gas_cost()} Грн."

    def gas_cost(self):
        return (self.cost * self.distance) / 10

    def print_gas_cost(self):
        return f"При ціні пального: {self.cost} Грн. за літр\n" \
               f"На шлях {self.distance} Км.\n" \
               f"Потрібно витатити мінімум {(self.cost * self.distance) / 10} Грн."


class Train(Transport):
    def __init__(self, time, cost, travel_class):
        super().__init__(time, cost)
        self.travel_class = travel_class
        self.type = 'Потяг'

    def __str__(self):
        return f"Вагон: {self.travel_class}\n" \
               f"Ціна за квиток: {self.cost} Грн.\n" \
               f"Час перевезення: {self.time} Годин"


t = Train(5, 140, "Купе")
p = Plane(3, 578, 1)
print(t)
print("")
print(p)
print("")
print(p.compare(t))

text = []


class Letter:
    __count = 0

    @classmethod
    def count(cls):
        return cls.__count

    def __init__(self, __text = ''):
        self.__text = __text
        Letter.__count += 1

    def set(self):
        self.__text = input("Введіть щось: ")

    def get(self):
        return self.__text

    def to_text(self):
        text.append(self.__text)


print(Letter.count())
texted = Letter()
print(Letter.count())
texted.set()
print(text)
texted.to_text()
print(text)
print(texted.get())
