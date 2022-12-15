def kor(x):
    a = [0] * x
    for i in range(x):
        b = False
        while not b:
            num = float(input(f"Введите {i + 1} координату: "))
            a[i] = num
            b = True
            if a[i] == 0:
                b = False
                print("Координаты не должны быть равны 0 ")

    return a


def checkKor(xy):
    if xy[0] > 0 and xy[1] > 0:
        print("Точка находится в 1 четверти плоскости")
    elif xy[0] < 0 and xy[1] > 0:
        print("Точка находится в 2 четверти плоскости")
    elif xy[0] < 0 and xy[1] < 0:
        print("Точка находится в 3 четверти плоскости")
    else:
        print("Точка находится в 4 четверти плоскости")


koordinate = kor(2)
checkKor(koordinate)
