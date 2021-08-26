class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, leg_size):
        super().__init__(name, age)
        self.leg_size = leg_size
        Cinderella.__count += 1

    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nРазмер туфлей: {self.leg_size}"

    @classmethod
    def count(cls):
        return cls.__count


class Prince(Human):
    def __init__(self, name, age, leg_size):
        super().__init__(name, age)
        self.leg_size = leg_size

    def find(self, array):
        for cin in array:
            if self.leg_size == cin.leg_size:
                return cin

c = Cinderella('Женя',20,45)
c2 = Cinderella('Рунь',42,37)
p = Prince('Ваня',30,45)
cin = [c,c2]
print(p.find(cin))
print(Cinderella.count())


class Notebook:
    __notes = []
    @classmethod
    def create(cls):
        name = input("")
        cost = input("")
        cls.__notes.append({'name': name, "cost": cost})
    @classmethod
    def all_notes(cls):
        return lambda note: note, cls.__notes



while True:
    print("1. Создать запись")
    print("2. Список всех записей")
    print("3. Общая сума всех покупок")
    print("4. Самая дорогая покупка")
    print("5. Поиск по названию покупки")
    print("6. Виход")
    ans = input("Виберите действие: ")
    if ans == '1':
        pass
    elif ans == '2':
        pass
    elif ans == '3':
        pass
    elif ans == '4':
        pass
    elif ans == '5':
        pass
    elif ans == '6':
        pass
    else:
        print("ВЫБЕРИТЕ ИЗ МЕНЮ!")
