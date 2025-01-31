# 各種題目型態

## Island: 
- 0130  Surrounded Regions         //BFS, DFS
- 0200  Number of Islands          //BFS, DFS, UnionFind 
- 0221  Maximal Square
- 0694  Number of Distinct Islands //BFS, DFS
- 0695  Max Area of Island         //BFS, DFS


## Interval:
- 0252  Meeting Rooms
- 0253  Meeting Rooms II

## Palindrome:
- 0005  Longest Palindromic Substring
- 0131  Palindrome Partitioning
- 0409  Longest Palindrome （組成）
- 0647  Palindromic Substrings //DP (good)

## Increasing:
- 0300  Longest Increasing Subsequence //DP, BS （維護一個tail array)
- 0491  Increasing Subsequences
- 0674  Longest Continuous Increasing Subsequence (連續)
- 1143  Longest Common Subsequence //還沒寫

## Sliding Window: 
- 0076  Minimum Window Substring
- 0239  Sliding Window Maximum

## Data Stucture 
- 0146  LRU Cache
- 0155  Min Stack (只可查最值)
- 0170  Two Sum III - Data structure design
- 0208  Implement Trie
- 0705  Design HashSet
- 0706  Design HashMap
- 0716  Max Stack (可查且pop最值)
- 0981  Time Based Key-Value Store

## Game
- 0055  Jump Game
- 0877  Stone Game
- 0994  Rotting Oranges 

## Word系列
- 0139  Word Break
- 0290  Word Pattern
- 0291  Word Pattern II

## Knight系列
- 0688  Knight Probability in Chessboard
- 0935  Knight Dialer
- 1197  Minimum Knight Moves  

## Shortest Path系列
- 0743  Network Delay Time (shortest path)
- 0787  Cheapest Flights Within K Stops (shortest path + 站數限制)

<br>

# 各種解法

## Two Pointer
- 0011  Container With Most Water

## Binary Search 

### Type 1 (基本)
- 0704  Binary Search  //最基本，包含找任意值，找最初，找最後 [Type1]

### Type 2 (XXOO)
- 0153  Find Minimum in Rotated Sorted Array //旋轉找極值 [Type2]
- 0852  Peak Index in a Mountain Array //找左半最後或找右半最左 [Type2]
- 
### Type 3 (一半一半)
- 0033  Search in Rotated Sorted Array //旋轉找值 [Type3]
- 0081  Search in Rotated Sorted Array II //旋轉找值，可能有重複
- 0162  Find Peak Element //沒有排序的數列 [Type3]
- 0240  Search a 2D Matrix II
- 
### Type 4 (二分答案)
- 1300  Sum of Mutated Array Closest to Target //[Type4]


## BFS必做
- 0127  Word Ladder
- 0210  Course Schedule II
- 0490  The Maze


## DFS必做
- 0113  Path Sum II

## Backtracking必做
- 0046  Permutations
- 0051  N-Queens
- 0077  Combinations
- 0078  Subsets

## DP必做
- 0064  Minimum Path Sum
- 0118  Pascal's Triangle
- 0120  Triangle   //change to buttom-up DP
- 0152  Maximum Product Subarray
- 0647  Palindromic Substrings //DP (good)
- 0718  Maximum Length of Repeated Subarray
- 1048  Longest String Chain //Bottom-up not yet
- 1143  Longest Common Subsequence (LCS) //Memoization, Tabulation 


## DP必做 (Memoization)
- 0322  Coin Change
- 0576  Out of Boundary Paths

# Tree 
- 0366  Find Leaves Of Binary Tree //可以從下方開始編號（使用height)
