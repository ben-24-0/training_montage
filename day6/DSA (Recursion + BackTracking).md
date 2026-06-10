#dsa

---
``` python
def add (a,b): # a,b is called parameters
	return a+b


def main():
n,m =5,13
	x= add(n,m) # n,m is known as arguments
```

# Types of Function Arguments
[Types of Function Arguments](https://www.geeksforgeeks.org/python/python-functions/)
![[Pasted image 20260608092737.png]]
## default arguments
```python
def myFun(x,y=10): #make sure the default parameter is in end

```
## Keyword Arguments
```PYTHON
# pass values using parameter names, so argument order does not matter.

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')
```
## Positional Arguments
```PYTHON
# values are assigned to parameters based on their order in the function call.
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("Case-2:")
nameAge(27, "Olivia")
```
## Arbitary Arguments
```python
##allow functions to accept multiple values. This is done using two special symbols:

## *args collects extra positional arguments as a tuple.
  #  **kwargs collects extra keyword arguments as a dictionary 
	def myFun(*args, **kwargs):
	    print("Non-Keyword Arguments (*args):")
	    for arg in args:
	        print(arg)
	
	    print("Keyword Arguments (**kwargs):")
	    for key, value in kwargs.items():
	        print(f"{key} == {value}")
	
	myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks') 
```


## ## Pass by Reference and Pass by Value


Variables refer to objects. Function behavior depends on whether the object is mutable or immutable.

- Mutable objects like lists can be modified inside functions.
- Immutable objects like integers and strings remain unchanged.
```python
def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)
```
>Output :
>[20, 11, 12, 13]
>10

>Explanation:

**myFun(x) modifies the first element of the list and lists are mutable, so the original list changes**
**myFun2(x) assigns a new value to x. Integers are immutable, so the original value of a remains unchanged**


>[!TIP]  uses pass-by-object-reference, where functions receive references to objects instead of actual copies.

# Recursion
[ Introduction to Recursion](https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/)


##  tail and non-tail recursion?**

A recursive function is tail recursive when a recursive call is the last thing executed by the function.


# Recursion Printing Patterns

> [!info] Core Idea
> Recursion has **2 phases**:
>
> 🟢 **PUSH Phase** → Going deeper into recursive calls  
> 🔴 **POP Phase** → Returning from recursive calls
>
> ```python
> print("Before")
> fun(...)
> print("After")
> ```
>
> - `Before` runs during **PUSH**
> - `After` runs during **POP**

---

# Pattern 1️⃣ : `1 → n → 1`

### Output (`n = 3`)

```text
1 2 3 2 1
```

### Code

```python
def fun(n, i=1):
    print(i, end=" ")

    if i < n:
        fun(n, i+1)
        print(i, end=" ")
```

---

## 🟢 PUSH Phase

```text
fun(3,1)
 └─ fun(3,2)
     └─ fun(3,3)
```

Values printed before recursion:

```text
1 2 3
```

---

## 🔴 POP Phase

Stack starts returning:

```text
fun(3,3)
 ↑
fun(3,2) → print 2
 ↑
fun(3,1) → print 1
```

Values printed after recursion:

```text
2 1
```

---

## ✅ Final Output

```text
1 2 3 2 1
```

---

## Stack View

```text
PUSH
----
1
2
3

POP
---
2
1
```

---

# Pattern 2️⃣ : `n → 1 → n`

### Output (`n = 3`)

```text
3 2 1 2 3
```

### Code

```python
def fun(n):
    print(n, end=" ")

    if n > 1:
        fun(n-1)
        print(n, end=" ")
```

---

## 🟢 PUSH Phase

```text
fun(3)
 └─ fun(2)
     └─ fun(1)
```

Values printed before recursion:

```text
3 2 1
```

---

## 🔴 POP Phase

Stack starts returning:

```text
fun(1)
 ↑
fun(2) → print 2
 ↑
fun(3) → print 3
```

Values printed after recursion:

```text
2 3
```

---

## ✅ Final Output

```text
3 2 1 2 3
```

---

## Stack View

```text
PUSH
----
3
2
1

POP
---
2
3
```

---

# 🧠 Master Rule

> [!tip]
> ### Code Position Determines Execution Time
>
> ```python
> def fun(n):
>     # PUSH
>     print(n)
>
>     fun(...)
>
>     # POP
>     print(n)
> ```
>
> Everything **before** the recursive call runs during **PUSH**.
>
> Everything **after** the recursive call runs during **POP**.

---

# 🎯 Visual Memory Trick

```text
Before Recursion  = Going Down ⬇️

After Recursion   = Coming Up ⬆️
```

```text
1 → 2 → 3
↓   ↓   ↓
⬆️  ⬆️  ⬆️
3 ← 2 ← 1
```

Whenever you're confused, draw the stack:

```text
PUSH ↓↓↓
BASE
POP ↑↑↑
```

That's the entire secret behind recursion printing questions.


## Returning a value from base call
###  Recursive Return Values and the Call Stack

```python
def rec(n):
    if n == 1:
        return 200

    rec(n - 1)
    print(n, end=" ")

x = rec(5)
print(x)
```

### Call Phase (PUSH)

```text
rec(5)
 └─ rec(4)
     └─ rec(3)
         └─ rec(2)
             └─ rec(1)
```

### Base Case

```python
if n == 1:
    return 200
```

So:

```text
rec(1) → 200
```

### Return Phase (POP)

The value `200` is returned to `rec(2)`:

```python
rec(1)      # returns 200
print(2)
```

Output:

```text
2
```

But there is **no return statement** after the print.

Python automatically does:

```python
return None
```

So:

```text
rec(2) → None
```

The same thing happens for every remaining call:

```text
rec(3) receives None
prints 3
returns None

rec(4) receives None
prints 4
returns None

rec(5) receives None
prints 5
returns None
```

### Complete Flow

```text
rec(1) → 200
          ↓ (ignored)

rec(2) prints 2 → returns None
          ↓

rec(3) prints 3 → returns None
          ↓

rec(4) prints 4 → returns None
          ↓

rec(5) prints 5 → returns None
```

### Stack View

```text
PUSH:
rec(5)
rec(4)
rec(3)
rec(2)
rec(1)

POP:
rec(1) → 200
rec(2) → None
rec(3) → None
rec(4) → None
rec(5) → None
```

### Final Output

```text
2 3 4 5
None
```

### Why?

The value `200` reaches only `rec(2)`.
	
Since `rec(2)` does not return that value, it is discarded.

```text
200
 ↓
rec(2) ❌ doesn't return it
 ↓
None propagates upward
```

### Rule

A return value travels back up the recursion stack **only if every recursive call returns it**.

```python
def rec(n):
    if(n==1):
        print(1)
        t=200
        return t
    t=rec(n-1)
    print(n,end=" ")
    return t
    
x=rec(5)
print(x)
```

or

```python
t = rec(n - 1)
return t
```

Otherwise, Python reaches the end of the function and returns:

```python
None
```

## [Reduce a number to 1 by performing given operations](https://www.geeksforgeeks.org/dsa/reduce-a-number-to-1-by-performing-given-operations/)
```python
	def countways(n):
	    if (n == 1):
	        return 0;
	    elif (n % 2 == 0):
	        return 1 + countways(n / 2);
	    else:
	        return 1 + min(countways(n - 1), 
	                    countways(n + 1));
	
	# Driver code
	n = 15;
	print(countways(n));

					#                 or.
---------------------------------------------------------------------------------
		def fun (n,i=0):
		    if n==1:
		        x=i
		        return x
		    elif n%2==0:
		        x=fun(n//2,i+1)
		    else:
		        x=min(fun(n-1,i+1),fun(n+1,i+1))
		    return x
		
		
		
		print(fun(int(input())))
```

# 💡 Integer Replacement — Mathematical Observation

## Key Idea

For an odd number `n`, we have two choices:

```text
n → n - 1
n → n + 1
```

Both results become even numbers.

The goal is to choose the option that creates **more trailing zeros in binary**, allowing more divisions by `2`.

---

## Observation

Every odd number satisfies:

```python
n % 4 == 1
```

or

```python
n % 4 == 3
```

### Case 1: `n % 4 == 1`

Example:

```text
5  % 4 = 1
9  % 4 = 1
13 % 4 = 1
```

Subtracting `1` produces a multiple of `4`:

```text
5  → 4
9  → 8
13 → 12
```

Since multiples of `4` can be divided by `2` repeatedly:

```text
5 → 4 → 2 → 1
```

✅ Prefer **decrement**

---

### Case 2: `n % 4 == 3`

Example:

```text
7  % 4 = 3
11 % 4 = 3
15 % 4 = 3
```

Adding `1` produces a multiple of `4`:

```text
7  → 8
11 → 12
15 → 16
```

This often gives more divisions by `2`:

```text
7 → 8 → 4 → 2 → 1
```

✅ Prefer **increment**

---

## Special Case

For:

```text
n = 3
```

Although:

```text
3 % 4 == 3
```

Incrementing is worse:

```text
3 → 4 → 2 → 1   (3 steps)
```

than

```text
3 → 2 → 1       (2 steps)
```

So handle `3` separately.

---

## Algorithm

``` python
def countSteps(n):
    
    count = 0
    while (n > 1):
        count += 1

        # num even, divide by 2
        if (n % 2 == 0):
            n //= 2

        # num odd, n%4 == 1 
        # or n==3(special edge case), 
        # decrement by 1
        elif (n % 4 == 1 or n == 3):
            n -= 1

        # num odd, n%4 == 3, increment by 1
        else:
            n += 1

    return count

# Driver code
if __name__ == "__main__":
    
    n = 15

    # Function call
    print(countSteps(n))

# This code is contributed by chitranayal```
---

## Binary Intuition

```text
7  = 111₂
8  = 1000₂   ← many trailing zeros

15 = 1111₂
16 = 10000₂  ← many trailing zeros
```

Adding `1` to numbers ending in many `1`s often creates a power of two, leading to several divisions by `2`.

---

> [!tip]
> For odd numbers:
>
> - `n % 4 == 1` → `n -= 1`
> - `n % 4 == 3` → `n += 1`
> - Exception: `n == 3` → `n -= 1`
>
> This greedy choice yields the minimum number of operations.

[

# scheme - Fibonacci Tree-Recursion in Structure 
![[Pasted image 20260608152746.png]]
```python
def nth_fibonacci(n):
    
    # base case
    if n <= 1:
        return n
      
    # sum of the two preceding 
    # Fibonacci numbers
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

n = 5
result = nth_fibonacci(n)
print(result)

```

# BackTracking
## Wildfire Method (DFS on Grids)

> [!info]
> The **Wildfire Method** is a DFS technique used to traverse and mark an entire connected component in a grid.
>
> Start a fire at one cell, and let it spread in all four directions until no connected land remains.

---

### Visualizing the Fire

Initial grid:

```text
1 1 1 1
1 0 0 0
0 0 1 1
1 0 0 0
```

Start fire at `(0,0)`:

```python
wildfire(grid, 0, 0)
```

The fire spreads through every connected `1`:

```text
2 2 2 2
2 0 0 0
0 0 1 1
1 0 0 0
```

Everything reachable from `(0,0)` has been burned.

---

### DFS Implementation

```python
def wildfire(grid, i, j):

    if (
        i < 0 or i >= len(grid) or
        j < 0 or j >= len(grid[0]) or
        grid[i][j] != 1
    ):
        return

    grid[i][j] = 2

    wildfire(grid, i + 1, j)  # Down
    wildfire(grid, i - 1, j)  # Up
    wildfire(grid, i, j + 1)  # Right
    wildfire(grid, i, j - 1)  # Left
```

---

### How the Fire Spreads

```text
        (i-1,j)
            ↑
            |
(i,j-1) ← (i,j) → (i,j+1)
            |
            ↓
        (i+1,j)
```

The current cell burns first, then spreads to its four neighbors.

---

### Example

```python
matrix = [
    [1,1,1,1],
    [1,0,0,0],
    [0,0,1,1],
    [1,0,0,0]
]

wildfire(matrix, 0, 0)
```

Result:

```text
2 2 2 2
2 0 0 0
0 0 1 1
1 0 0 0
```

---

### Common Mistake

After burning the first component:

```text
2 2 2 2
2 0 0 0
0 0 1 1
1 0 0 0
```

Remaining `1`s:

```text
(2,2) (2,3) (3,0)
```

Counting remaining `1`s gives:

```text
3
```

But that is **not** the number of islands.

---

### Counting Islands Correctly

```python
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):

        if matrix[i][j] == 1:
            count += 1
            wildfire(matrix, i, j)

print(count)
```

Output:

```text
2
```

Why?

```text
Island 1:
(2,2) ── (2,3)

Island 2:
(3,0)
```

Two separate wildfire calls were needed.

---

### Core Pattern

```text
Find an unvisited 1
        │
        ▼
Count the component
        │
        ▼
Burn the entire component
        │
        ▼
Continue scanning
```

---

### Mental Model

> [!tip]
>
> Flood Fill:
>
> ```text
> 1 → New Color
> ```
>
> Wildfire:
>
> ```text
> 1 → Burned (2 or 0)
> ```
>
> The DFS is identical.
>
> Only the action performed on each visited cell changes.

---

### Complexity

| Metric | Complexity                   |
| ------ | ---------------------------- |
| Time   | `O(m × n)`                   |
| Space  | `O(m × n)` (recursion stack) |

---

### Takeaway

```text
One Wildfire Call
        =
One Connected Component
        =
One Island
```

Whenever you need to explore an entire region of connected cells, think:

```text
Start a fire.
Let DFS spread it.
Mark everything it touches.
```

## Flood Fill (DFS on Grids)

> [!info]
> Flood Fill starts from a source cell and spreads to all connected cells having the same color.
>
> Instead of burning cells, we **repaint** them.

---

### Visualizing the Fill

Initial image:

```text
1 1 1
1 1 0
1 0 1
```

Start at:

```python
sr = 1
sc = 1
color = 2
```

Original color:

```text
1
```

After filling:

```text
2 2 2
2 2 0
2 0 1
```

Only cells connected to `(1,1)` with the original color are changed.

---

### DFS Implementation

```python
def floodFill(image, sr, sc, color):

    old = image[sr][sc]

    if old == color:
        return image

    def dfs(r, c):

        if (
            r < 0 or r >= len(image) or
            c < 0 or c >= len(image[0]) or
            image[r][c] != old
        ):
            return

        image[r][c] = color

        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    dfs(sr, sc)

    return image
```

---

### How the Fill Spreads

```text
        (r-1,c)
            ↑
            |
(r,c-1) ← (r,c) → (r,c+1)
            |
            ↓
        (r+1,c)
```

Each painted cell tries to paint its four neighbors.

---

### DFS Pattern

```text
Out of bounds?
        ↓
Return

Different color?
        ↓
Return

Paint current cell
        ↓
Visit 4 neighbors
```

---

### Example Walkthrough

Starting image:

```text
1 1 1
1 1 0
1 0 1
```

Start:

```python
dfs(1, 1)
```

Traversal:

```text
(1,1)
   │
   ├── (0,1)
   │      ├── (0,0)
   │      └── (0,2)
   │
   └── (1,0)
          └── (2,0)
```

Cells painted:

```text
(1,1)
(0,1)
(0,0)
(0,2)
(1,0)
(2,0)
```

---

### Common Pitfall

Without this check:

```python
if old == color:
    return image
```

Example:

```python
old = 2
color = 2
```

You repaint a cell with the same color and keep revisiting it forever.

Always handle this case first.

---

---

### Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | `O(m × n)` |
| Space  | `O(m × n)` |

Each cell is visited at most once.

---

## Flood Fill vs Wildfire

| Flood Fill         | Wildfire                  |
| ------------------ | ------------------------- |
| Repaint cells      | Burn cells                |
| `old → new_color`  | `1 → 0` or `1 → 2`        |
| Preserve component | Destroy component         |
| Used for coloring  | Used for counting islands |

The DFS traversal is exactly the same.

Only the operation on each visited cell changes.


## Takeaway

```text
Find a cell
      ↓
Paint it
      ↓
Spread to matching neighbors
      ↓
Repeat recursively
```

Flood Fill is simply:

```text
DFS + Color Replacement
```

>**LeetCode:** https://leetcode.com/problems/flood-fill/


## Maze Path (Down + Right)

## Idea

Starting from `(0,0)`, find all possible paths to `(n,n)`.

Allowed moves:

```text
D = Down
R = Right
```

Blocked cells:

```text
0 = Cannot visit
1 = Can visit
```

---

## Example Grid

```python
grid = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
```

Visual:

```text
S 1 0 0
1 1 1 0
0 1 1 1
0 0 1 E
```

```text
S = Start
E = End
```

---

## Recursive Idea

At every cell:

```text
Can move Down?
    ↓
Recurse

Can move Right?
    ↓
Recurse
```

When destination is reached:

```text
Print the path
```

---

## Code

```python
def maze(grid, path, i, j):

    if i == n and j == n:
        print(path)
        return

    if i + 1 <= n and grid[i+1][j] == 1:
        maze(grid, path + 'D', i + 1, j)

    if j + 1 <= n and grid[i][j+1] == 1:
        maze(grid, path + 'R', i, j + 1)


n = len(grid) - 1

maze(grid, "", 0, 0)
```

---

## Recursion Tree

```text
(0,0)
   |
   D
   |
(1,0)
 /   \
D     R
|     |
(2,0) (1,1)
```

Each recursive call explores one possible choice.

---

## Output

```text
DRDRR
DRRDR
```

---

## Path Visualization

### DRDRR

```text
S
↓
↓
→
↓
→
→
E
```

### DRRDR

```text
S
↓
→
→
↓
→
↓
E
```

---

## Base Case

```python
if i == n and j == n:
    print(path)
    return
```

Reached destination.

Print the accumulated path.

---

## Pattern

```text
Current Cell
     │
     ▼
Try Down
     │
     ▼
Try Right
     │
     ▼
Destination?
     │
     ▼
Print Path
```

---

## Complexity

Let `P` be the number of valid paths.

```text
Time  : O(P)
Space : O(path length)
```

Every valid path is explored exactly once.

---

## Key Observation

```text
path + 'D'
```

means:

```text
"I moved Down to reach this cell"
```

```text
path + 'R'
```

means:

```text
"I moved Right to reach this cell"
```

The string itself stores the complete route from Start to End.
