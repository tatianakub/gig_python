# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
#
# out
#5.099

def kor(x):
    a = [0] * x
    for i in range(x):
        b = False
        while not b:
            num = float(input(f"Введите {i + 1} координату точки: "))
            a[i] = num
            b = True
            if a[i] == 0:
                b = False
                print("Координаты не должны быть равны 0 ")

    return a

def calcLength(a, b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return length


print("Введите координаты точки А")
A = kor(2)
print("Введите координаты точки В")
B = kor(2)

print(f"Длина отрезка: {format(calcLength(A, B), '.2f')}")