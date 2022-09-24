# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def inputQuarter():
    check = True
    while check:
        x = int(input('Введите номер четверти: '))
        if 0 < x < 5: return str(x)
        else: print('Введите число от 1 до 4')
match inputQuarter():
    case '1':
        print('x > 0; y > 0')
    case '2':
        print('x < 0; y > 0')
    case '3':
        print('x < 0; y < 0')
    case '4':
        print('x > 0; y < 0')
