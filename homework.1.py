a = int(input()) #вводим коэффиценты
b = int(input())
c = int(input())
D = b**2 - 4 * a * c #ищем дискриминант
#ищем корни квадратного уравнения в зависимости от значения дискриминанта
if D>1:
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print(x1,x2)
if D == 0:
    x1 = -b / 2*a
    print(x1)
if D < 0:
    print('Нет корней')

