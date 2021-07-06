#### 0.Initialize a dictionary, add a key and a value, print the length of the dict and the value within the key
 <details> <summary> Result </summary>

  ```js
drive_car = {}
drive_car['age'] = 18
drive_car['transmission'] = 'automatic'


print "There are" + str(len(drive_car)) + "elements in the dict"
print drive_car
  ```
  
  </details>
  
  #### 0.Print the elements from a nested dictionary that contains also lists
 <details> <summary> Result </summary>

  ```js
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], 
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
  'dicti': {'iron': 300, 'yellow': 4},
  (1, 2, 3, 4):[{'test':4}]
}

print inventory['gold']
print inventory['pouch']
print inventory['dicti']['iron']
print inventory['dicti']['yellow']
print inventory['1,2,3,4']
print inventory[1,2,3,4][0]['test']

                
  ```
  
  </details>
  
  
