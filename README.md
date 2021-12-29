# LeetCode Problems

### Basics
- Search Algorithms
  - Linear Search
  - Binary Search
  - BFS
  - DFS
- Sort Algorithms
  - Bubble sort
  - Selection sort
  - Insertion sort
  - Shell sort
  - Merge sort
  - Heap sort
  - Quick sort
  - Count sort
  - Radix sort
  - Bucket sort
- Stack
- Queues
- Trees


### Search algorithms
#### [Linear Search Algorithm](Basics/Search/LinearSearch.py)
- **O(n) time complexity**

#### [Binary Search Algorithm](Basics/Search/BinarySearch.py)
- Data must be sorted!
- **O(logn) time complexity**

#### Breadth-First Search (BFS)
#### Depth-first search (DFS)

### Sort algorithms
https://visualgo.net/en/sorting

#### [Bubble sort](Basics/Sorting/BubbleSort.py)
- Works by repeatedly swapping the adjacent elements if they are in wrong order.
- In place algorithm
- **O(n<sup>2</sup>) time complexity**  - Quadratic

**Stable sort vs Unstable sort**
>Unstable sort: The order of same elements are not preserved.

#### [Selection sort](Basics/Sorting/SelectionSort.py)
- In place algorithm
- **O(n<sup>2</sup>) time complexity**  - Quadratic
- Better than bubble as it does less swapping
- Unstable algorithm

#### [Insertion sort]()
- In place algorithm
- **O(n<sup>2</sup>) time complexity**  - Quadratic
- Stable algorithm

#### [Shell sort]()
- Variation of Insertion sort
- Insertion sort chooses which element to insert using a gap of 1
- Shell Sort starts out using a larger gap value
- As the algorithm runs, the gap is reduced
- Goal is to reduce the amount of shifting required
- **Knuth** Sequence is the common gap value used : (3<sup>k</sup> - 1) / 2
- In place algorithm
- **Worst case is O(n<sup>2</sup>) time complexity** - Quadratic (but based on the gap sequence used)
- Doesnt require as much shifting as insertion sort, so it usually performs better
- Unstable algorithm

#### [Merge sort]()
- Divide and conquer algorithm
- Recursive algorithm
- Two phases : Splitting and merging
- Splitting phase leads to faster sorting during the merging phase
- Splitting is logical. We don't create new arrays
- Splitting phase
  - Start with unsorted array
  - Divide the arrays into 2 arrays, which are unsorted.
  - Split the left array and right array into 2 arrays each
  - Keep splitting until all the arrays have only one element each
- Merging Phase
  - Merge every left /right pair of sibling arrays into sorted array
  - Repeat until you have a single array
  - Not in place. Uses temporary arrays.
- Not a in-Place algorithm
- **O(nlogn)**
- Stable algorithm

#### [Quick sort]()
- Divide and conquer algorithm
- Recursive algorithm
- Uses a pivot element to partition the array into two parts
- elements < pivot to its left , elements > pivot to its right
- Pivot will then be in its correct sorted position
- the process is now repeated for the left array and right array
- Eventually every element has been the pivot so every element will be in its correct sorted position
- In-Place algorithm (unlike merge sort)
- **O(nlogn)**
- **Worst case is O(n<sup>2</sup>)**
- Unstable algorithm

#### [Count sort]()
- Makes assumptions about the data
- Doesn't use comparisons
- counts the number of occurrences of each value
- Only works with non-negative discrete values (cant work with floats,strings)
- Values must be a within specific range
- Not an in-place algorithm
- **O(n)** - can achieve this because we are making assumptions about the data we are sorting
- If we want the sort to be stable, we have to do some extra steps

#### [Radix sort]()
- Makes assumptions about the data
- Data must have same radix and width
- Data must be integers or strings
- Sort based on each individual letter or digit position
- Start at the rightmost position
- Must use a stable sort algorithm at each stage
- Counting sort is often used as sort algorithm for radix sort - must be stable counting sort
- **O(n)**
- Often runs slower than O(nlogn) algorithms because of the overhead involved
- In-Place algorithm depends on which sort algorithm used
- Stable algorithm

#### [Heap sort]()


#### [Bucket sort]()
- Distribute the items into buckets based on their hashed values(scattering phase)
- Sort the items in each bucket
- Merge the buckets (gathering phase)


### Stacks
- LIFO
- push, pop, peek
- **O(1)** for push, pop, and peek when using linked list
### Queues
- FIFO
- add - also called enqueue : adds at the end of the queue
- remove - also called as dequeue
- peek - to get 1st element
- Circular Queue

https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions

## 14 Patterns to Ace Any Coding Interview Question

>### https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed