## Stack
## MonoTonic Stack
### [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
![[Pasted image 20260609171332.png]]


```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        stack= []
        for curr in nums2:
            while stack and stack[-1]<curr:
                ele = stack.pop()
                d[ele]=curr
            stack.append(curr)
        while(stack):
            d[stack.pop()]=-1
        print(d)
        res =[]
        for i in nums1:
            res.append(d[i])
        return res

        
```
# 496. Next Greater Element I

## Intuition

Instead of finding the next greater element for each number in `nums1` separately, we first process the entire `nums2` array and store the answer for every element in a hashmap.

The stack keeps elements whose next greater element has not been found yet.

---

## Algorithm

1. Traverse `nums2`.
2. For each `curr`:
   - While the stack is not empty and `curr` is greater than the top element:
     - Pop the element.
     - Store `curr` as its next greater element in the hashmap.
   - Push `curr` onto the stack.
3. After traversal, elements remaining in the stack have no greater element on their right, so map them to `-1`.
4. Build the result for `nums1` using the hashmap.

---

## Dry Run

### Input

```python
nums1 = [4,1,2]
nums2 = [1,3,4,2]
```

### Step 1: Process `nums2`

| Current | Stack Before | Action | HashMap |
|----------|-------------|---------|---------|
| 1 | [] | Push 1 | {} |
| 3 | [1] | 3 > 1 → Pop 1, d[1]=3 | {1:3} |
| 4 | [3] | 4 > 3 → Pop 3, d[3]=4 | {1:3, 3:4} |
| 2 | [4] | Push 2 | {1:3, 3:4} |

Stack after traversal:

```python
[4, 2]
```

These elements have no greater element to their right:

```python
d[2] = -1
d[4] = -1
```

Final hashmap:

```python
{
    1: 3,
    3: 4,
    2: -1,
    4: -1
}
```

---

## Build Answer

For each element in `nums1`:

```python
4 -> -1
1 -> 3
2 -> -1
```

Result:

```python
[-1, 3, -1]
```

---

## Key Observation

Whenever a larger element `curr` arrives:

```python
while stack and stack[-1] < curr:
```

`curr` becomes the **next greater element** for all smaller elements on the top of the stack.

This works because:

- Elements are pushed once.
- Elements are popped once.

So each element is processed at most two times.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element is pushed and popped at most once.

### Space Complexity

```text
O(n)
```

For the stack and hashmap.

---

## Code

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []

        for curr in nums2:
            while stack and stack[-1] < curr:
                ele = stack.pop()
                d[ele] = curr
            stack.append(curr)

        while stack:
            d[stack.pop()] = -1

        return [d[x] for x in nums1]
```


[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
# 739. Daily Temperatures

## Intuition

For each day, we need to find the **next day with a higher temperature**.

A brute force approach would check every day to the right, resulting in **O(n²)** time.

Instead, we use a **monotonic decreasing stack** that stores indices of days whose warmer day hasn't been found yet.

---

## Key Idea

The stack stores **indices**, not temperatures.

Why?

Because the answer requires:

```python
future_day - current_day
```

which means we need positions, not just values.

---

## Algorithm

Traverse the array from **right to left**.

For each day:

1. Remove all days with temperatures less than or equal to the current temperature.
2. If the stack is not empty, the top of the stack is the next warmer day.
3. Store the difference in indices.
4. Push the current index onto the stack.

---

## Dry Run

### Input

```python
temperatures = [73,74,75,71,69,72,76,73]
```

### Start from the end

| i | Temp | Stack (indices) | Next Warmer Day | Result |
|---|------|----------------|-----------------|--------|
| 7 | 73 | [] | None | 0 |
| 6 | 76 | [7] → pop 7 | None | 0 |
| 5 | 72 | [6] | 6 | 1 |
| 4 | 69 | [6,5] | 5 | 1 |
| 3 | 71 | [6,5,4] → pop 4 | 5 | 2 |
| 2 | 75 | [6,5,3] → pop 3,5 | 6 | 4 |
| 1 | 74 | [6,2] | 2 | 1 |
| 0 | 73 | [6,2,1] | 1 | 1 |

Final Answer:

```python
[1,1,4,2,1,1,0,0]
```

---

## Why Pop Smaller Temperatures?

```python
while stk and temperatures[stk[-1]] <= temperatures[i]:
    stk.pop()
```

If a future temperature is smaller (or equal) than the current one, it can never be the answer.

Example:

```python
Current = 75
Future  = 72
```

Since `72` is not warmer than `75`, it is useless and removed.

---

## Example

```python
temperatures = [75,72,76]
```

When processing `75`:

```python
75 > 72
```

So `72` is popped because it cannot be the next warmer day.

The next warmer day is `76`.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each index is:

- Pushed once
- Popped once

---

### Space Complexity

```text
O(n)
```

For the stack.

---

## Code

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        res = [0] * n

        for i in range(n - 1, -1, -1):

            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()

            if stk:
                res[i] = stk[-1] - i

            stk.append(i)

        return res
```

---

## Pattern

This is a classic **Next Greater Element** problem.

The only difference is:

- Instead of storing the next greater value,
- We store the **distance to the next greater value**.

```text
Next Greater Element
        ↓
Daily Temperatures
```

Use a **Monotonic Decreasing Stack** whenever you see:

- Next Greater Element
- Next Warmer Day
- Stock Span
- Buildings with Sunset View
- Monotonic Stack pattern questions