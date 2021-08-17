arr = [-1, -2, 3, 4, 555]
arr2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


while True:

    ans = input("""
1. Find the minimum number in the list.
2. Remove duplicates from the list.
3. Replace every 4th element with x.
4. Find an element close to the arithmetic mean.
5. Create "Square". 
6. Print the multiplication table.
7. Exit.
Chose func: """)

    if ans == "1":
        print(min(arr2))

    elif ans == "2":
        arr2 = list(set(arr2))
        print(arr2)

    elif ans == "3":
        # for i in arr2[::4]: arr2[arr2.index(i)] = 'x'
        # print(arr2)
        for i in range(len(arr2)):
            if ((i + 1) % 4) == 1:
                arr2[i] = "x"
        print(arr2)

    elif ans == "4":
        avg = 0
        for i in arr:
            avg += i
        avg /= len(arr)
        print(min(arr, key=lambda x: abs(x - avg)))

    elif ans == "5":
        while True:
            try:
                side = int(input("Input the side size: "))
                break
            except:
                print("WRONG!")

        square = ''
        for i in range(side):
            if i == 0 or i == side - 1:
                square += '*' * side
            else:
                square += '*' + ' ' * (side - 2) + '*'
            square += '\n'
        print(square)

    elif ans == "6":
        x = 1
        y = 1
        table = ""
        while y <= 9:
            table += f"{x * y}" + " " * (6 - len(str({x * y})))

            x += 1
            if x // 10:
                x = 1
                y += 1
                table += "\n"
        print(table)
    elif ans == "7":
        break

    else:
        print("WRONG!")
