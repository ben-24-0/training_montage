![[Dislike3.png]]

```python
t = int(input())

  

queries = []

for _ in range(t):

queries.append(int(input()))

  

valid = []

  

i = 1

while len(valid) <= 1000:
	if i % 3 != 0 and i % 10 != 3:
	valid.append(i)

	i += 1

  

for k in queries:
	print(valid[k-1],end=" ")

  

# t = int(input())
# for i in range (t):
# n = int(input())
# i=0
# k=1

# while(1):
	# if i%3!=0 and i%10!=3:
	# if n==k:
	# print(i)
	# break
	# k=k+1
	# i=i+1
```

# List vs Array

## List

- Mutable
    
- Dynamic size (can grow/shrink)
    
- Elements need not be stored contiguously in memory
    
- Supports built-in methods like `append()`, `remove()`, `insert()`, etc.
    
- Slightly higher memory overhead due to dynamic resizing and references
    

# Python List Methods

```python
nums = [10, 20, 30]
```

| Method               | Example                   | Description                        |
| -------------------- | ------------------------- | ---------------------------------- |
| `append()`           | `nums.append(40)`         | Add element to the end             |
| `insert()`           | `nums.insert(1, 15)`      | Insert element at index            |
| `extend()`           | `nums.extend([40, 50])`   | Add multiple elements              |
| `remove()`           | `nums.remove(20)`         | Remove first occurrence of value   |
| `pop()`              | `nums.pop()`              | Remove and return last element     |
| `pop(index)`         | `nums.pop(1)`             | Remove and return element at index |
| `clear()`            | `nums.clear()`            | Remove all elements                |
| `index()`            | `nums.index(30)`          | Return index of element            |
| `count()`            | `nums.count(10)`          | Count occurrences                  |
| `sort()`             | `nums.sort()`             | Sort in ascending order            |
| `sort(reverse=True)` | `nums.sort(reverse=True)` | Sort in descending order           |
| `reverse()`          | `nums.reverse()`          | Reverse the list                   |
| `copy()`             | `nums.copy()`             | Create a shallow copy              |

## Common Operations

### Length
```python
len(nums)
```

### Check Existence
```python
20 in nums
20 not in nums
```

```python

### Modifying a List While Iterating

```python
li = [1,2,3,4,5,6,7]

for i in li:
    li.remove(i)

print(li)
```

Output:

```python
[2, 4, 6]
```

When an element is removed, the remaining elements shift left, causing some elements to be skipped.

### Alternatives

```python
for i in li[:]:
    li.remove(i)
```

```python
while li:
    li.pop()
```

```python
li = []
```
```

### Slicing
```python
nums[1:4]
```

```python
nums[:3]
```

```python
nums[::2]
```

### Concatenation
```python
a = [1, 2]
b = [3, 4]

c = a + b
```

### Repetition
```python
nums = [1, 2]

nums * 3
```

## Traversing a List

### For Each Element
```python
for num in nums:
    print(num)
```

### Using Index
```python
for i in range(len(nums)):
    print(nums[i])
```

### Using enumerate()
```python
for index, value in enumerate(nums):
    print(index, value)
```

## List Comprehension

### Create a New List
```python
squares = [x * x for x in range(5)]
```

### With Condition
```python
evens = [x for x in range(10) if x % 2 == 0]
```

## Useful Built-in Functions

```python
max(nums)
```

```python
min(nums)
```

```python
sum(nums)
```

```python
sorted(nums)
```

```python
any(nums)
```

```python
all(nums)
```


## Array

- Fixed size (traditional arrays)
    
- Stores elements in contiguous memory locations
    
- More memory efficient
    
- Faster random access using indexing
    
- Best suited when size is known beforehand
    

---

## Why Does Array Indexing Start at 0?

> [!NOTE]  
> Array indexing starts from `0` because the index represents the **offset from the starting memory address**.

Formula:

```text
Address of arr[i] = Base Address + (i × Size of Element)
```

Thus:

```text
arr[0] -> Base Address + 0
arr[1] -> Base Address + 1 × Size
arr[2] -> Base Address + 2 × Size
```

The first element is at an offset of `0`, hence indexing starts at `0`.

---

## Quick Comparison

| *Feature*            | *List*           | *Array*          |
| ------------------ | -------------- | -------------- |
| Size               | Dynamic        | Fixed          |
| Memory             | Less efficient | More efficient |
| Storage            | Non-contiguous | Contiguous     |
| Insertion/Deletion | Easier         | Costly         |
| Access by Index    | O(1)           | O(1)           |
| Cache Performance  | Lower          | Better         |





