# strings
# 1
st = 'as 23 fdfdg544'
print([i for i in st if i.isdigit()])

# 2
st = 'as 23 fdfdg544 34'
st = [i for i in st.split() if not i.isalpha()]
for i in st:
    if i.isdigit():
        pass
    else:
        temp = st.index(i)
        temp2 = ''
        for j in i:
            if j.isdigit():
                temp2 += j
        st[temp] = temp2
print(st)

# lists
# 1
greeting = 'Hello, world'
print(list(greeting.upper()))

# 2
print([num ** 2 for num in range(50) if num % 2 or not num])  # not num эквивалент num == 0


# function
# 1
def print_list(list):
    print(list)


print_list([1, 2, 3, 4, 5, 6])


# 2
def minimal(num_1, num_2, num_3):
    print(min(num_1, num_2, num_3))
    return min(num_1, num_2, num_3)


d = minimal(1, 2, 3)
print(d)


# 3
def maximal(num_1, num_2, num_3):
    print(max(num_1, num_2, num_3))
    return max(num_1, num_2, num_3)


b = maximal(1, 2, 3)
print(b)


# 4
def strange(*arg):
    print(max(arg))
    return min(arg)


w = strange(1, 2, 3, 4, 5, 6, 7, 8)
print(w)


# 5
def list_max(list):
    return max(list)


print(list_max([1, 2, 3, 4, 5, 6, 7]))


# 6
def list_min(list):
    return min(list)


print(list_min([1, 2, 3, 4, 5, 6, 7]))


# 7
def list_sum(list):
    return sum(list)


print(list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 8
def list_avg(list):
    return sum(list) / len(list)


print(list_avg([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# decorators
def decor(fun):
    def inner(*args, **kwargs):
        return fun(*args, **kwargs).replace('_', ' ')

    return inner


@decor
def pr():
    return 'Hello_boss_!!!'


print(pr())
