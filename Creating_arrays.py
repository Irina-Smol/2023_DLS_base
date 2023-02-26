'''
Дан массив 

A[0,…,N-1]

Реализуйте функцию cumsum_and_erase(...), принимающую один обязательный аргумент A и один опциональный аргумент erase, по умолчанию равный 1.

Функция должна выполнять следующие действия: 
сформировать массив B[0,…,N−1], где 
Bi =A0 +…+Ai --- массив частичных сумм массива A;
удалить из массива B все элементы, равные параметру erase; получить массив C;
вернуть C в качестве ответа

Постарайтесь сделать это за время O(N) без использования Numpy.

Пример работы функции: 

A = [5, 1, 4, 5, 14] 
B = cumsum_and_erase(A, erase=10) 
assert B == [5, 6, 15, 29], "Something is wrong! Please try again"
'''
# 1
def cumsum_and_erase(A, erase=1):
    s = 0
    C = []   
    for i in range(len(A)):
        s+=A[i]
        if s!=erase: C.append(s)

    return C
  
  # 2
  def cumsum_and_erase(A, erase = 1):
    B = [sum(A[:i]) for i in range(1, len(A) + 1) if sum(A[:i]) != erase]
    return B
