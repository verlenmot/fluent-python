# Methods of splitting a list
example_list = "test hello rain".split()
example_list_two = list('ABCDEFGHIJKLMNOPQ')

# Equivalent result
print(example_list[2])
print(example_list.__getitem__(2))

# Equivalent result
print(example_list_two[2:8:2])
print(example_list_two.__getitem__(slice(2,8,2)))

# Endless print
class Example():

    def __getitem__(self, index):
        return example_list_two[index]

# test = Example()

