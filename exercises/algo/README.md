# 1️⃣ Sorting Algorithms
### 📌 When to Use?

- When dealing with arrays, logs, or event ordering.
- When asked to sort or rank elements efficiently.
- When the problem involves finding the k-th largest/smallest element.
- When solving problems involving merging sorted data.

## 🔹 QuickSort (Best for General Sorting)
- Time Complexity: 🟢 O(n log n) (average), 🔴 O(n²) (worst case)
- Space Complexity: 🟢 O(log n)
- Use when: Sorting an unsorted array quickly and space is not a major constraint.

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))
```

## 🔹 MergeSort (Best for Large Datasets & Stability)
- Time Complexity: 🟢 O(n log n)
- Space Complexity: 🔴 O(n)
- Use when: You need stable sorting or are dealing with linked lists.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    while left and right:
        sorted_arr.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return sorted_arr + left + right

print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]))
```

# 2️⃣ Searching Algorithms
### 📌 When to Use?

- When you need to search for a target element efficiently.
- When the input is sorted.

## 🔹 Binary Search (Best for Sorted Data)
- Time Complexity: 🟢 O(log n)
- Use when: Searching in a sorted list.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 5))  # Output: 2
```

# 4️⃣ Graph Algorithms
### 📌 When to Use?

- When solving shortest path or connectivity problems.
- When working with social networks, routes, or dependencies.

## 🔹 Breadth-First Search (BFS) (Best for Shortest Path)
- Time Complexity: 🟢 O(V + E)
- ✅ Use BFS when you need the shortest path (e.g., "Find the shortest path in an unweighted graph").


```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

bfs(graph, "A")  # Output: A B C D E F
```

## 🔹 Depth-First Search (DFS) (Best for Exploring All Paths)
- Time Complexity: 🟢 O(V + E)
-  Use DFS when you need to traverse an entire graph (e.g., "Find all connected components in a graph").

```python
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

dfs(graph, "A")  # Output: A B D E F C
```

# 5️⃣ Dynamic Programming
### 📌 When to Use?

- When the problem involves overlapping subproblems and optimal substructure.
- When solving Knapsack, Fibonacci, or Edit Distance problems.

## 🔹 Fibonacci Sequence (Best for Recursive Optimization)
- Time Complexity: 🟢 O(n)

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(10))  # Output: 55
```

# 6️⃣ Greedy Algorithms
### 📌 When to Use?

- Task scheduling, load balancing, and optimizing costs in cloud environments.
## 🔹 Activity Selection (Best for Scheduling Problems)

```python
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort by finish time
    last_end_time = 0
    selected = []
    
    for start, end in activities:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end

    return selected

activities = [(1, 3), (2, 5), (4, 6), (6, 8)]
print(activity_selection(activities))
```

# 7️⃣ String Manipulation Algorithms
### 📌 When to Use?

- When solving problems involving substring search, pattern matching, or text parsing.

## 🔹 Sliding Window (Best for Finding Substrings)
- Time Complexity: 🟢 O(n)
- ✅ Use when the problem requires finding the longest substring with certain properties (e.g., "Find the longest substring with at most K distinct characters").

```python
def longest_substring(s, k):
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_substring("eceba", 2))  # Output: 3
```