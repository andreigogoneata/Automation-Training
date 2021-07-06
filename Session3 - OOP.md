# Session 3
## OOP | Exceptions | Files in Python


## Classes

 - How to create a class
 - Constructors
 - Self parameter -> reference to the current instance of the class
 
```js
import socket

class Server:
    """ Holds all server related operations, regardless of the OS """
    def __init__(self, hostname, procs=2, mem=4):
        """ Constructor.
        Parameters:
            hostname <String> The server's hostname.
            procs: <Int> (optional) Number of processors.
            mem: <Int> (optional) GB of RAM.
        """
        self.hostname = hostname
        self.procs = procs
        self.total_mem = mem
 
        self._load = 0
 
        self._set_system_info()
 
    def print_server_information(self):
        """ Print all server information """
        print "\nServer info follows:"
        print "Hostname: %s" % self.hostname
        print "IP addr: %s" % self.ip
        print "Processor number: %s" % self.procs
        print "Mem: %s" % self.total_mem
        print "Server load: %s" % self._load
 
    def start_process(self, process_name):
        """ Start a new process on the server.
        Parameters:
            process_name: <String> The name of the process to start.
        Return:
            True/False
        """
        process_load = 10
        if process_name == "SA":
            process_load = 50
 
        server_load = self._load + process_load
        if server_load > 120:
            print "Server load is too high. Stop some processes first."
            return False
 
        self._load = server_load
 
        return True
 
    def _set_system_info(self):
        """ Retrieves additional information about this server."""
        self.ip = socket.gethostbyname(self.hostname)
 
 
if __name__ == "__main__":
    # Create object
    linux_server = Server("yahoo.com")
    linux_server.print_server_information()
 
    if linux_server.start_process("SA"):
        print "Started process successfully."
        linux_server.print_server_information()
    else:
        print "Unable to start this process."
    print dir(linux_server)
```

1. Create a class:
    PersonalData:
        + name
        + age
        + print_info()
 
2. Add several PersonalData objects to a list.
     - Find the oldest person
     - Sort the list alphabetically

```js
import random
 
 
 class PersonalData:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def print_info(self):
        print "Name: %s" % self.name
        print "age: %s" % self.age
 
if __name__ == "__main__":
    data_list = []
    for i in range(0, 10):
        data_list.append(PersonalData("Name%s" % random.randint(0, 100),
                                      random.randint(18, 65)))
    for p in data_list:
        p.print_info()
 
    print "Find oldest person"
    oldest = data_list[0]
    for data in data_list:
        if oldest.age < data.age:
            oldest = data
 
    oldest.print_info()
 
    data_list = sorted(data_list, key=lambda a: a.name)
    for data in data_list:
        data.print_info()
```

## Inheritance

```js
from example2 import Server
 
# class Server:
#    def __init__(self, hostname, procs=2, mem=4):
#        self.hostname = hostname
#        self.procs = procs
#        self.total_mem = mem
#        ...
 
 
class CoreServer(Server):
    def __init__(self, hostname):
        self.sa_release = "Isaac"
 
        Server.__init__(self, hostname)
 
    def start_process(self, process_name):
        print "CoreServer:start_process"
        return Server.start_process(self, process_name)
 
    def start_services(self):
        if self.start_process("SA"):
            print "Starting services on %s" % self.hostname
        else:
            print "Unable to start SA due to high server load."
 
 
core = CoreServer("hp.com")
print dir(core)
core.print_server_information()
 
core.start_services()
core.print_server_information()
```

- Special methods
- Overwrite default/built in methods

```js
class PersonalData:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __str__(self):
        return "name: %s " % self.name + "age: %s" % self.age
 
    def __cmp__(self, other):
        if self.name == other.name:
            return 0
        else:
            return 1
 
 
data1 = PersonalData("Titus", "25")
print data1
 
data2 = PersonalData("Titus", "25")
 
print data1 == data2
```
- Static variables and methods
- decorators, static, static methods

```js
class PersonalData:
    employee_id = 0
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
        PersonalData.employee_id += 1
 
    def print_info(self):
        print "name: %s" % self.name
        print "age: %s" % self.age
 
    @staticmethod
    def get_free_id():
        return PersonalData.employee_id + 1
 
 
print PersonalData.employee_id
data1 = PersonalData("Titus", "25")
print PersonalData.employee_id
print PersonalData.get_free_id()
```
 
## Encapsulation

 - restricted acces to methods and variables
 
```js
 class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

### change the price
c.__maxprice = 1000
c.sell()

### using setter function
c.setMaxPrice(1000)
c.sell()
```
 
## Polymorphism

 - abbility to use common methods for different classes
```js
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```

## Exceptions
- When an error(exception) occurs, Python will normally stop and generate an error message.
- try except block

- Block of code that will generate an error because x is not defined
```js
print(x)
```
- Block of code that will generate an exception because x is not defined

```js
try:
  print(x)
except:
  print("An exception occurred")
```

- Using else keyword if no errors are raised during block execution

```js
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```

- Raising an exception if a certain condition occurs
```js
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```


# Homework classes
<details>
1. Create a class to represent complex numbers. Implement methods to add,
subtract and multiply two complex numbers

2. a) Create a class Floor that represent the floor in a building:
Floor:
+ size: square meters inside the floor
+ floor_nr: the number this floor has

b) Create a class Building that represents a building a city:
Building:
+ name: the name of the building
+ base_size: squere meters of the ground floor
+ max_floor: the maximum number of floors
+ floors: a list of all the floors (list of Floor objects) inside
the building
+ add_floor(objFloor): adds a floor in the building you cannot add
a floor with a larger size over a floor with
a smaller size this method should also give the
floor it's floor_nr

c) Create a class City that represents a city with buildings and floors
City:
+ name: name of the city
+ size: the square meters of the city
+ buildings: a list of Building objects inside the city
+ add_building: adds a building inside the buildings list
make sure the total buildings base size is not
greater than 50% of size.

d) Create an algorithm that creates a city and populates it with buildings
until it reaches the maximum size, and populates the buildings with floors.

3. 21. Implement a simple 21 card game. Classes:
Deck
+ constructor: population, calls shuffle
+ shuffle()
+ draw_card()

Hand:
+ cards
+ sum

Player
+ draw()

AI Player
+ draw()

Card
+ color
+ value
_str_

Known facts:

there is no special rule when adding cards
the card values are from 1 to 11: A=1, J=Q=K=10
the AI stop when sum is higher than 18
you are asked to draw cards until you decide to stop.
 
</details>

# Homework methods and exceptions
<details>
</details>   
