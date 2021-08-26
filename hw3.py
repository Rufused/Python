from typing import Callable, List


def notebook() -> Callable:
    todo_list: List[str] = []

    def add_todo(todo: str = None) -> list:
        if todo is None:
            pass
        else:
            nonlocal todo_list
            todo_list.append(todo)
        return get_all()

    def get_all() -> list:
        #     temp = ''
        #     for el in todo_list:
        #         temp += f'{el}\n'
        #     return temp
        return todo_list

    return add_todo


book = notebook()
book('help')
book('print')
book('stop')
book(35)
book(['drop'])
print(book())
# ?
notbook = notebook()
print(notbook(123))

print(list(filter(lambda x: not x % 15, list(range(1000)))))

summ = lambda x: x + int(f'{x}{x}') + int(f'{x}{x}{x}')
print(summ(7))



def persistence(num):
    per = 0
    mul = 1
    while num > 0:
        # print(per, num, mul, '--------')
        per += 1
        mul = mul * (num % 10)
        num = num // 10
        # print(per, num, mul, '--------')
        if num <= 1 and mul < 10:
            break
        elif not num and mul:
            num, mul = mul, 1

    return per
print(persistence(39))


def persistence(num):
    per = 0
    while len(list(str(num))) > 1:
        per += 1
        temp = 1
        for n in list(str(num)):
            temp *= int(n)
        num = temp

    return per


print(persistence(195))

#OR

from functools import reduce


def persistence(num):
    per = 0
    while len(list(str(num))) > 1:
        per += 1
        num = reduce(lambda x,y: int(x)*int(y),list(str(num)))
    return per


print(persistence(195))
