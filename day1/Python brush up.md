# Python Basics

## Type Casting

Type casting is the process of converting one data type into another.

### Examples

```python
x = "10"

num = int(x)      # String -> Integer
flt = float(x)    # String -> Float
txt = str(10)     # Integer -> String
```

---

## Taking Multiple Inputs

### Using `map()`

```python
a, b = map(int, input("Enter two numbers: ").split())
```

### How it works

1. `input()` takes input as a string.
	
2. `.split()` separates values by spaces.
    
3. `map(int, ...)` converts each value to an integer.
    
4. Values are assigned to `a` and `b`.


**Example Input**

```text
10 20
```

**Output**

```python
a = 10
b = 20
```

---

# Bitwise Operators

Bitwise operators work directly on the binary representation of numbers.

|Operator|Meaning|
|---|---|
|`~`|NOT|
|`&`|AND|
|`\|`|OR|
|`^`|XOR|
|`<<`|Left Shift|
|`>>`|Right Shift|

---

## Left Shift (`<<`)

Shifts bits to the left.

### Formula

```text
x << y = x × 2^y
```

### Example

```python
10 << 2
```

Binary:

```text
10  = 1010
1010 << 2
101000
```

Result:

```text
40
```

### Pattern

```text
10 << 1 = 20
10 << 2 = 40
10 << 3 = 80
10 << 4 = 160
```

---

## Right Shift (`>>`)

Shifts bits to the right.

### Formula

```text
x >> y = floor(x / 2^y)
```

### Example

```python
10 >> 1
```

Binary:

```text
1010 >> 1
0101
```

Result:

```text
5
```

### Pattern

```text
10 >> 1 = 5
10 >> 2 = 2
10 >> 3 = 1
```

---

## XOR (`^`)

### Rule

- Same bits → `0`
    
- Different bits → `1`
    

### Truth Table

```text
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

### Important Property

A number XORed with itself becomes zero.

```python
7 ^ 7
```

Binary:

```text
111
111
---
000
```

Result:

```text
0
```

### Even/Odd Number of 1s

```text
Even number of 1s  -> 0
Odd number of 1s   -> 1
```

---

# Assignment Operators

Shortcut operators used to update values.

| Operator | Equivalent   |
| -------- | ------------ |
| `+=`     | `a = a + b`  |
| `-=`     | `a = a - b`  |
| `*=`     | `a = a * b`  |
| `/=`     | `a = a / b`  |
| `%=`     | `a = a % b`  |
| `//=`    | `a = a // b` |
| `**=`    | `a = a ** b` |

### Example

```python
x = 10

x += 5   # 15
x -= 2   # 13
x *= 3   # 39
```

# Operator Precedence

> [!NOTE]
> Similar to BODMAS but includes programming operators.

## Order (Highest → Lowest)

1. `()`
2. `**`
3. Unary `+`, `-`
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. Comparison (`<`, `>`, `<=`, `>=`, `==`, `!=`) 
7. ``` python
   5 + 2 > 3 // 7 > 3 
   ```
8. `not`
9. `and`
10. `or`





