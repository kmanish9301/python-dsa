# Python DSA Reference --- One-File Cheat Sheet

A practical Python reference for solving DSA problems in LeetCode and similar platforms.

**How to use this file** - Keep it open in PyCharm while solving problems. - Use `Ctrl + F` to search for a method or
topic, such as
`append`, `Counter`, `slice`, or `binary search`. - Examples are small and can be copied into a scratch file to
experiment with. - Unless stated otherwise, examples show Python 3.

------------------------------------------------------------------------

## 1. Variables and basic data types

``` python
name = "Manish"       # str: text
age = 25              # int: whole number
price = 19.99         # float: decimal number
is_valid = True       # bool: True or False
nothing = None        # NoneType: no value
```

Check a type:

``` python
type("hello")         # str
type([1, 2, 3])       # list
isinstance(10, int)   # True
```

Convert types:

``` python
int("123")            # 123
float("3.14")         # 3.14
str(123)              # "123"
list("abc")           # ['a', 'b', 'c']
```

**Truthy/falsy values:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, and `set()` are falsy. Most other values are
truthy.

``` python
if not nums:
    print("The list is empty")
```

## 2. Input, output, and operators

``` python
print("Hello")
x = 10
y = 3

x + y    # 13
x - y    # 7
x * y    # 30
x / y    # 3.333... (true division)
x // y   # 3 (floor division)
x % y    # 1 (remainder)
x ** y   # 1000 (power)
```

Useful operators:

``` python
x == y       # equal
x != y       # not equal
x > y
x >= y
x < y
x <= y
x in [1, 2]  # membership
x not in []  # not a member
a and b
a or b
not a
```

**Important:** `=` assigns a value; `==` compares values.

Integer division with negative numbers rounds down:

``` python
-7 // 3     # -3
-7 % 3      # 2
```

## 3. Strings (`str`)

Strings are **immutable**: methods return a new string rather than changing the original.

``` python
s = "hello world"
```

### Indexing and slicing

``` python
s[0]       # 'h' — first character
s[-1]      # 'd' — last character
s[0:5]     # 'hello' — index 0 up to, but not including, 5
s[:5]      # 'hello'
s[6:]      # 'world'
s[::2]     # every second character
s[::-1]    # reverse the string
```

General slice form: `sequence[start:stop:step]`. The `stop` index is excluded.

### Common string methods

``` python
s.lower()                   # lowercase
s.upper()                   # uppercase
s.capitalize()              # first character uppercase
s.title()                   # title case
s.strip()                   # remove whitespace at both ends
s.lstrip()                  # remove left-side whitespace
s.rstrip()                  # remove right-side whitespace
s.replace("world", "Python")
s.find("world")             # index, or -1 if absent
s.index("world")            # index, raises ValueError if absent
s.count("l")                # count occurrences
s.startswith("hello")       # True
s.endswith("world")         # True
s.split()                   # split on whitespace
"a,b,c".split(",")          # ['a', 'b', 'c']
"-".join(["a", "b", "c"])   # 'a-b-c'
```

Character checks:

``` python
"123".isdigit()             # True
"abc".isalpha()             # True
"abc123".isalnum()          # True
"   ".isspace()             # True
```

Useful patterns:

``` python
# Reverse
reversed_s = s[::-1]

# Check palindrome
is_palindrome = s == s[::-1]

# Build a string efficiently from pieces
parts = ["Py", "thon"]
result = "".join(parts)     # "Python"

# Convert to characters
chars = list("cat")         # ['c', 'a', 't']
```

**DSA tip:** Repeated string concatenation inside a large loop can be inefficient. Collect pieces in a list and use
`"".join(parts)`.

## 4. Lists (Python's usual array)

A `list` is an ordered, mutable collection. Python lists can grow and hold different types, though DSA lists usually
contain similar values.

``` python
nums = [10, 20, 30, 40]
empty = []
```

### Access, update, and slice

``` python
nums[0]       # 10
nums[-1]      # 40
nums[1:3]     # [20, 30]
nums[:2]      # [10, 20]
nums[2:]      # [30, 40]
nums[::-1]    # reversed copy
nums[1] = 99  # update element
len(nums)     # number of elements
```

