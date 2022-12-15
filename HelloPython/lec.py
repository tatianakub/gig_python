# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ' , b, ' = ' , a+b)

# a = 1.3986
# b = 3
# c = round(a * b, 5)
# print(c)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username= input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Таня':
#     print('Я так ждал тебя, Таня!')
# else:
#     print('Привет, ', username)

# переворачивание числа
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(inverted)

# for

# r = range(10) #или диапазон (1, 5)
# for i in r:
#     print(i)

# help(int)  #если не знаешь что что делает, можно посмотреть


# функция
def fname(x):
    arg = 1
    print(fname(arg))
    print(type(fname(arg)))
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
