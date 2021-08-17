cart = []


while True:
    print("1. Создать запись")
    print("2. Список всех записей")
    print("3. Общая сумма всех покупок")
    print("4. Самая дорогая покупка")
    print("5. Поиск по названию товара")
    print("6. Выход")
    # print("7.")
    # print("8.")
    # print("9.")
    ans = input("Выберите ответ: ")

    if ans == "1":
        name = input("Введите название товара: ")

        while True:
            cost = input("Введите цену товара: ")
            if cost.isdigit():
                cost = int(cost)
                break
            else:
                print("ВЫ ДОЛЖНЫ ВВЕСТИ ЧИСЛО!")

        cart.append({"product": name, "cost": cost})

    elif ans == "2":
        print(cart)

    elif ans == "3":
        sum = 0
        for el in cart:
            sum += el["cost"]
        print(sum)

    elif ans == "4":
        max = 0
        for el in cart:
            if max < el["cost"]:
                max = el["cost"]
        print(max)

    elif ans == "5":
        find = input("Введите название покупки: ")
        for i in range(len(cart)):
            if cart[i]["product"] == find:
                print(cart[i])

    elif ans == "6":
        break

    else:
        "Неправильный ввод."