### Common list methods

``` python
nums.append(50)        # add one item at the end
nums.extend([60, 70])  # add all items from another iterable
nums.insert(1, 15)     # insert 15 at index 1
nums.pop()             # remove and return last item
nums.pop(0)            # remove and return item at index 0
nums.remove(30)        # remove first matching value; error if absent
nums.index(20)         # index of first match; error if absent
nums.count(20)         # number of occurrences
nums.reverse()         # reverse the list in place
nums.sort()            # sort in place, ascending
nums.sort(reverse=True)
```

### Sorting

``` python
nums = [4, 1, 3, 2]

nums.sort()                 # changes nums; returns None
sorted_nums = sorted(nums)  # returns a new sorted list
descending = sorted(nums, reverse=True)

words = ["pear", "fig", "banana"]
sorted(words, key=len)      # sort by word length
```

Don't do `nums = nums.sort()`; that sets `nums` to `None`.

### Copying lists

``` python
a = [1, 2, 3]
b = a              # same list object — edits affect both
c = a.copy()       # shallow copy
d = a[:]           # also a shallow copy
```

### Useful list patterns

``` python
# Loop over values
for value in nums:
    print(value)

# Loop over indexes
for i in range(len(nums)):
    print(i, nums[i])

# Index and value together
for i, value in enumerate(nums):
    print(i, value)

# Create a list of zeros
zeros = [0] * 5

# List comprehension
squares = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]

# Filter
evens = [x for x in nums if x % 2 == 0]
```

**Common pitfall with 2D lists:**

``` python
# Correct: each row is a separate list
grid = [[0 for _ in range(3)] for _ in range(2)]

# Avoid: rows all refer to the same list
# grid = [[0] * 3] * 2
```

## 5. Tuples

Tuples are ordered and immutable.

``` python
point = (3, 4)
x, y = point             # unpacking
one_item = (5,)          # comma is required for a one-item tuple
```

Tuples are useful for fixed pairs, coordinates, and dictionary keys when all tuple contents are hashable.

``` python
visited = set()
visited.add((2, 3))
```

## 6. Sets

A set stores unique values and supports fast average-case membership checks.

``` python
seen = set()
seen.add(5)
seen.add(5)              # still only one 5
seen.remove(5)           # error if absent
seen.discard(99)         # safe if absent
5 in seen                # membership check
len(seen)
```

Create a set from a list:

``` python
nums = [1, 2, 2, 3]
unique = set(nums)       # {1, 2, 3}
```

Set operations:

``` python
a = {1, 2, 3}
b = {3, 4, 5}

a | b    # union: {1, 2, 3, 4, 5}
a & b    # intersection: {3}
a - b    # difference: {1, 2}
a ^ b    # symmetric difference: {1, 2, 4, 5}
```

**DSA uses:** duplicates detection, visited nodes, membership checks, unique elements.

## 7. Dictionaries (`dict` / hash maps)

Dictionaries map keys to values. They are extremely useful for frequency counting and fast lookups.

``` python
person = {"name": "Sam", "age": 25}
person["name"]             # "Sam"
person["city"] = "Pune"    # add or update
del person["age"]          # delete key
person.get("age", 0)       # default if missing
"name" in person           # checks keys
len(person)
```

Looping:

``` python
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)
```

### Frequency counter pattern

``` python
nums = [1, 2, 2, 3, 2]
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1

# freq is {1: 1, 2: 3, 3: 1}
```

### Two Sum pattern

``` python
def two_sum(nums, target):
    seen = {}  # number -> index

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

    return []
```

**Important:** `if key in my_dict` checks keys, not values.

## 8. Conditions and loops

``` python
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

`for` loop:

``` python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(10, 0, -1):  # 10 down to 1
    print(i)
```

`range(start, stop, step)` excludes `stop`.

``` python
i = 0
while i < 5:
    print(i)
    i += 1
```

Loop control:

``` python
break       # exit the loop
continue    # skip to the next iteration
pass        # do nothing; placeholder
```

Reverse index traversal:

``` python
nums = [10, 20, 30]
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
```

The three range arguments mean: start at the last index, stop before
`-1` (so index `0` is included), and move backward by `1`.

## 9. Functions and recursion

``` python
def add(a, b):
    return a + b

