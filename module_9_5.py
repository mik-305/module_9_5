class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError()
    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        while self.pointer < self.stop:
            self.pointer += self.step
            #print('--------------->', self.pointer)
            #return 'Подсчёт закончен'
            return self.pointer
        raise StopIteration()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

try:
    iter1 = Iterator(100, 200, 1)
    for i in iter1:
        print(i, end='')

except StepValueError:
    print('Шаг указан неверно')
iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')






