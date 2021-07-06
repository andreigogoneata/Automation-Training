# Session 1
## Data Types in Python
Data Type | Data value
------------ | -------------
Integers | 5, 8, 400
Float | 4.3, 5.7, 12.3
String | words, characters
Boolean | True or False
List | [1, 2, 3, 4]  
Dictionaries | {1:'first', 2:'second'}
Tuples | (1,2,3)
Sets | {1, 2, 3}
##
## Everything is an object in Python
 - In Python a name is just a label for a certain object
 - Each certain name references a certain object
 
 ```js
 x = 300          //Reference count to object 300 is 1
 y = 300          //Reference count to object 300 is 2
 z = [300, 300]   //Reference count to object 300 is 4
 
 del x            //del doesn't removes the value 300, it removes the name x that was refering to 300
                  //Reference count to object 300 is decreased to 3
 y = None
 z = None         //Reference count to object 300 is 0
  ```
  
 Every python object holds 3 things
 - Its **Type**
 - Its **Value**
 - Its **reference count**
 
## PyObject
Atribute | Values
------------ | -------------
Type | integer
Refcount | 2
Value | 300
```js
x = 300
y = 300
print (id(x))
print (id(y))
print (x is y)
 > 28501818
 > 28501818
 > True
```
## Garbage collector
- Object refCount = 0    -> Object is deleted and the memory is deallocated
##
### Using **print** function to display the type of a variable:
<details>
 <summary>Click to expand</summary>
 
 ```js
- print ("True is of type:", type(True))
  - True is of type: <type 'bool'>
- print ('ion' is of type:", type('ion'))
  - ion is of type: <type 'str'>
- print ("100 is of type:", type(100))
  - 100 is of type: <type 'int'>
- print ("3.14 is of type:", type(3.14))
  - 100 is of type: <type 'float'>
- print ("[1, 2, 3] is of type:", type([1, 2, 3]))
  - [1, 2, 3] is of type: <type 'list'>
- print ("(1, 2, 3) is of type:", type((1, 2, 3)))
  - (1, 2, 3) is of type: <type 'tuple'>
  
- print ("{1, 2, 3} is of type:", type({1, 2, 3}))
  - {1, 2, 3} is of type: <type 'set'>
- print ("{1: 2}) is of type:", type({1: 2}))
  - {1: 2}) is of type: <type 'dict'>
  
- print (type(True))
  - <type 'bool'>
- print (type(1))
  - <type 'int'>
  
- print (type(True) == type(1))
  - False
- print (True == 1)
  - True
  
 ```
 
</details>

##
### Reading keyboard input
<details>
 <summary> Click to expand </summary>
 
```js
name = input("Give me a name: ")
print ("Your name is: %s" % name)

value1= input("Give me a value: ")
value2= input("Give me anoter name: ")
print ('The sum is: %s' % value1 + value2)

value1= int(input("Give me a value: "))
value2= int(input("Give me anoter name: "))
sum = int(value1) + int(value2)
print ('The sum is: %d' % sum)

ch = input("Enter a character: ")[0]
print (ch)

ch = input("Enter a character: ")[0:6]
print (ch)

result = eval(input("Give me an expression: "))
print (result)

//argv file

print ("Name: %s, Age: %d" % ('John', 22))  
```

</details>

##
### Working with basic arithmetic operators
<details>
 <summary> Click to expand </summary>
 
```js
import math
#from math import sqrt

a = 5 
b = 4
s = 'string'

print (a+b)
print (type(a+b))

print (a/b) 
print (type(a/b))
//print (a//b)

print (a*b)
print (a%b)
print (type(a/b))

c = 2.5
print (type(c*a))
print (math.sqrt(b))

print (str(a) + s)
print (s * 5)

> Operations with Strings
s = 'hi'
c = 5

print (s[1])
print (len(s))
print (s + 'there')

print ('Value of c is:' + c)
print ('Value of c is:' + str(c))
print ('value of c is: %d ' % c)
```

</details>

##
### Working with lists
<details>
 <summary> Click to expand </summary>
 
