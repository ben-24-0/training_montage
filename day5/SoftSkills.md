#softskills
365 = 1 year =>Normal
# Calendars 
```
```
![[Pasted image 20260606190137.png]]

| Month | Code |
| ----- | ---- |
| Jan   | 0    |
| Feb   | 3    |
| Mar   | 3    |
| Apr   | 6    |
| May   | 1    |
| Jun   | 4    |
| Jul   | 6    |
| Aug   | 2    |
| Sep   | 5    |
| Oct   | 0    |
| Nov   | 3    |
| Dec   | 5    |

| Century | Code |
| ------- | ---- |
| 1600    | 6    |
| 1700s   | 4    |
| 1800s   | 2    |
| 1900s   | 0    |
| 2000s   | 6    |
| 2100s   | 4    |

Leap Year Adjustment
```
Jan = -1
Feb = -1
```

In a leap year, subtract 1 from the final day count if the date falls in January or February.


## Calendar Shortcut

1. Take last 2 digits of year → YY
2. Compute YY/4 (ignore remainder)
3. Add Date
4. Add Month Code
5. Add Century Code
6. Total % 7
7. Match with day table

Day Number =
Date + Month Code + Century Code + YY + floor(YY/4)

Q. 26/05/2026
Using your shortcut:

```text
Date = 6
Month Code (June) = 4
YY = 26
YY/4 = 6
Century Code (2000s) = 6
```

Total:

```text
6 + 4 + 26 + 6 + 6
= 48
```

Now:

```text
48 % 7 = 6
```

Day table:

```text
0 Sun
1 Mon
2 Tue
3 Wed
4 Thu
5 Fri
6 Sat
```

**06/06/2026 = Saturday**.


##  How many days could be in K weeks and K days?

1 week = 7 days

K weeks + K days
= 7K + K
= 8K days

Use the **odd days shortcut**.

### Step 1: 2011 is a non-leap year

We need another **non-leap year** with the same total odd days difference = multiple of 7.

### Check each option

#### 2011 → 2014

```text
Years = 3
Leap years = 0

Odd days = 3
```

❌ Not divisible by 7

---

#### 2011 → 2018

```text
Years = 7
Leap years = 2012, 2016 = 2

Odd days = 7 + 2 = 9
9 % 7 = 2
```

❌

---

#### 2011 → 2021

```text
Years = 10
Leap years = 2012, 2016, 2020 = 3

Odd days = 10 + 3 = 13
13 % 7 = 6
```

❌

---

#### 2011 → 2022

```text
Years = 11
Leap years = 2012, 2016, 2020 = 3

Odd days = 11 + 3 = 14
14 % 7 = 0
```

✅ Same calendar

### Quick Rule

```text
Odd Days = Normal Years + Leap Years
```

If:

```text
Odd Days % 7 = 0
```

and both years are either leap or non-leap, then the calendars are identical.

**Answer: 2022** 

## Last Day of a Century

Starting from a known reference:
```
31 Dec 1600 = Sunday
```
> [!TIP] every century shifts by 5 odd days
```
31 Dec 1600 = Sunday
31 Dec 1700 = Sunday + 5 = Friday
31 Dec 1800 = Friday + 5 = Wednesday
31 Dec 1900 = Wednesday + 5 = Monday
31 Dec 2000 = Monday + 5 = Sunday
```

Possible:
- Mon
- Wed
- Fri
- Sun

Impossible:
- Tue
- Thu
- Sat


# Clocks
---

## Basics

- Minute hand = 360° in 60 min
- Hour hand = 360° in 12 hr

Minute hand speed = 6°/min ==> 6° for 1 min
Hour hand speed = 0.5°/min 
Relative speed = 5.5°/min

---

## Angle Between Hands

Angle = |30H - 5.5M|

H = hour
M = minutes

Smaller Angle:

if angle > 180°
    angle = 360° - angle

---

## Hands Coincide

11 times in 12 hours

Time after H o'clock:

M = 60H / 11

Examples:

1:05 5/11
2:10 10/11
3:16 4/11

---

## Hands Opposite (180°)

M = (60H + 360) / 11

---

## Right Angle (90°)

M = (60H ± 180) / 11

---

## Gain / Lose

Clock gains:
Actual Time = Clock Time - Gain

Clock loses:
Actual Time = Clock Time + Loss

---

## Useful Values

1 minute = 6°
5 minutes = 30°
15 minutes = 90°
30 minutes = 180°

