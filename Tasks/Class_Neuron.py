'''
Реализуйте класс "Нейрон", у которого будет несколько методов
 __init__. Принимает на вход массив весов нейрона --- w = (w_1, \ldots, w_n), 
 а также функцию активации f (аргумент по умолчанию f(x)=x). Сохраняет веса и функцию внутри класса.
forward. 
Принимает на вход массив x = (x_1, \ldots, x_N) --- входы нейрона. Возвращает f(w_1x_1 + \ldots + w_nx_n). 
Возвращает массив x, который подавался на вход функции forward при её последнем вызове.
'''

class Neuron:
    def __init__(self, w, f = lambda x: x):
        self.w=w
        self.f=f

    def forward(self, x):
        self.x=x
        return self.f(sum([self.x[i]*self.w[i] for i in range(len(self.x))]))
    def backlog(self):
        return self.x