```js
>Functions 'append, extend and insert'
a = [1, 2, 3, 4, 5]
b = a

print (a)
print (type(a))

a.append(6)
print (a)
a.append(['ana', 'are', 'mere']) #use also extend to see the list length difference
print (a)
print (len(a))

a.insert(1, 'new')
print (a)
 
#time_difference_file

>Functions 'pop and remove'
a = [1, 2, 3, 4, 5, 1]
a.pop(1) #use also remove to see the difference
print (a)

>Function index
print (a.index(2))

>Function reverse
a.reverse()
print (a)

>Function sort
a.sort()
print (a)

>Slicing
a = [1, 2, 3, 4, 5]
print (a[2:4])
print (a[:2])
print (a[2:])

b = a 
b[1] = 'elem'
print (b)
print (a)
b= a[:]
b[1] = 2
print ('\n', b)
print (a)
```
Exercises: https://pynative.com/python-list-exercise-with-solutions/

 
</details>

##
### Working with tuples
<details>
 <summary> Click to expand </summary>
 
```js
a = (1)
print (type(a))
a = (1,)
print (type(a))
a = (1, 2, 2, 2, 3, 4, 2)
print ('a =', a)
print ('2 apare de %s ori in tupla' % a.count(2))
print ('4 apare in tupla pe pozitia %d' % a.index(4)
 
my_list = [1, 2, 3]
my_set = {4, 5, 6}
print (tuple(my_list))
print (tuple(my_set))
 
print ('*' * 60)
a = [1, 2, 3, 4]
b = (5, 6, 7, a)
print (b)

a.append(9)
print (b)
c = [9999, 333]
a = 1, 2, 3, 4, 5, c
print (a)
print (type(a))

print (a[5][0])
a, b = 1, 2
print (a)
print (b)
 
// a, b = 1, 2, 3
 
a = (11, 22, 33)
a1, a2, a3 = a
print (a1)
print (a2)
print (a3)
# a[0] = 1
```

</details>

##
### Working with sets
<details>
 <summary> Click to expand </summary>
 
```js
a = {1, 2, 3}
b = set([1,2,3])
print (type(a), type(b))

a.add(4)
print ('a =', a)

//a.add(5, 6)
//len(a)
//a.add((5,6))
//a.add([7,8])
//a.update([7,8])
//a.update()

b = a
b.add(9)
print (a,b)

b = a.copy()
b.add(10)
print (a,b)
a.remove(1)
a.pop

#Operation between two sets
diff = b.difference(a)
print ('b-a: ', diff)

uni = a.union(b)
print ('a+b: ', uni)

inter = a.intersection(b)
print ('a intersected with b: ', inter

// converting to and from lists
my_list = [1, 2, 3]
my_set = set(my_list)
print (my_set)

my_new_list = list(my_set)
print (my_new_list)
```

</details>

##
### Working with dictionaries
<details>
 <summary> Click to expand </summary>
 
```js
//basics
a  = {'key': 'value'}
print (a)
print (type(a))

a[1] = 10
print (a)

a['list'] = [1, 2, 3]
a[1, 2] = (1,2)   #tuple as a key
print (a)

a[[1, 2]] = [1, 2, 3]   #list as a key
print (a)
a  = {'first': 'element', 1: 4, 'third': 5, (1, 2): None, 'testing': 'another one'}
print (a)

> Operations with dictionaries
#delete operation
del a['third']
print (a)

//add operation
a['third'] =  4
print (a)

//update operation
a['third'] = 5
print (a)

print ('Dictionary keys:', a.keys())
print ('Dictionary values:', a.values())
print ('Dictionary items:', a.items())
```

</details>

##
### Working with datetime
<details>
 <summary> Click to expand </summary>
 
```js
# datetime features
import datetime
import time
 
current_date = datetime.datetime.now()
 
print (type(current_date))
print (current_date)

tday = datetime.date.today()
print(tday.weekday()))
print(tday.isoweekday()))

tdelta = datetime.timedelta(days=7)
print (tday + tdelta)

my_custom_date = datetime.datetime(2000, 12, 12, 14, 59, 59)
print (type(current_date))
print (my_custom_date)

t1 = datetime.datetime.now()
print (t1)
time.sleep(5)
t2 = datetime.datetime.now()
print (t2)
dif = t2 - t1
print (dif)
print (type(dif))

from datetime import datetime as dt
 
now = dt.now()
print (now)
 
# printing date in a custom format
my_now = now.strftime('%A, %d %B %Y')
print (my_now)
 
# constructing a datetime object from a string
str_date = "22/03/2012 - 09:57"
new_date = dt.strptime(str_date, "%d/%m/%Y - %H:%M")
print (new_date)
print (type(new_date))
```

</details>
