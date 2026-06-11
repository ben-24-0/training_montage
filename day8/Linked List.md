# Linked Lists - Complete Guide


- [[#Foundations|Foundations]]
	- [[#Foundations#What is a Linked List?|What is a Linked List?]]
	- [[#Foundations#Visual Representation|Visual Representation]]
	- [[#Foundations#Why Do We Need Linked Lists?|Why Do We Need Linked Lists?]]
	- [[#Foundations#Array Problem|Array Problem]]
	- [[#Foundations#Linked List Solution|Linked List Solution]]
	- [[#Foundations#Anatomy of a Node|Anatomy of a Node]]
	- [[#Foundations#Python Node Structure|Python Node Structure]]
	- [[#Foundations#Understanding self.next|Understanding self.next]]
	- [[#Foundations#Head Pointer|Head Pointer]]
- [[#Core Concepts|Core Concepts]]
	- [[#Core Concepts#Traversal Logic|Traversal Logic]]
	- [[#Core Concepts#Dry Run|Dry Run]]
	- [[#Core Concepts#Golden Rule|Golden Rule]]
- [[#Implementation|Implementation]]
	- [[#Implementation#Creating a Node|Creating a Node]]
	- [[#Implementation#Creating Individual Nodes|Creating Individual Nodes]]
	- [[#Implementation#Creating a Linked List Class|Creating a Linked List Class]]
	- [[#Implementation#Append Operation|Append Operation]]
	- [[#Implementation#Code|Code]]
	- [[#Implementation#Dry Run|Dry Run]]
	- [[#Implementation#Display Operation|Display Operation]]
	- [[#Implementation#Code|Code]]
	- [[#Implementation#Example|Example]]
- [[#Complete Program|Complete Program]]
- [[#Interview Cheat Sheet|Interview Cheat Sheet]]
	- [[#Interview Cheat Sheet#Create Node|Create Node]]
	- [[#Interview Cheat Sheet#Traverse List|Traverse List]]
	- [[#Interview Cheat Sheet#Find Last Node|Find Last Node]]
	- [[#Interview Cheat Sheet#Insert at End|Insert at End]]
	- [[#Interview Cheat Sheet#Stop Condition|Stop Condition]]
- [[#Most Common LeetCode Linked List Operations|Most Common LeetCode Linked List Operations]]
- [[#Fast & Slow Pointer Pattern|Fast & Slow Pointer Pattern]]
- [[#Common Applications|Common Applications]]
- [[#Problem 876: Middle of the Linked List|Problem 876: Middle of the Linked List]]
	- [[#Problem 876: Middle of the Linked List#Problem Statement|Problem Statement]]
	- [[#Problem 876: Middle of the Linked List#Examples|Examples]]
	- [[#Problem 876: Middle of the Linked List#Example 1|Example 1]]
	- [[#Problem 876: Middle of the Linked List#Example 2|Example 2]]
	- [[#Problem 876: Middle of the Linked List#Intuition|Intuition]]
	- [[#Problem 876: Middle of the Linked List#Visualization|Visualization]]
	- [[#Problem 876: Middle of the Linked List#Initial State|Initial State]]
	- [[#Problem 876: Middle of the Linked List#After Move 1|After Move 1]]
	- [[#Problem 876: Middle of the Linked List#After Move 2|After Move 2]]
	- [[#Problem 876: Middle of the Linked List#Stop Condition|Stop Condition]]
	- [[#Problem 876: Middle of the Linked List#Why Does It Work?|Why Does It Work?]]
	- [[#Problem 876: Middle of the Linked List#Solution|Solution]]
	- [[#Problem 876: Middle of the Linked List#Complexity Analysis|Complexity Analysis]]
	- [[#Problem 876: Middle of the Linked List#Key Insight|Key Insight]]
- [[#Problem 141: Linked List Cycle|Problem 141: Linked List Cycle]]
- [[#Problem Statement|Problem Statement]]
- [[#What is a Cycle?|What is a Cycle?]]
	- [[#What is a Cycle?#Normal Linked List (No Cycle)|Normal Linked List (No Cycle)]]
	- [[#What is a Cycle?#Linked List with Cycle|Linked List with Cycle]]
- [[#Examples|Examples]]
	- [[#Examples#Example 1|Example 1]]
	- [[#Examples#Example 2|Example 2]]
	- [[#Examples#Example 3|Example 3]]
- [[#Approach 1: Brute Force (Set)|Approach 1: Brute Force (Set)]]
- [[#Approach 2: Floyd's Cycle Detection (Optimal)|Approach 2: Floyd's Cycle Detection (Optimal)]]
	- [[#Approach 2: Floyd's Cycle Detection (Optimal)#Core Idea|Core Idea]]
	- [[#Approach 2: Floyd's Cycle Detection (Optimal)#Case 1: No Cycle|Case 1: No Cycle]]
	- [[#Approach 2: Floyd's Cycle Detection (Optimal)#Case 2: Cycle Exists|Case 2: Cycle Exists]]
- [[#Why They Must Meet|Why They Must Meet]]
- [[#Visualization|Visualization]]
	- [[#Visualization#Initial|Initial]]
	- [[#Visualization#Move 1|Move 1]]
	- [[#Visualization#Move 2|Move 2]]
	- [[#Visualization#Move 3|Move 3]]
- [[#Solution|Solution]]
- [[#Loop Condition Explanation|Loop Condition Explanation]]
- [[#Complexity Analysis|Complexity Analysis]]
- [[#Key Insight|Key Insight]]

---

## Foundations

### What is a Linked List?

A Linked List is a linear data structure where elements are stored in separate objects called **nodes**.

Unlike arrays:

- Arrays store elements in contiguous memory
- Linked Lists store elements anywhere in memory
- Nodes are connected using pointers/references

---

### Visual Representation

```
10      20      30      40

┌────┬────┐    ┌────┬────┐    ┌────┬────┐    ┌────┬────┐
│ 10 │ •──┼──► │ 20 │ •──┼──► │ 30 │ •──┼──► │ 40 │None│
└────┴────┘    └────┴────┘    └────┴────┘    └────┴────┘
```

Each box is a **Node**. Each node contains:

1. **Data** - the actual value
2. **Reference to next node** - pointer/link to the next node

---

### Why Do We Need Linked Lists?

### Array Problem

```python
arr = [10,20,30,40]
```

Insert 15 at index 1:

```python
[10,15,20,30,40]
```

**Issue:** All elements after index 1 must shift → **O(n) time complexity**

### Linked List Solution

```
10 -> 20 -> 30 -> 40
```

Insert 15 after 10:

```
10 -> 15 -> 20 -> 30 -> 40
```

**Advantage:** Only pointers change, no shifting required → **O(1) time complexity for insertion**

---

### Anatomy of a Node

A node contains:

```python
data      # The value stored
next      # Reference to next node
```

### Python Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Understanding self.next

Create a node:

```python
node1 = Node(10)
```

Memory state:

```
node1:
  data = 10
  next = None
```

Create another node:

```python
node2 = Node(20)
```

Connect them:

```python
node1.next = node2
```

Now:

```
10 -> 20 -> None
```

---

### Head Pointer

The first node is called the **Head**.

```
head
 ↓
10 -> 20 -> 30 -> None
```

**Important:** Without head, the entire list is lost.

```
Head is the entry point to the Linked List.
```

---

## Core Concepts

### Traversal Logic

**Question:** How do we visit every node?

**Answer:** Start from head and keep moving using next.

```python
curr = head

while curr:
    print(curr.data)
    curr = curr.next
```

### Dry Run

Given:

```
head
 ↓
10 -> 20 -> 30 -> None
```

**Iteration 1:**

- curr = 10
- Print: 10
- Move: curr = curr.next

**Iteration 2:**

- curr = 20
- Print: 20
- Move: curr = curr.next

**Iteration 3:**

- curr = 30
- Print: 30
- Move: curr = curr.next

**Iteration 4:**

- curr = None
- Loop stops

---

### Golden Rule

Whenever you see a Linked List question:

```
1. Start from head
2. Move using next
3. Stop at None
```

This single idea solves most Linked List problems.

---

## Implementation

### Creating a Node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Creating Individual Nodes

```python
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect them
node1.next = node2
node2.next = node3

# Result: 10 -> 20 -> 30 -> None
```

---

### Creating a Linked List Class

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

Initially:

```
head -> None
```

This is an empty list.

---

### Append Operation

**Goal:** Add a node to the end of the list

Given: `10 -> 20 -> 30`

Append: `40`

Result: `10 -> 20 -> 30 -> 40`

### Code

```python
def append(self, data):
    new_node = Node(data)
    
    # If list is empty, new node becomes head
    if self.head is None:
        self.head = new_node
        return
    
    # Traverse to the last node
    curr = self.head
    while curr.next:
        curr = curr.next
    
    # Connect last node to new node
    curr.next = new_node
```

### Dry Run

Current list: `10 -> 20 -> 30 -> None`

Call: `append(40)`

**Steps:**

1. Create new_node with data=40
2. Traverse to last node (30)
3. Connect: 30.next = 40
4. Final: `10 -> 20 -> 30 -> 40`

---

### Display Operation

Print the entire linked list

### Code

```python
def display(self):
    curr = self.head
    
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    
    print("None")
```

### Example

```python
ll.display()
# Output: 10 -> 20 -> 30 -> 40 -> None
```

---

## Complete Program

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
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
            print(curr.data, end=" -> ")
            curr = curr.next
        
        print("None")


# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.display()
# Output: 10 -> 20 -> 30 -> 40 -> None
```

---

## Interview Cheat Sheet

### Create Node

```python
new_node = Node(value)
```

### Traverse List

```python
curr = head
while curr:
    curr = curr.next
```

### Find Last Node

```python
while curr.next:
    curr = curr.next
```

### Insert at End

```python
curr.next = new_node
```

### Stop Condition

```python
curr == None
```

---

## Most Common LeetCode Linked List Operations

1. **Traversal** - Visit every node
2. **Search** - Find a specific value
3. **Reverse Linked List** - Reverse the order
4. **Find Middle Node** - Locate center node
5. **Remove Nth Node** - Delete specific node
6. **Merge Two Lists** - Combine two lists
7. **Detect Cycle** - Check for loops
8. **Palindrome Linked List** - Check if palindrome
9. **Intersection of Lists** - Find common node
10. **Add Two Numbers** - Add number lists

**Key Insight:** Master traversal first. Everything else is just pointer manipulation.

---

## Fast & Slow Pointer Pattern

The Fast & Slow Pointer technique is one of the most important Linked List patterns.

```
Slow Pointer → moves 1 step per iteration
Fast Pointer → moves 2 steps per iteration
```

## Common Applications

- Finding the middle node
- Detecting cycles
- Finding the start of a cycle
- Checking if list is palindrome
- Reordering a list
- Removing the Nth node from the end

---

## Problem 876: Middle of the Linked List

**LeetCode:** https://leetcode.com/problems/middle-of-the-linked-list/

### Problem Statement

Given the head of a singly linked list, return the middle node.

If there are two middle nodes, return the **second** middle node.

### Examples

### Example 1

**Input:** `1 -> 2 -> 3 -> 4 -> 5`

**Output:** `3 -> 4 -> 5`

### Example 2

**Input:** `1 -> 2 -> 3 -> 4 -> 5 -> 6`

**Output:** `4 -> 5 -> 6`

### Intuition

Use two pointers:

```python
slow = head    # moves 1 step
fast = head    # moves 2 steps
```

Movement:

```python
slow = slow.next
fast = fast.next.next
```

When fast reaches the end, slow will be at the middle.

### Visualization

### Initial State

```
1 -> 2 -> 3 -> 4 -> 5
S
F
```

### After Move 1

```
1 -> 2 -> 3 -> 4 -> 5
     S    F
```

### After Move 2

```
1 -> 2 -> 3 -> 4 -> 5
          S         F
```

### Stop Condition

Fast reaches the end → Slow is at middle node.

### Why Does It Work?

```
Slow moves 1 step
Fast moves 2 steps

When Fast covers the entire list,
Slow covers exactly half of it.
```

So Slow naturally lands at the middle.

### Solution

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

### Complexity Analysis

|Metric|Complexity|
|---|---|
|Time|O(n)|
|Space|O(1)|

### Key Insight

**When you see:** Middle, Halfway, Center, Split the List

**Think:** Fast & Slow Pointer

---

## Problem 141: Linked List Cycle

**LeetCode:** https://leetcode.com/problems/linked-list-cycle/

## Problem Statement

Given the head of a linked list, determine whether the linked list contains a cycle.

Return `True` if a cycle exists, otherwise `False`.

## What is a Cycle?

A cycle occurs when a node points back to a previous node instead of pointing to `None`.

### Normal Linked List (No Cycle)

```
1 -> 2 -> 3 -> 4 -> None
```

Traversal eventually ends.

### Linked List with Cycle

```
1 -> 2 -> 3 -> 4
     ^         |
     |_________|
```

Traversal never ends.

## Examples

### Example 1

```
head = [3,2,0,-4], pos = 1
```

Visualization:

```
3 -> 2 -> 0 -> -4
     ^         |
     |_________|
```

**Output:** `True`

### Example 2

```
head = [1,2], pos = 0
```

Visualization:

```
1 -> 2
^    |
|____|
```

**Output:** `True`

### Example 3

```
head = [1]
```

Visualization:

```
1 -> None
```

**Output:** `False`

## Approach 1: Brute Force (Set)

Store every visited node in a set.

```python
def hasCycle(self, head):
    visited = set()
    curr = head
    
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    
    return False
```

**Complexity:**

- Time: O(n)
- Space: O(n) ❌ Extra space required

## Approach 2: Floyd's Cycle Detection (Optimal)

Also called: **Tortoise and Hare Algorithm**

### Core Idea

Use two pointers moving at different speeds:

```python
slow = head    # moves 1 step
fast = head    # moves 2 steps
```

**Key Insight:** On a circular track, a faster runner will eventually catch the slower runner.

### Case 1: No Cycle

```
1 -> 2 -> 3 -> 4 -> None
```

Fast pointer reaches `None` first → No cycle → Return `False`

### Case 2: Cycle Exists

```
1 -> 2 -> 3 -> 4
     ^         |
     |_________|
```

Fast pointer catches Slow pointer → Cycle exists → Return `True`

## Why They Must Meet

Imagine a circular running track:

```
Slow runner → Speed 1
Fast runner → Speed 2
```

If both keep running on a circle:

```
Fast runner will eventually catch the Slow runner.
```

The same principle applies inside a linked list cycle.

## Visualization

Given:

```
1 -> 2 -> 3 -> 4
     ^         |
     |_________|
```

### Initial

```
Slow = 1
Fast = 1
```

### Move 1

```
Slow = 2
Fast = 3
```

### Move 2

```
Slow = 3
Fast = 2
```

### Move 3

```
Slow = 4
Fast = 4
```

**They meet!** → Cycle confirmed

## Solution

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

## Loop Condition Explanation

```python
while fast and fast.next:
```

**Why?**

Because we need to safely access `fast.next.next`:

```python
fast.next.next
```

Requires:

- `fast != None`
- `fast.next != None`

Otherwise Python throws an error.

## Complexity Analysis

|Metric|Complexity|
|---|---|
|Time|O(n)|
|Space|O(1)|

## Key Insight

**When you see:** Cycle, Loop, Circular Structure, Repeated Traversal

**Think:** Floyd's Cycle Detection Algorithm

---

# Problem 19: Remove Nth Node From End of List

**LeetCode:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Problem Statement

Given the head of a linked list, remove the **n-th node from the end** of the list and return the head.

## Example

### Input

```
head = [1,2,3,4,5]
n = 2
```

Linked List:

```
1 -> 2 -> 3 -> 4 -> 5
```

### Output

```
1 -> 2 -> 3 -> 5
```

The 2nd node from the end is **4**, so we remove it.

---

## Approach 1: Brute Force (Two Pass)

### Step 1: Count Nodes

```
1 -> 2 -> 3 -> 4 -> 5
Count = 5
```

### Step 2: Calculate Position from Start

```python
position = count - n = 5 - 2 = 3
```

### Step 3: Traverse Again and Delete

This requires **two traversals** → O(n) + O(n) = O(2n)

---

## Approach 2: Fast & Slow Pointer (Optimal)

Instead of counting, create a **gap of n nodes** between Fast and Slow.

### Step 1: Move Fast by n Steps

```python
for i in range(n):
    fast = fast.next
```

Given list: `1 -> 2 -> 3 -> 4 -> 5` and `n = 2`

After moving Fast:

```
1 -> 2 -> 3 -> 4 -> 5
S        F
(gap of 2 nodes)
```

### Why Create This Gap?

When Fast reaches the end, Slow will be **just before the node to delete**.

**Key Insight:**

```
If Fast always stays n nodes ahead of Slow:
When Fast reaches the end,
Slow reaches the node before the target node.
```

### Step 2: Edge Case - Removing Head

If we need to remove the head node:

```python
if fast is None:
    return head.next
```

### Step 3: Move Both Together

```python
while fast and fast.next:
    fast = fast.next
    slow = slow.next
```

Both pointers move together, maintaining the gap.

### Step 4: Delete the Node

```python
slow.next = slow.next.next
```

Before:

```
3 -> 4 -> 5
```

After:

```
3 ------> 5
(skip 4)
```

## Dry Run

**Input:** `1 -> 2 -> 3 -> 4 -> 5`, `n = 2`

### Initial Gap

```
1 -> 2 -> 3 -> 4 -> 5
S        F
```

### Move 1

```
1 -> 2 -> 3 -> 4 -> 5
     S        F
```

### Move 2

```
1 -> 2 -> 3 -> 4 -> 5
          S        F
```

Fast is at the last node (5). Stop.

### Delete

```
Slow = 3 (node with value 3)
Slow.next = 4
Slow.next.next = 5

Execute: slow.next = slow.next.next
Result: 3.next = 5
```

**Final:** `1 -> 2 -> 3 -> 5`

## Solution

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        
        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next
        
        # Edge case: removing head node
        if fast is None:
            return head.next
        
        # Move both pointers until fast reaches end
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # Delete the node
        slow.next = slow.next.next
        
        return head
```

## Complexity Analysis

|Metric|Complexity|
|---|---|
|Time|O(n)|
|Space|O(1)|

## Key Insight

This problem shows a **new use of Fast & Slow pointers**:

### Middle Node Problem

```
Fast moves 2x faster
Goal: Find Middle
```

### Remove Nth From End Problem

```
Fast starts n nodes ahead
Goal: Maintain a fixed gap
When Fast reaches the end,
Slow reaches the node before the target.
```

**Pattern Recognition:**

When you see: Nth Node From End, Kth Node From End, Distance Between Nodes

**Think:** Move Fast K steps first, then move both together

---

# Template

## Fast & Slow Pointer Template

```python
slow = head
fast = head

# Problem 1: Finding Middle
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow


# Problem 2: Detecting Cycle
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
        return True

return False


# Problem 3: Remove Nth From End
for i in range(n):
    fast = fast.next

if fast is None:
    return head.next

while fast and fast.next:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next
return head
```

## Variations Using This Template

This template is reused in:

- Linked List Cycle
- Linked List Cycle II
- Find Cycle Start
- Happy Number
- Circular Array Loop
- Duplicate Number (Floyd's Algorithm)

---

# Interview One-Liner

```
Fast moves 2 steps.
Slow moves 1 step.

When Fast reaches the end,
Slow reaches the middle.
```

---

**End of Guide**