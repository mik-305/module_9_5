class StepValueError(ValueError):
    pass
class Iterator:
    #global pointer
    global pointer
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError()
    def __iter__(self):
        #global pointer     # ???
        pointer = self.start
        return self

    def __next__(self):
        #global pointer    # ???
        print('--------------->', pointer)
        pointer += self.step

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

try:
    iter1 = Iterator(100, 200, 1)
    print('Тип iter1 = ', type(iter1), '----', list(iter1))

    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг указан неверно')





