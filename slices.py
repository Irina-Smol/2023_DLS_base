'''
Дан list x:

x = [1, 2, 3, 4, 5]
x[<YOUR CODE>] = [-1, -3, -5]

Заполните слайс вместо <YOUR CODE>, чтобы результатом стал следующий list:
[-5, 2, -3, 4, -1]
'''
x[::-2] = [-1, -3, -5]
print(x)

# x[ : : -2] выбирает из списка элементы с шагом -2 начиная с последнего, так как шаг отрицательный, то есть [5, 3, 1] ;
# [5, 3, 1] = [-1, -3, -5] присваивает выбранным элементам значения -1, -3 и -5
