# Linked Lists -(Foundation)
#dsa
## What is a Linked List?

A Linked List is a linear data structure where elements are stored in separate objects called **nodes**.

Unlike arrays:

- Arrays store elements in contiguous memory.
    
- Linked Lists store elements anywhere in memory.
    
- Nodes are connected using pointers/references.
    

---

## Visual Representation

```text
10      20      30      40

┌────┬────┐    ┌────┬────┐    ┌────┬────┐    ┌────┬────┐
│ 10 │ •──┼──► │ 20 │ •──┼──► │ 30 │ •──┼──► │ 40 │None│
└────┴────┘    └────┴────┘    └────┴────┘    └────┴────┘
```

Each box is a **Node**.

Each node contains:

1. Data
    
2. Reference to next node
    

---

## Why Do We Need Linked Lists?

### Array Problem

```python
arr = [10,20,30,40]
```

Insert 15 at index 1:

```python
[10,15,20,30,40]
```

All elements after index 1 must shift.

Cost:

```text
O(n)
```

---

### Linked List Solution

```text
10 -> 20 -> 30 -> 40
```

Insert 15:

```text
10 -> 15 -> 20 -> 30 -> 40
```

Only a few pointers change.

No shifting required.

---

# Anatomy of a Node

A node contains:

```python
data
next
```

Example:

```python
Node(
    data = 10,
    next = address_of_next_node
)
```

---

## Python Node Structure

```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
```

---

## Understanding self.next

```python
node1 = Node(10)
```

Memory:

```text
node1

data = 10
next = None
```

---

Create another node:

```python
node2 = Node(20)
```

Connect them:

```python
node1.next = node2
```

Now:

```text
10 -> 20 -> None
```

---

## Head Pointer

The first node is called the Head.

```text
head
 ↓
10 -> 20 -> 30 -> None
```

Without head, the entire list is lost.

Always remember:

```text
Head is the entry point to the Linked List.
```

---

# Traversal Logic

Question:

How do we visit every node?

Answer:

Start from head and keep moving using next.

```python
curr = head

while curr:
    print(curr.data)
    curr = curr.next
```

---

## Dry Run

```cpp
head
 ↓
10 -> 20 -> 30 -> None
```

Iteration 1:

```python
curr = 10
```

Print:

```text
10
```

Move:

```python
curr = curr.next
```

Now:

```python
curr = 20
```

---

Iteration 2:

```text
20
```

Move:

```python
curr = 30
```

---

Iteration 3:

```text
30
```

Move:

```python
curr = None
```

Loop stops.

---

# Golden Rule

Whenever you see a Linked List question:

```text
Start from head
Move using next
Stop at None
```

This single idea solves most Linked List problems.


# Linked Lists - (Implementation)
---
## Creating a Node

```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
```

---

## Creating Individual Nodes

```python
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
```

Connect them:

```python
 ```

Visualization:

```text
10 -> 20 -> 30 -> None
```

---

# Creating a Linked List Class

```python
class LinkedList:

    def __init__(self):
        self.head = None
```

Initially:

```text
head -> None
```

Empty list.

---

# Append Operation

Goal:

```text
10 -> 20 -> 30
```

Append:

```text
40
```

Result:

```text
10 -> 20 -> 30 -> 40
```

---

## Append Code

```python
def append(self,data):

    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    curr = self.head

    while curr.next:
        curr = curr.next

    curr.next = new_node
```

---

## Append Dry Run

Current:

```text
10 -> 20 -> 30 -> None
```

Append:

```python
append(40)
```

Traverse:

```text
10
20
30
```

Reached last node.

Connect:

```text
30.next = 40
```

Final:

```text
10 -> 20 -> 30 -> 40
```

---

# Display Operation

## Code

```python
def display(self):

    curr = self.head

    while curr:
        print(curr.data,end=" -> ")
        curr = curr.next

    print("None")
```

---

## Example

```python
ll.display()
```

Output:

```text
10 -> 20 -> 30 -> 40 -> None
```

---

# Complete Program

```python
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def append(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node


    def display(self):

        curr = self.head

        while curr:
            print(curr.data,end=" -> ")
            curr = curr.next

        print("None")


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.display()
```

Output:

```text
10 -> 20 -> 30 -> 40 -> None
```

---

# Interview Cheat Sheet

## Create Node

```python
new_node = Node(value)
```

## Traverse

```python
curr = head

while curr:
    curr = curr.next
```

## Last Node

```python
while curr.next:
    curr = curr.next
```

