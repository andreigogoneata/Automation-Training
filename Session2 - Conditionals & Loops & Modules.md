# Session 2
## Conditionals | Loops | Modules in Python


##
## Python Conditions and IF stataments
 - Python supports the usual logical conditions from mathematics:
 
 ```js
 Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
```

##
- Python if Statement Syntax:
- Python relies on indentation


```js
if expression
 Statement
```

```js
t = 3
if t < 4:
   print ('That's True!')
```
##
```js
if expression
 Statement
else 
 Statement
```

```js
t = 3
if t < 4:
   print ('That's True!')
else:
   print ('Not True!')
```

- 'elif' expression

```js
x = 5
if x < 0:
   x = 0
   print('Negative changed to zero')
elif x == 0:
   print('Zero')
elif x == 1:
   print('Single')
else:
   print('More')
```

##
## Range function

- used when iterating over a sequence of numbers: range()
```js
for i in range(5):
    print(i)
```

```js
range(start, stop, step)
range(5, 10) -> 5, 6, 7, 8, 9
range(0, 10, 3) -> 0, 3, 6, 9
```

##
## For statements

- used for iterating over items of any sequence

```js
for val in sequence:
    instructions in for block
```

```js
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

```js
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    if val % 2 == 0:
       sum = sum + val

print("The sum is ", sum)
```

- 'break' parameter
- With the break statement we can stop the loop before it has looped through all the items:

```js
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

##

# While Loop

- With the while loop we can execute a set of statements as long as a condition is true.

```js
while test_expression:
    Body of while
```

```js
i = 1
while i < 6:
  print(i)
  i += 1
```

## 

# Enumerate

- The enumerate() method adds counter to an iterable and returns it (the enumerate object).

```js
grocery = ['bread', 'milk', 'butter']

for count, item in enumerate(grocery):
  print(count, item)

-> 
0 bread
1 milk
2 butter
```

## 

# Modules

- The module can contain functions, but also variables of all types (arrays, dictionaries, objects etc):

- mymodule.py
```js
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
``` 

```js
import mymodule

a = mymodule.person1["age"]
print(a)
```




