# 1
st = 'as 23 fdfdg544'
for l in set(st):
    print(f'{l} - {st.count(l)}')

# lists
# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = []
# for i in numbers:
#     if i > 4:
#         arr.append('GT')
#     elif i <= 4:
#         arr.append('LT')
# print(arr)
print(['GT' if i > 4 else 'LT' for i in numbers])

# 2
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
print([(i, j) for i in list1 for j in list2 if not i + j])


# 3
def numbs(number):
    temp = {"odd": 0, "even": 0}

    for n in str(number):
        if int(n) % 2:
            temp["odd"] += 1
        else:
            temp["even"] += 1

    return temp


print(numbs(11222))

# 4
number = 32750


def terms(number):
    string = ''
    for n, m in zip(str(number), range(len(str(number)), 0, -1)):

        if n == str(0) and m == 1:
            pass

        elif m == len(str(number)):
            string += (n + ('0' * (m - 1)))

        else:
            string += ' + ' + (n + ('0' * (m - 1)))

    return string


print(terms(number))
