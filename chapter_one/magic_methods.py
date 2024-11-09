import random

# Methods of splitting a list
example_list = "test hello rain".split()
example_list_two = list('ABCDEFGHIJKLMNOPQ')

# Equivalent result
print(example_list[2])
print(example_list.__getitem__(2))

# Equivalent result
print(example_list_two[2:8:2])
print(example_list_two.__getitem__(slice(2,8,2)))


class Example():

    def __getitem__(self, index):
        return "Idem"

test = Example()

# Endless print
# for x in test:
#     print(x)


# Class to try out __len__ and __getitem__
class GetLen():
    def __init__(self):
        self.numbers = "one two three four five six seven eight nine ten".split()
    
    def __len__(self):
        return len(self.numbers)
    
    def __getitem__(self, i):
        return self.numbers[i]

# Experiments
get_len = GetLen()

print(len(get_len))
print(get_len[3])
print(get_len[1::2])

# for item in get_len:
#     print(item)
reversed(get_len)

for item in reversed(get_len):
    print(item)

print(sorted(get_len))

print(random.choice(get_len))