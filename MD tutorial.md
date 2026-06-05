# 1. Headings

```
# Main Topic## Sub Topic### Smaller Topic#### Tiny Topic
```

Output:

```
Main Topic └─ Sub Topic     └─ Smaller Topic
```

---

# 2. Code Blocks

Three backticks:

````
```pythona, b = map(int, input().split())```
````

Output:

```
a, b = map(int, input().split())
```

The word after the first three backticks enables syntax highlighting.

Examples:

````
```python``````java``````cpp``````bash```
````

---

# 3. Inline Code

For variables, methods, operators:

```
Use `map()` to convert values.
```

Output:

Use `map()` to convert values.

---

# 4. Horizontal Lines

```
---
```

Output:

---

Useful for separating sections.

---

# 5. Bullet Lists

```
- Apple- Banana- Mango
```

Output:

- Apple
- Banana
- Mango

Nested:

```
- DSA  - Arrays  - Strings
```

Output:

- DSA
    - Arrays
    - Strings

---

# 6. Numbered Lists

```
1. Input2. Process3. Output
```

Output:

1. Input
2. Process
3. Output

---

# 7. Tables

```
| Operator | Meaning ||----------|---------|| & | AND || | | OR || ^ | XOR |
```

⚠️ For OR you need to escape the pipe:

```
| Operator | Meaning ||----------|---------|| & | AND || \| | OR || ^ | XOR |
```

Output:

|Operator|Meaning|
|---|---|
|&|AND|
|\||OR|
|^|XOR|

---

# 8. Blockquotes

```
> Important:> XOR of same numbers is always 0.
```

Output:

> Important:  
> XOR of same numbers is always 0.

Great for interview tips.

---

# 9. Checkboxes

```
- [x] Learn Arrays- [x] Learn Strings- [ ] Learn Graphs
```

Output:

- [x]  Learn Arrays
- [x]  Learn Strings
- [ ]  Learn Graphs

Perfect for placement prep.

---

# 10. Callouts (Obsidian Special)

```
> [!NOTE]> Important concept.> [!TIP]> Useful shortcut.> [!WARNING]> Common mistake.
```

Output becomes fancy colored boxes in Obsidian.

Example:

```
> [!TIP]> x << y = x * 2^y
```

---

# 11. Folding Sections

```
<details><summary>Click to expand</summary>Hidden content here.</details>
```

Useful for solutions.

---

# 12. Internal Links (Obsidian's killer feature)

Suppose you have:

```
Arrays.mdStrings.md
```

You can write:

```
[[Arrays]][[Strings]]
```

Now clicking them opens those notes.

---

# 13. Tags

```
#python#dsa#placement
```

Then Obsidian can group all notes with the same tag.


# Markdown Math Cheat Sheet (Obsidian)

## Inline Math

```md
$x^2$
```

Result: (x^2)

```md
$\frac{1}{2}$
```

Result: (\frac{1}{2})

### Larger Inline Fraction

```md
$\dfrac{1}{2}$
```

or

```md
$\displaystyle \frac{1}{2}$
```
$\displaystyle \frac{1}{2}$

---

## Block Math

```md
$$
\frac{a+b}{c+d}
$$
```

$$
\frac{a+b}{c+d}
$$

---

## Multi-line Equations

### Recommended (Works in Obsidian)

```md
$$
\begin{array}{l}
100x = 88x + 396 \\
12x = 396 \\
x = 33
\end{array}
$$
```

$$
\begin{array}{l}
100x = 88x + 396 \\
12x = 396 \\
x = 33
\end{array}
$$
---

## Align Equal Signs

```md
$$
\begin{array}{rcl}
100x & = & 88x + 396 \\
12x  & = & 396 \\
x    & = & 33
\end{array}
$$
```

$$
\begin{array}{rcl}
100x & = & 88x + 396 \\
12x  & = & 396 \\
x    & = & 33
\end{array}
$$

### Column Types

|Symbol|Meaning|
|---|---|
|l|Left align|
|c|Center|
|r|Right align|

Example:

```md
\begin{array}{rcl}
a & = & b \\
c & = & d
\end{array}
```

---

## Common Math Symbols

### Powers

```md
x^2
```
x^2
```md
x^{10}
```

$$x^{10}$$

### Subscripts

```md
a_1
```

a_1
```md
a_{n+1}
```

$$a_{n+1}$$

### Square Root

```md
\sqrt{x}
```
$$
\sqrt{x}

$$
```md
\sqrt[3]{x}
```

$$sqrt[3]{x}$$
### Fractions

```md
\frac{a}{b}
```

### Summation

```md
\sum_{i=1}^{n} i
```

$$\sum_{i=1}^{n} i$$
### Product

```md
\prod_{i=1}^{n} i
```
$$\prod_{i=1}^{n} i$$
### Infinity

```md
\infty
```

---

## Interview / DSA Examples

```md
$$
\begin{array}{l}
\text{Sum of first n numbers} \\
n(n+1)/2
\end{array}
$$
```

```md
$$
\begin{array}{l}
\text{Binary Search} \\
O(\log n)
\end{array}
$$
```

```md
$$
\begin{array}{l}
\text{Arithmetic Progression} \\
S = \frac{n}{2}(a+l)
\end{array}
$$
```

---

## New Line

Inside arrays:

```md
\\
```

Example:

```md
a = b \\
c = d
```

---

## Useful Tip

For quick notes, these are often easier to read than rendered math:

```text
n(n+1)/2
O(log n)
a^2 + b^2 = c^2
```

Reserve LaTeX for derivations and multi-step calculations.