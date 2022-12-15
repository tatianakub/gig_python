#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def inputNum(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите числа {xyz[i]}: "))
    return a


def predicate(x):
    b = not (x[0] or x[1] or x[2])
    c = not x[0] and not x[1] and not x[2]
    result = b == c
    return result


res = inputNum(3)

if predicate(res) == True:
    print("Истина")
else:
    print("Ложь")
