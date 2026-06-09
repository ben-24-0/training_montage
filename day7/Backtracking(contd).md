## Word Search (Backtracking + DFS)

**LeetCode:** https://leetcode.com/problems/word-search/

---

## Problem

Given a grid of characters and a word, determine whether the word can be formed by moving:

```text
Up
Down
Left
Right
```

Rules:

* One cell can be used only once in a path.
* Characters must be matched in order.

---

## High-Level Idea

The solution has **three phases**:

```text
1. Quick Validation
2. Optimization
3. DFS + Backtracking
```

---

# Phase 1: Quick Validation

Before starting DFS, check whether the board even contains enough letters.

### Count Letters in the Word

```python
cw = Counter(word)
```

Example:

```text
Word = ABCCED
```

```python
cw = {
    'A':1,
    'B':1,
    'C':2,
    'D':1,
    'E':1
}
```

---

### Count Letters in the Board

```python
ltrs = [c for r in board for c in r]
cb = Counter(ltrs)
```

Board:

```text
A B C E
S F C S
A D E E
```

Flattened:

```python
['A','B','C','E',
 'S','F','C','S',
 'A','D','E','E']
```

Counts:

```python
cb = {
    'A':2,
    'B':1,
    'C':2,
    'D':1,
    'E':3,
    'F':1,
    'S':2
}
```

---

### Early Rejection

```python
for c in cw:
    if c not in cb or cb[c] < cw[c]:
        return False
```

Meaning:

```text
Does the board have every required letter?

AND

Does it have enough copies?
```

Example:

```text
Word needs:
A = 4

Board has:
A = 2
```

Impossible.

Return immediately.

No DFS needed.

---

# Phase 2: Optimization

```python
if cb[word[-1]] < cb[word[0]]:
    word = word[::-1]
```

---

### Why?

DFS begins by searching for the first character.

Suppose:

```text
Word = AAAAAB
```

Board:

```text
A appears 50 times
B appears 1 time
```

Without optimization:

```text
Start from A

50 possible starting positions
```

With optimization:

```text
Reverse word

BAAAAA
```

Now:

```text
Start from B

1 possible starting position
```

Much less searching.

---

> [!tip]
> Start DFS from the rarer character whenever possible.

---

# Phase 3: DFS + Backtracking

The actual search starts here.

---

## Meaning of Parameters

```python
backtrack(idx, i, j)
```

| Variable | Meaning                           |
| -------- | --------------------------------- |
| `idx`    | Character currently being matched |
| `i`      | Row                               |
| `j`      | Column                            |

---

### Example

```text
Word = ABCCED
```

```text
idx = 0 → A
idx = 1 → B
idx = 2 → C
idx = 3 → C
...
```

---

## Base Case

```python
if idx >= len(word):
    return True
```

All characters matched.

Example:

```text
Matched:

A B C C E D
```

Success.

---

## Invalid State Check

```python
if (
    i < 0 or i >= m or
    j < 0 or j >= n or
    board[i][j] != word[idx]
):
    return False
```

Reject if:

```text
Out of bounds
Wrong character
```

---

## Mark Cell as Visited

```python
temp = board[i][j]
board[i][j] = ""
```

Example:

```text
A B C
```

After visiting A:

```text
"" B C
```

This prevents revisiting the same cell.

---

## Move to Next Character

```python
idx += 1
```

Current:

```text
A
```

Next target:

```text
B
```

---

## Explore All Directions

```python
backtrack(idx, i-1, j)
backtrack(idx, i+1, j)
backtrack(idx, i, j-1)
backtrack(idx, i, j+1)
```

Visual:

```text
      Up
       ↑
Left ← X → Right
       ↓
     Down
```

If any direction succeeds:

```python
return True
```

---

## Backtracking

If every direction fails:

```python
board[i][j] = temp
```

Restore the cell.

Example:

Before DFS:

```text
A B C
```

Marked:

```text
"" B C
```

Restore:

```text
A B C
```

This allows other paths to reuse the cell.

---

## Why Backtracking Is Needed

Imagine:

```text
A B C
D E F
```

You try:

```text
A → B
```

Dead end.

Without restoring:

```text
A and B stay blocked forever
```

Other valid paths would fail.

Backtracking resets the board for future searches.

---

# Starting the Search

```python
for i in range(m):
    for j in range(n):
        if backtrack(0, i, j):
            return True
```

Try every cell as a starting point.

```text
(0,0)
(0,1)
(0,2)
...
```

The first successful path returns:

```python
True
```

If all starting positions fail:

```python
return False
```

---

# Mental Model

```text
Pick a starting cell
        │
        ▼
Match current character
        │
        ▼
Mark as visited
        │
        ▼
Try 4 directions
        │
        ▼
Success?
   /         \
 Yes         No
  │           │
 True     Restore Cell
              │
              ▼
         Try Another Path
```

---

# Pattern Recognition

This exact DFS + Backtracking pattern appears in:

* Word Search
* Rat in a Maze
* N-Queens
* Sudoku Solver
* Palindrome Partitioning
* Combination Sum

The idea is always:

```text
Choose
  ↓
Explore
  ↓
Undo (Backtrack)
  ↓
Try Another Choice
```
---
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        cw = Counter(word)
        print(cw)
        ltrs = [c for r in board for c in r]
        print(ltrs)
        cb = Counter(ltrs)
        print(cb)
        for c in cw:
            if not c in cb or cb[c] < cw[c]: return False
            
        if cb[word[-1]] < cb[word[0]]:
            word = word[::-1]
 
        def backtrack(idx, i, j):
            if idx >= len(word): return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
            
            temp = board[i][j]
            board[i][j] = ""
            idx += 1

            if backtrack(idx, i - 1, j): return True
            if backtrack(idx, i + 1, j): return True
            if backtrack(idx, i, j - 1): return True
            if backtrack(idx, i, j + 1): return True
            
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(0, i, j): return True
        return False

```

##Other Problems
# Common Backtracking Problems

1. **Subsets**
   https://leetcode.com/problems/subsets/

2. **Combination Sum**
   https://leetcode.com/problems/combination-sum/

3. **Permutations**
   https://leetcode.com/problems/permutations/

4. **Word Search**
   https://leetcode.com/problems/word-search/

5. **N-Queens**
   https://leetcode.com/problems/n-queens/

---

## Learning Order

```text
Subsets
   ↓
Combination Sum
   ↓
Permutations
   ↓
Word Search
   ↓
N-Queens
```

These five cover most of the common backtracking patterns:

```text
Subsets           → Pick / Skip
Combination Sum   → Choose & Reuse
Permutations      → Choose Unused
Word Search       → Grid Backtracking
N-Queens          → Constraint Backtracking
```
