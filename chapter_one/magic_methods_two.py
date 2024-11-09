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

# Experiment
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

# Experiment
class Cup():
    def __init__(self, colour):
        self.colour = colour
    
    # def __add__(self, other):
    #     if type(other) == Coffee:
    #         return f"Pouring coffee into the {self.colour} cup!"
    
    def __add__(self, other):
        if type(other) == Coffee:
            print(f"Pouring coffee into the {self.colour} cup!")
            return FilledCup(self.colour, other)

class Coffee():
    def __init__(self, volume):
        self.volume = volume

class FilledCup(Cup):
    def __init__(self, colour, liquid):
        super().__init__(colour)
        self.liquid = liquid

coffee = Coffee(150)
cup = Cup("white")
filled_cup = cup + coffee
print(filled_cup.liquid.volume)