answer = add(2, 3)  # 5
```

`print()` displays a value; `return` sends a value back to the caller.

Default parameters:

``` python
def greet(name="friend"):
    return f"Hello, {name}"
```

Multiple return values:

``` python
def min_max(nums):
    return min(nums), max(nums)

smallest, largest = min_max([3, 1, 8])
```

Recursion example:

``` python
def factorial(n):
    if n <= 1:             # base case
        return 1
    return n * factorial(n - 1)
```

Every recursive solution needs a base case that stops recursion.

Lambda (small anonymous function):

``` python
square = lambda x: x * x
```

## 10. Built-in functions worth knowing

``` python
len(nums)                  # length
sum(nums)                  # total
min(nums)                  # smallest
max(nums)                  # largest
sorted(nums)               # new sorted list
reversed(nums)             # reverse iterator
enumerate(nums)            # index-value pairs
range(5)                   # integer sequence
abs(-7)                    # 7
round(3.14159, 2)           # 3.14
all([True, True])           # True if every item is truthy
any([False, True])          # True if at least one is truthy
```

Other useful tools:

``` python
list(zip([1, 2], ["a", "b"]))  # [(1, 'a'), (2, 'b')]
```

`zip()` stops when the shortest iterable ends.

Safe min/max with possibly empty data:

``` python
max(nums, default=0)
```

## 11. Handy standard-library tools for DSA

Import these as needed; they are built into Python.

### `collections.Counter` --- count frequencies

``` python
from collections import Counter

counts = Counter("banana")
counts["a"]            # 3
counts.most_common(2)  # most frequent 2 items
```

Compare character frequencies:

``` python
from collections import Counter

Counter("listen") == Counter("silent")  # True
```

### `defaultdict` --- automatic default values

``` python
from collections import defaultdict

groups = defaultdict(list)
groups["fruit"].append("apple")
```

### `deque` --- efficient queue

``` python
from collections import deque

q = deque([1, 2, 3])
q.append(4)          # add right
q.appendleft(0)      # add left
q.pop()              # remove right
q.popleft()          # remove left
```

Use `deque` for BFS queues. Removing the first item of a normal list with `pop(0)` is usually inefficient.

### `heapq` --- priority queue / min-heap

``` python
import heapq

heap = [5, 1, 4]
heapq.heapify(heap)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)
```

Python's `heapq` is a min-heap. A common max-heap workaround for numbers is to push their negatives.

### `bisect` --- binary search positions in sorted lists

``` python
import bisect

nums = [1, 3, 3, 7]
bisect.bisect_left(nums, 3)   # 1: first insertion position
bisect.bisect_right(nums, 3)  # 3: after the last 3
```

### `math`

``` python
import math

math.gcd(12, 18)       # 6
math.ceil(2.1)         # 3
math.floor(2.9)        # 2
math.sqrt(25)          # 5.0
math.inf               # infinity
```

## 12. Common DSA patterns

### Two pointers

Use when working with sorted arrays, pairs, palindromes, or ends of a sequence.

``` python
left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        # found the pair
        break
    elif total < target:
        left += 1
    else:
        right -= 1
```

This particular movement rule assumes the list is sorted in ascending order.

### Sliding window

Useful for many contiguous subarray/substring problems.

``` python
left = 0
window_sum = 0

for right in range(len(nums)):
    window_sum += nums[right]

    while window_sum > target and left <= right:
        window_sum -= nums[left]
        left += 1

    # current window is nums[left:right + 1]
```

This example assumes non-negative numbers when shrinking based on
`window_sum > target`. Different problems need different window conditions.

### Binary search

Use on a sorted list or a search space with a suitable monotonic condition.

``` python
left, right = 0, len(nums) - 1

while left <= right:
    mid = left + (right - left) // 2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)  # loop ended without finding target
```

### Prefix sums

Useful for repeated range-sum calculations.

``` python
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)

# Sum of nums[left:right + 1]
range_sum = prefix[right + 1] - prefix[left]
```

### Stack

Useful for valid parentheses, next greater element, and monotonic-stack problems.

``` python
stack = []
stack.append(value)  # push
top = stack[-1]      # peek; only if non-empty
value = stack.pop()  # pop; only if non-empty
```

### BFS queue

``` python
from collections import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

