print('     Iterable Objects     ')

print('      EX1       ')

# Iterables iter()

print(iter('String'))  # String

print(iter(['list1', 'list', 'list3']))  # list

print(iter(('tuple1', 'tuple2', 'tuple3')))  # tuple

print(iter({'set1', 'set2', 'set3'}))  # set

print((iter({'aaa': 1, 'bbb': 2, 'ccc': 3})))  # dict

print('  Not Iterable ')

print('      EX2       ')

# print(iter(112))  # int
#
# print(iter(2.47))  # float
#
# print(iter(len))  # built-in functions

print('       For over lists       ')

print('      EX3       ')
#
fruits = ["apple", "banana", "cherry"]
brake_fruits = ["portocala", 'ssss', "Pepene", "Croampe"]

for i in fruits:
    print(i)

for i in 'str':
    print(i)

for i in brake_fruits:
    print(i)
    if i == 'ssss':
        break

for i in brake_fruits:
    if i == 'Croampe':
        break
    print(i)

print('       For over dict       ')

print('      EX4      ')

dict = {'a2a': 100, 'sale_price': 2, 'linetype': 4}

for k in dict.keys():
    print(k)

for k in dict.values():
    print(k)

for v in dict:
    print(dict[v])

i, j = (1, 2)
print(i, j)

for i, j in [(1, 2), (3, 4), (5, 6), (6, 7)]:
    print(i, j)

print(dict.items())

for k, v in dict.items():
    print('key =', k, 'value = ', v)

print('       Range Function      ')

print('      EX4      ')

# Syntax
# range(start, stop, step)
# start - Optional. An integer number specifying at which position to start. Default is 0
# stop - Required. An integer number specifying at which position to stop (not included).
# step - Optional. An integer number specifying the incrementation. Default is 1

my_range = range(3, 6)

for i in my_range:
    print(i)

my_range_step = range(3, 21)

for i in my_range_step:
    print(i)

for n in (0, 1, 2, 3, 4, 5, 6, 7, 8):
    print(n)

my_range = range(5, 20, 3)
for i in my_range:
    print(i)

print(list(range(-10, 5)))

print(list(range(5, -5)))

print(list(range(5, -10, -1)))

print(tuple(my_range))

print('       For over dict       ')

print('      EX5      ')

for i in ['aaa', 'bbb', 'ccc']:
    print(i)
else:
    print('I am done looping over the list')

for i in ['ddd', 'eee', 'zzz']:
    if i == 'zzz':
    # if i == 'xxx':
        break
    print(i)
else:
    print('i am not in the else case')
    # print('i am in the else')