> [!TOP]
> 


# Python List Methods

| Method               | Description                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `append(x)`          | Adds `x` to the end of the list. Modifies the original list. Time Complexity: **O(1)**                                                                       |
| `insert(i, x)`       | Inserts `x` at index `i`. Existing elements shift right. Time Complexity: **O(n)**                                                                           |
| `extend(iterable)`   | Adds all elements from another iterable (list, tuple, set, etc.) to the end of the list. Time Complexity: **O(k)** where `k` is the number of added elements |
| `remove(x)`          | Removes the first occurrence of `x`. Raises `ValueError` if `x` is not found. Time Complexity: **O(n)**                                                      |
| `pop()`              | Removes and returns the last element. Raises `IndexError` if the list is empty. Time Complexity: **O(1)**                                                    |
| `pop(i)`             | Removes and returns the element at index `i`. Elements after `i` shift left. Time Complexity: **O(n)**                                                       |
| `clear()`            | Removes all elements from the list, making it empty. Time Complexity: **O(n)**                                                                               |
| `index(x)`           | Returns the index of the first occurrence of `x`. Raises `ValueError` if not found. Time Complexity: **O(n)**                                                |
| `count(x)`           | Returns the number of times `x` appears in the list. Time Complexity: **O(n)**                                                                               |
| `sort()`             | Sorts the list in ascending order. Modifies the original list. Uses Timsort. Time Complexity: **O(n log n)**                                                 |
| `sort(reverse=True)` | Sorts the list in descending order. Modifies the original list. Time Complexity: **O(n log n)**                                                              |
| `reverse()`          | Reverses the order of elements in-place. Does not sort. Time Complexity: **O(n)**                                                                            |
| `copy()`             | Creates a shallow copy of the list. Nested mutable objects are still shared. Time Complexity: **O(n)**                                                       |

## append()

```python
nums = [1, 2, 3]
nums.append(4)

print(nums)
# [1, 2, 3, 4]
```

Adds a single element to the end of the list.

---

## insert()

```python
nums = [1, 2, 3]
nums.insert(1, 100)

print(nums)
# [1, 100, 2, 3]
```

Inserts an element at a specific index.

Elements from that index onward are shifted right.

---

## extend()

```python
nums = [1, 2, 3]
nums.extend([4, 5])

print(nums)
# [1, 2, 3, 4, 5]
```

Adds multiple elements from another iterable.

```python
nums.append([4, 5])
# [1, 2, 3, [4, 5]]
```

```python
nums.extend([4, 5])
# [1, 2, 3, 4, 5]
```
>[!faq] anything other than an iterable can raise an error
>	eg nums.extend(47)


---

## remove()

```python
nums = [1, 2, 3, 2]
nums.remove(2)

print(nums)
# [1, 3, 2]
```

Removes only the first occurrence of the value.

---

## pop()

```python
nums = [1, 2, 3]

x = nums.pop()

print(x)
# 3

print(nums)
# [1, 2]
```

Removes and returns the last element.

---

## pop(index)

```python
nums = [1, 2, 3]

x = nums.pop(1)

print(x)
# 2

print(nums)
# [1, 3]
```

Removes and returns the element at the given index.

---

## clear()

```python
nums = [1, 2, 3]
nums.clear()

print(nums)
# []
```

Removes all elements from the list.

---

## index()

```python
nums = [10, 20, 30]

print(nums.index(20))
# 1
```

Returns the index of the first matching element.

---

## count()

```python
nums = [1, 2, 2, 2, 3]

print(nums.count(2))
# 3
```

Counts how many times an element appears.

---

## sort()

```python
nums = [5, 1, 3, 2]
nums.sort()

print(nums)
# [1, 2, 3, 5]
```

Sorts the original list in ascending order.

---

## sort(reverse=True)

```python
nums = [5, 1, 3, 2]
nums.sort(reverse=True)

print(nums)
# [5, 3, 2, 1]
```

Sorts the original list in descending order.

---

## reverse()

```python
nums = [1, 2, 3, 4]
nums.reverse()

print(nums)
# [4, 3, 2, 1]
```

Reverses the current order of elements.

```python
[3, 1, 4]
```

becomes

```python
[4, 1, 3]
```

---

## copy()

```python
nums = [1, 2, 3]

new_nums = nums.copy()

print(new_nums)
# [1, 2, 3]
```

Creates a shallow copy.

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
# [1, 2, 3]

print(b)
# [1, 2, 3, 4]
```
#python #dsa