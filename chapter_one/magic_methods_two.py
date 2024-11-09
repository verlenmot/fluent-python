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

class Reversion():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value * other
    
    def __mul__(self, other):
        return self.value + other
    
reverted_int = Reversion(5)

print(reverted_int * 5)
print(reverted_int + 5)