## Insert at End

```python
curr.next = new_node
```

## Stop Condition

```python
curr == None
```

---

# Most Common LeetCode Linked List Operations

1. Traversal
    
2. Search
    
3. Reverse Linked List
    
4. Find Middle Node
    
5. Remove Nth Node
    
6. Merge Two Lists
    
7. Detect Cycle
    
8. Palindrome Linked List
    
9. Intersection of Lists
    
10. Add Two Numbers
    

Master Traversal first.

Everything else is just pointer manipulation.

# Fast & Slow Pointer Pattern

The Fast & Slow Pointer technique is one of the most important Linked List patterns.

```text
Slow Pointer → moves 1 step
Fast Pointer → moves 2 steps
```

Common applications:

* Finding the middle node
* Detecting cycles
* Finding the start of a cycle
* Palindrome Linked List
* Reordering a list
* Removing the Nth node from the end

---

## 876. Middle of the Linked List

**LeetCode:** https://leetcode.com/problems/middle-of-the-linked-list/

---

### Problem Statement

Given the head of a singly linked list, return the middle node.

If there are two middle nodes, return the second middle node.

---

### Example 1

### Input

```text
1 → 2 → 3 → 4 → 5
```

### Output

```text
3 → 4 → 5
```

---

## Example 2

### Input

```text
1 → 2 → 3 → 4 → 5 → 6
```

### Output

```text
4 → 5 → 6
```

---

## Intuition

Use two pointers:

```python
slow = head
fast = head
```

Move them at different speeds:

```python
slow = slow.next
fast = fast.next.next
```

---

## Visualization

### Initial State

```text
1 → 2 → 3 → 4 → 5
S
F
```

---

### First Move

```text
1 → 2 → 3 → 4 → 5
    S   F
```

---

### Second Move

```text
1 → 2 → 3 → 4 → 5
        S       F
```

---

### Stop Condition

```text
Fast reaches the end.
```

At this point:

```text
Slow is at the middle node.
```

---

## Why Does It Work?

```text
Slow moves 1 step.
Fast moves 2 steps.
```

Therefore:

```text
When Fast covers the entire list,
Slow covers half of it.
```

So Slow naturally lands at the middle.

---

## Code

```python
class Solution:
    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

---

## Complexity Analysis

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(1)       |

---

## Pattern Recognition
---
---


Whenever you see:

```text
Middle
Halfway
Center
Split the List
```

Think:

```text
Fast & Slow Pointer
```

---


## 141. Linked List Cycle

**LeetCode:** https://leetcode.com/problems/linked-list-cycle/
---
---

### Problem Statement

Determine whether a linked list contains a cycle.

---

### Without a Cycle

```text
1 → 2 → 3 → 4 → None
```

Traversal ends normally.

---

### With a Cycle

```text
1 → 2 → 3 → 4
    ↑       ↓
    └───────┘
```

Traversal never ends.

---

### Brute Force Idea

Store visited nodes in a set.

```python
visited = set()
```

If a node appears again:

```python
return True
```

Otherwise:

```python
visited.add(node)
```

---

### Drawback

```text
Extra Space = O(n)
```

We can do better.

---

### Optimal Approach

Use two pointers.

```python
slow = head
fast = head
```

Move:

```python
slow = slow.next
fast = fast.next.next
```

---

### Visualization

### Initial State

```text
1 → 2 → 3 → 4
↑
S,F
```

---

### First Move

```text
Slow = 2
Fast = 3
```

---

### Second Move

```text
Slow = 3
Fast = 2
```

---

### Third Move

```text
Slow = 4
Fast = 4
```

They meet.

```text
Cycle Exists
```

---

### Why Must They Meet?

Imagine a circular running track.

```text
Slow runs at speed 1
Fast runs at speed 2
```

If both continue moving:

```text
Fast eventually catches Slow.
```

The same principle applies inside a cycle.

---

### Key Observation

### No Cycle

```text
Fast reaches None
```

Result:

```python
False
```

---

### Cycle Exists

```text
Fast catches Slow
```

Result:

```python
True
```

---

## Code

```python
class Solution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

---

## Complexity Analysis

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(1)       |

---

## Comparison

| Problem         | Goal        | Condition        |
| --------------- | ----------- | ---------------- |
| Middle Node     | Find middle | Fast reaches end |
| Cycle Detection | Check loop  | Slow meets Fast  |

---

# Fast & Slow Pointer Template

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    # Problem-specific logic
```

This template is the foundation for many Linked List interview questions.
