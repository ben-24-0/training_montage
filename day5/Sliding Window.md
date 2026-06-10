#dsa
### Var Sliding window continuation
- asking the length of sub-array where the sum is less than equal to k
```python
li=[2,3,1,5,2,4,6,7,8,5,2,3] 
r,m,s,l=0,0,0,0
k=10
while(r<len(li)):
    s+=li[r]
    while s>k:
        s-=li[l]
        l+=1
    length = r-l+1
    m = max(m,length)
    r+=1
print(m)
    



```
## Problems
Subarray Product Less Than K :[713](https://leetcode.com/problems/subarray-product-less-than-k/description/)
```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k<=1):
            return 0
        l = 0
        p = 1
        c = 0
        r=0 
        for r in range(len(nums)):
            p *= nums[r]
            while p >=k:
                p = p// nums[l]
                l+=1
            c += r-l+1
            # r+=1
        return c
        
```


# 713. Subarray Product Less Than K

## Idea

All numbers are positive. If the product becomes `>= k`, adding more elements will only increase it, so we use a sliding window.

## Algorithm

```python
product *= nums[r]

while product >= k:
    product //= nums[l]
    l += 1
```

After shrinking, the window `[l...r]` has product `< k`.

## Counting Trick

If the current window is valid, then every suffix ending at `r` is also valid.

Example:

```text
Window = [5,2,6]

Valid subarrays:
[6]
[2,6]
[5,2,6]
```

Number of valid subarrays ending at `r`:

```python
r - l + 1
```

So:

```python
count += r - l + 1
```

## Edge Case

```python
if k <= 1:
    return 0
```

Since all numbers are positive, every product is at least `1`, so no subarray can have product `< k`.

## Code

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        l = 0
        product = 1
        count = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k:
                product //= nums[l]
                l += 1

            count += r - l + 1

        return count
```


https://leetcode.com/problems/longest-substring-without-repeating-characters
https://leetcode.com/problems/max-consecutive-ones-iii


## Binary Search

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        low=0
        high=len(nums)-1
        inx=-1
        while low<=high:
            avg=(low+high)//2
            if target==nums[avg]:
                inx=avg
                return inx
            elif nums[avg]<target:
                low=avg+1
            elif nums[avg]>target:
                high=avg-1
        return inx
        
```
## Problems Solved
[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)
[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/2024152113/)
[162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)


[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
--
Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return _the minimum integer_ `k` _such that she can eat all the bananas within_ `h` _hours_.
# Explanation
___


**Example 1:**

**Input:** piles = [3,6,7,11], h = 8
**Output:** 4

| k         | ceil(3/k) | ceil(6/k) | ceil(7/k) | ceil(11/k) | Total hours     |
| --------- | --------- | --------- | --------- | ---------- | --------------- |
| k=1       | 3         | 6         | 7         | 11         | sum<2:5<br>     |
| k=2       | 2         | 3         | 4         | 6          | sum<2:5<br>     |
| k=3       | 1         | 2         | 3         | 4          | sum<2:5<br>     |
| k=4       | 1         | 2         | 2         | 3          | sum<2:5<br>     |
| k=5       | 1         | 1         | 2         | 6          | sum<2:5<br><br> |
| k=6       | 1         | 1         | 1         | 2          | sum<2:5<br>     |
| k='7'<br> | 1         | 1         | 1         | 4          | sum<2:5<br><br> |
| ...       | .         | .         | .         | .          | .               |
| k=11      | 0         | 0         | 0         | 0          | 0               |
|           |           |           |           |            |                 |
You can save this template for most **Binary Search on Answer** problems:
```python
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int):

        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)

            return hours <= h

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            if can_finish(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
```

# Binary Search on Answer

## Observation

We are not searching an array.

We are searching for the **smallest valid answer**.

Example:

```text
1  2  3  4  5  6  7
F  F  F  T  T  T  T
         ^
      answer
```

Once an answer becomes valid, every larger answer is also valid.

This monotonic property allows Binary Search.

---

## Define Search Space

```python
low = minimum_possible_answer
high = maximum_possible_answer
```

---

## Check Function

Create a helper function that tells whether an answer is valid.

```python
def check(x):
    ...
    return True or False
```

Examples:

- Koko Eating Bananas → Can Koko finish within `h` hours?
    
- Capacity to Ship Packages → Can all packages be shipped within `d` days?
    
- Minimum Days to Make Bouquets → Can we make `m` bouquets?
    

---

## Binary Search

```python
while low <= high:
    mid = (low + high) // 2

    if check(mid):
        high = mid - 1      # search for a smaller valid answer
    else:
        low = mid + 1       # current answer is too small
```

---

## Return

```python
return low
```

At the end:

```text
low = first valid answer
high = last invalid answer
```

```text
F F F F | T T T T
        ^
       low
```

---

## Koko Example

```python
def check(k):
    hours = 0

    for pile in piles:
        hours += ceil(pile / k)

    return hours <= h
```

```text
k

1  2  3  4  5  6  7
F  F  F  T  T  T  T
         ^
      minimum valid speed
```

Time Complexity:

```text
O(n log(maxAnswer))
```

## Common Binary Search on Answer Problems

- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
- [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
- [1552. Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)
- Aggressive Cows (Classic) — Not on LeetCode, commonly found on SPOJ/GeeksforGeeks




## [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid

            if mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
```

## [443. String Compression](https://leetcode.com/problems/string-compression/)
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        nw = ""
        count = 1

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                nw += chars[i - 1]

                if count > 1:
                    nw += str(count)

                count = 1

        chars[:] = list(nw)
        return len(chars)
```






