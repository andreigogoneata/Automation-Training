#### 0.Using the list indexes, modify the value from a list within a certain index: lst=[1, 2, "penguin", "tiger"]
 <details> <summary> Result </summary>

  ```js
  list[1] = 4
  list[3] = "lion"
  ```
  </details>

#### 1.Use append and extend to add new elements in the lst list: lst=[1, 2, "penguin", "tiger"]. Print the length of the list

 <details> <summary> Result </summary>

  ```js
lst.append('animal')
lst.extend(['frog'])
print len(lst)

  ```
  </details>


#### 2.Write a Python program to clone or copy a list.
  <details> <summary> Result </summary>

  ```js
  original_list = [10, 22, 44, 23, 4]
  new_list = list(original_list)
  print(original_list)
  print(new_list)
  ```
  </details>
  
#### 3.Given a list of ints length 3, change the list with the elements in reverse order, so [1, 2, 3] becomes [3, 2, 1].
<details> <summary> Result </summary>

```js
list = [1,2,3]
list.reverse()
print list

rever = list[::-1]
print rever

 ```
 
  </details>
  
#### 4.Given a list within a list with length 6, create three other lists named: first, middle, last, each containing 2 elements: elements = [1, 2, 3 ,4, 5, 6]

<details> <summary> Result </summary>

```js
elements = [1, 2, 3 ,4, 5, 6]
first = elements[0:2]
middle = elements[2:4]
last = elements[4:6]
print first, middle, last
 ```
 
 </details>


#### 5.Given a list within a list with length 3, compute the sum of the elements: lst = [1, 2, [3, 4], 5] sum = 15
<details> <summary> Result </summary>

```js
lst = [1, 2, [3, 4], 5]
s = lst[0] + lst[1] + lst[2][0] + lst[2][1] + lst[3]
print s
 ```
 
  </details>

#### 6.Given a list within a list with length 5, create a new list with the first and last element of the original
<details> <summary> Result </summary>

```js
nums = [1,2,3,4,5]
lst = nums[:1] + nums[-1:]
print lst
 ```
 
  </details>
  
  #### 7.Given a list with at least 3 elements, swap the first and the last elements in the list
<details> <summary> Result </summary>

```js
nums = [1,2,3,4,5]
temp = nums[0]
nums[0] = nums[len(nums)-1]
nums[len(nums)-1] = temp

 ```
 
  </details>
  
  
  
