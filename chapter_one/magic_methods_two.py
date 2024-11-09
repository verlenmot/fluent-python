class Test():
    a = 5
    b = 7

    def __getitem__(self, index):
        return 5 + index
    
    def __add__(self, other):
        return other
    
    def __mul__(self, other):
        return other * 2

example = Test()

print(example[2])

print(example + 9)

print(example * 2)