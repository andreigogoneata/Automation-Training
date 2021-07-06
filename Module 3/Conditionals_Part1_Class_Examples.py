

print('                ')

print('      EX1       ')

print('                ')


print('Start Fooo Barrr $$$$$$$')

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')
print('End Fooo Barrr $$$$$$$$$')


print('                ')

print('      EX2       ')

print('                ')


print("Started What Line Will be executed Yes / No #####")

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:  #
    print('Outer condition is true')  #

    if 10 > 20:  # x
        print('Inner condition 1')  #

    print('Between inner conditions')  #

    if 10 < 20:  # x
        print('Inner condition 2')  #

    print('End of outer condition')  #
print('After outer condition')  #

print("End Line Will be executed Yes / No #############")


print('                ')

print('      EX3       ')

print('                ')


print('Started if / else statement ^^^^^^^^')
x = 20
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
print('Ended if / else statement ^^^^^^^^')


print('                ')

print('      EX4       ')

print('                ')


print('Start What is my name ? &&&&&&&&&&&')

name = 'Your Name'
if name == 'Andreea':
    print('Hello Andreea')
elif name == 'Lidia':
    print('Hello Lidia')
elif name == 'Andrei':
    print('Hello Andrei')
elif name == 'Daniel':
    print('Hello Daniel')
elif name == 'Sergiu':
    print('Hello Sergiu')
else:
    print("I don't know who you are!")

print('End What is my name ? &&&&&&&&&&&')


print('                ')

print('      EX5       ')

print('                ')


print('Start Can i get your name ? %%%%%%%%%%%')

names = {
    'Andreea': 'Hello Andreea',
    'Lidia': 'Hello Lidia',
    'Andrei': 'Hello Andrei',
    'Daniel': 'Hello Daniel',
    'Sergiu': 'Hello Sergiu'
}

print(names.get('Andreea', "I don't know who you are!"))
new_name = 'Gogo'
print(names.get(new_name, f"{new_name} I don't know who you are!"))

print('End Can i get your name ? %%%%%%%%%%%')


print('                ')

print('      EX6       ')

print('                ')


class_presence = 1

if class_presence == 1:
    print('Andrei');print('Andreea');print('Lidia')
elif class_presence == 2:
    print('Sergiu');print('Daniel')
elif class_presence == 3:
    print('Gogo');print('Andrei C.')
elif class_presence == 4:
    print('Yeyy');print('Everyone has attended this class')
else:
    print('Really? No one that is registered for this class has attended');print(':-((')


print('                ')

print('      EX7       ')

print('                ')



if 'Gogo' in 'Gogo is presenting this class': print('1'); print('2'); print('3');print('Hei Hei :D')

print("Andrei C.") if class_presence == 7 else print("Andrei C. is not in class")


print('                ')

print('      EX8       ')

print('                ')


monthly_income = 100  # $100
monthly_expenses = 500  # $500

print("You are in the Green go ahead and spend it all :D !!!") if monthly_income > monthly_expenses else print("=") if monthly_income == monthly_expenses else print("Stop what you're doing !!! You will go broke ---$$$$$")


print('                ')

print('      EX9       ')

print('                ')

monthly_expenses = 200
fun_expenses = 33
monthly_income = 500

if monthly_expenses > fun_expenses and monthly_income > monthly_expenses:
    print("You are in the Green go ahead and spend it all :D !!!")

print('                ')

print('      EX10       ')

print('                ')
monthly_expenses = 200
fun_expenses = 33
monthly_income = 500

if monthly_expenses > fun_expenses or monthly_expenses > monthly_income:
  remaining_budget = monthly_income - monthly_expenses - fun_expenses
  print(f"At least one statemet is true you have more money $$${remaining_budget} then you think !!!!")
  print('                ')