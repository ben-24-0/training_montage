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