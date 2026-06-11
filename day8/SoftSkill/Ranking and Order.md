#softskills 

# Ranking & Order — High-Yield Patterns from the PDF

> [!TIP]
> Do **not** solve all 100+ questions.
>
> Almost every Ranking question in the PDF belongs to one of these **5 patterns**.

---

# Pattern 1: Same Person From Both Ends

## Formula

```text
Total = Left Rank + Right Rank - 1
```

---

## Representative Question

```text
Rahul is 34th from the left.

Rahul is 37th from the right.

Find total persons.
```

### Solution

```text
Total

= 34 + 37 - 1

= 70
```

<details>
<summary>Answer</summary>

```text
70
```

</details>

---

## Similar Questions

```text
Q11
Q14
Q22
Q34
```

---

# Pattern 2: Find Rank From Other Side

## Formula

```text
Other Side Rank

= Total - Given Rank + 1
```

---

## Representative Question

```text
There are 22 persons.

Rahul is 13th from the right.

Find his rank from the left.
```

### Solution

```text
Left

= 22 - 13 + 1

= 10
```

<details>
<summary>Answer</summary>

```text
10th
```

</details>

---

## Similar Questions

```text
Q1
Q15
Q28
Q30
Q35
Q36
Q37
```

---

# Pattern 3: Persons Between Two People

---

## Case A: No Overlap

### Formula

```text
Between

= Total - (Left Rank + Right Rank)
```

---

## Representative Question

```text
Total = 62

Rahul = 24th from left

Nitesh = 20th from right

Find persons between.
```

### Solution

```text
62 - (24 + 20)

= 18
```

<details>
<summary>Answer</summary>

```text
18
```

</details>

---

## Case B: Overlap

### Formula

```text
Between

= (Left Rank + Right Rank)

- Total

- 2
```

---

## Representative Question

```text
Total = 62

Rahul = 36th from left

Nitesh = 29th from right
```

### Solution

```text
(36 + 29)

- 62

- 2

= 1
```

<details>
<summary>Answer</summary>

```text
1
```

</details>

---

## Similar Questions

```text
Q3
Q5
Q39
Q45
```

---

# Pattern 4: Interchange of Positions

Most Important Pattern

---

## Representative Question

```text
Rahul is 12th from left.

Nitesh is 18th from right.

They interchange positions.

Rahul becomes 25th from left.

Find total persons.
```

### Shortcut

```text
Total

= New Left Rank

+ Old Right Rank

- 1
```

### Calculation

```text
25 + 18 - 1

= 42
```

<details>
<summary>Answer</summary>

```text
42
```

</details>

---

## Persons Between

### Formula

```text
Between

= New Rank

- Old Rank

- 1
```

### Calculation

```text
25 - 12 - 1

= 12
```

<details>
<summary>Answer</summary>

```text
12
```

</details>

---

## Similar Questions

```text
Q17
Q23
Q40
Q49
```

---

# Pattern 5: Exact Middle Person

---

## Representative Question

```text
Rahul = 10th from left

Nitesh = 9th from right

Gaurav sits exactly between them.

Gaurav = 16th from left.

Find total persons.
```

### Solution

```text
16 - 10 - 1

= 5
```

```text
5 persons between Rahul and Gaurav

5 persons between Gaurav and Nitesh
```

```text
Gaurav from right

= 9 + 5 + 1

= 15
```

```text
Total

= 16 + 15 - 1

= 30
```

<details>
<summary>Answer</summary>

```text
30
```

</details>

---

## Similar Questions

```text
Q3
Q11
Q27
```

---

# Important "Cannot Be Determined" Cases

## Case 1

```text
Rahul = 22nd from left

Nitesh = 35th from right

Find total persons.
```

### Why?

```text
Overlap may occur

or

May not occur
```

<details>
<summary>Answer</summary>

```text
Cannot Be Determined
```

</details>

---

## Case 2

```text
R is 15th from right

10 persons between R and M

Find M's rank.
```

### Why?

```text
M can be left

or

M can be right
```

<details>
<summary>Answer</summary>

```text
Data Inadequate
```

</details>

---

# Must-Solve Questions From PDF

## Tier 1

```text
Q11
Q14
Q17
Q22
Q23
```

---

## Tier 2

```text
Q27
Q34
Q39
Q40
Q49
```

---

# One-Page Revision Sheet

## Total Persons

```text
Total

= Left + Right - 1
```

---

## Other Side Rank

```text
Other Rank

= Total - Given Rank + 1
```

---

## Between Persons (No Overlap)

```text
Between

= Total - (Left + Right)
```

---

## Between Persons (Overlap)

```text
Between

= (Left + Right)

- Total

- 2
```

---

## Interchange

```text
Total

= New Rank + Old Opposite Rank - 1
```

```text
Between

= New Rank - Old Rank - 1
```

---

# Exam Strategy

> [!TIP]
>
> First identify the pattern:
>
> ```text
> Same Person Both Ends?
>        ↓
> Left + Right - 1
>
> Find Other Side?
>        ↓
> Total - Rank + 1
>
> Two Persons?
>        ↓
> Check Overlap
>
> Interchange?
>        ↓
> Use Swap Formula
>
> Exact Middle?
>        ↓
> Equal Distance Logic
> ```
>
> These five patterns cover almost every Ranking & Order question in the PDF. :contentReference[oaicite:0]{index=0}
