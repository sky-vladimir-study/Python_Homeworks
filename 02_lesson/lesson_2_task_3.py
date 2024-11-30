from math import ceil

def square(a, b):
    return ceil(a*b)

a = float(input('Введите сторону квадрата 1: '))
b = float(input('Введите сторону квадрата 2: '))

print(f'Округленная в большую сторону сумма - {square(a,b)}')
