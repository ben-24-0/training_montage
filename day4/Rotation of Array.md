#dsa 
K rotation of arrays/List :
			- Rotate Array 
	
			  
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n <= 1:
            return

        k %= n

        i, j = 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = k, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
```
two Pointer 
			- Merge Sorted Array - [88](https://leetcode.com/problems/merge-sorted-array/description/)
			- Valid Palindrome : [125](https://leetcode.com/problems/valid-palindrome/description/)
			- Valid Palindrome 2 : [680](https://leetcode.com/problems/valid-palindrome-ii/)
Sliding Window

			# Sliding Window (Fixed Size)

## Concept Sliding Window

A **fixed-size sliding window** is used when we need to process all contiguous subarrays/substrings of size `k`.

Instead of recalculating the result for every window, we:

1. Compute the result for the first window.
2. Slide the window by one position.
3. Remove the element leaving the window.
4. Add the element entering the window.

This reduces the time complexity from **O(n × k)** to **O(n)**.

---

## Visualization

Array:

```text
[1, 2, 3, 4, 5]
```

Window size:

```text
k = 3
```

Windows:

```text
[1, 2, 3]
   [2, 3, 4]
      [3, 4, 5]
```

---

## Example: Maximum Sum Subarray of Size K

### Brute Force

```python
nums = [1, 2, 3, 4, 5]
k = 3

max_sum = 0

for i in range(len(nums) - k + 1):
    curr_sum = sum(nums[i:i+k])
    max_sum = max(max_sum, curr_sum)
```

**Time Complexity:** `O(n × k)`

---

### Sliding Window

```python
nums = [1, 2, 3, 4, 5]
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right]       # add new element
    window_sum -= nums[right - k]   # remove old element

    max_sum = max(max_sum, window_sum)

print(max_sum)
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(1)`

---

## Generic Template

```python
window = initial_window_value

for i in range(k, len(arr)):
    window += arr[i]       # add entering element
    window -= arr[i - k]   # remove leaving element

    # process current window
```

---

## When to Use

Use a fixed-size sliding window when:

- Window size `k` is given.
- Need to process contiguous subarrays/substrings.
- Looking for:
  - Maximum/Minimum sum
  - Average
  - Count of elements
  - Frequency calculations
  - Pattern matching in substrings

---
## Common LeetCode Problems (Subarray / Sliding Window)

- [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
- [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

---

## SubArray vs SubSequence
### Quick Memory Trick

```
Subarray   = Continuous chunk[1, 2, 3, 4]    └─┘Subsequence = Pick and choose[1, 2, 3, 4] ↑     ↑  ↑
```

**Every subarray is a subsequence, but not every subsequence is a subarray.**

If a problem says:  
  
- **Contiguous** → Think **Subarray**  
- **Can skip elements** → Think **Subsequence**  
- **Sliding Window** → Usually **Subarray**  
- **DP on choices (take / not take)** → Usually **Subsequence**
# Important Subsequence Problems

## Easy
- [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

## Medium
- [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)
- [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

## Hard
- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

---

## Must Know

1. [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)
2. [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
3. [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
4. [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)