## 13. Common algorithm helpers

Reverse a list in place:

``` python
nums.reverse()
```

Reverse without changing the original:

``` python
reversed_nums = nums[::-1]
```

Find unique values:

``` python
unique = list(set(nums))  # order is not guaranteed by this pattern
```

Remove duplicates while preserving order:

``` python
unique = list(dict.fromkeys(nums))
```

Swap values:

``` python
a, b = b, a
```

Check if a list is sorted:

``` python
is_sorted = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
```

Character frequency:

``` python
from collections import Counter
freq = Counter(text)
```

Flatten one level of nested lists:

``` python
flat = [item for row in matrix for item in row]
```

## 14. Big O quick reference

Typical average-case costs; exact costs can vary by operation and implementation.

Operation Typical time
  -------------------------------------- ----------------
`list[i]` access O (1)
List append at end Amortized O (1)
List insert/delete near beginning O (n)
Search with `x in list`                            O (n)
Sort a list O (n log n)
Dictionary lookup/insert Average O (1)
Set membership Average O (1)
`deque.append()` / `deque.popleft()`               O (1)
Binary search O (log n)

Space complexity measures extra memory used as input grows. For example, a frequency dictionary may use O (n) extra
space.

## 15. Common Python mistakes

1. **Using an index that doesn't exist**

   ``` python
   # Last valid index is len(nums) - 1
   nums[len(nums) - 1]
   ```

2. **Forgetting that the slice end is excluded**

   ``` python
   nums[0:3]  # indexes 0, 1, 2
   ```

3. **Confusing `append` and `extend`**

   ``` python
   a = [1, 2]
   a.append([3, 4])   # [1, 2, [3, 4]]
   a.extend([3, 4])   # [1, 2, 3, 4]
   ```

4. **Expecting `sort()` to return a list**

   ``` python
   nums.sort()        # modifies nums; returns None
   nums = sorted(nums)  # creates a sorted list
   ```

5. **Changing a list while iterating over it** Build a new list or iterate over a copy if you need to remove items.

6. **Using `is` to compare values** Use `==` for value equality. `is`
   checks object identity; it is commonly used for `x is None`.

7. **Forgetting dictionary keys must be hashable** Strings, numbers, and tuples of hashable values can be keys; lists
   cannot.

8. **Returning too early** Check whether the problem requires one answer, all answers, or a count before placing
   `return` inside a loop.

9. **Off-by-one errors** Carefully check `left < right` versus
   `left <= right`, and whether `right` is inclusive.

10. **Empty input** Consider `[]`, `""`, one-element inputs, duplicates, negative numbers, and no-solution cases.

## 16. LeetCode Python function template

LeetCode usually provides the class and method signature. Keep the required signature unchanged.

``` python
class Solution:
    def example(self, nums: list[int], target: int) -> int:
        # Write your logic here
        return -1
```

For older Python versions, you may see `List[int]` with
`from typing import List`. Follow the version and signature shown by the platform.

Quick test outside LeetCode:

``` python
def example(nums, target):
    # temporary implementation
    return target in nums

print(example([1, 2, 3], 2))  # True
```

## 17. Mini lookup table

If you need to... Try...
  --------------------------------- ----------------------------------
Count items                       `Counter(items)` or a dictionary Check if seen before              `seen = set()`
Add one item to a list            `append(x)`
Add multiple items                `extend(items)`
Remove last list item             `pop()`
Sort without modifying original   `sorted(items)`
Get index and value               `enumerate(items)`
Loop through two lists together   `zip(a, b)`
Make a reversed copy              `items[::-1]`
Queue for BFS                     `deque()`
Get smallest item repeatedly      `heapq`
Binary-search insertion point     `bisect`
Count characters                  `Counter(text)`
Convert string to characters      `list(text)`
Join strings                      `"".join(parts)`

------------------------------------------------------------------------

**Practice tip:** Try to understand the operation rather than memorizing every method. When solving a problem, first
identify the data structure or pattern you need, then use `Ctrl + F` in this file to look up the syntax.
