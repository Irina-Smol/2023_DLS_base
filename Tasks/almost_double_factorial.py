'''
Реализуйте функцию almost_double_factorial(n), вычисляющую произведение всех нечётных натуральных чисел, не превосходящих n.
В качестве аргумента ей передаётся натуральное (ноль -- натуральное) число n⩽100.
Возвращаемое значение - вычисленное произведение.

Комментарий. В случае, если n = 0, требуется вернуть 1.

В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!
'''
# 1
def almost_double_factorial(n):
    x = 1
    if n == 0:
        x = 1
    else:
        for i in range(1, n+1):
            if i % 2 != 0:
                x = x * i
                i = i + 1
    return x
    
# 2   
def almost_double_factorial(n):
    res = 1
    for i in range(1, n+1, 2):
        res *= i
    return res