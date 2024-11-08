# Python_interview_Questions_Hackerrank
Python Interview Questions Hackerrank

**#Question1-Array Segment Reversal**
**#Problem Statement:****
Given an integer array arr and a list of operations operations, each operation specifies a segment of arr to reverse. The operations list is a 2D integer array where each element operations[i] contains two integers:

operations[i][0]: the starting index of the segment (inclusive).
operations[i][1]: the ending index of the segment (inclusive).
Your task is to reverse the specified segments of the array in the order they are given in operations and return the modified array.

**#Explanation of the Code**
The function performOperations(arr, operations) takes an array and a list of operations. Each operation is a list containing two indices [left, right].
For each operation, it reverses the subarray from index left to right using Python slicing.
The test cases are then executed with their respective inputs, and the results are printed out.

**Testcase1-Basic test case**
arr = [0, 1, 2, 3, 4]
operations = [[1, 3]]
Expected Output: [0, 3, 2, 1, 4]
Explanation: Reverse the subarray from index 1 to 3, resulting in [0, 3, 2, 1, 4].
**Testcase2-Multiple Reversals**
arr = [1, 2, 3, 4, 5]
operations = [[1, 3], [0, 4]]
Expected Output: [5, 4, 3, 2, 1]
Explanation: First, reverse [2, 3, 4] to get [1, 4, 3, 2, 5]. Then reverse the entire array, resulting in [5, 4, 3, 2, 1].
**Testcase3-Reverse Entire Array**
arr = [9, 8, 7, 6]
operations = [[0, 3]]
Expected Output: [6, 7, 8, 9]
Explanation: Reverse the entire array from index 0 to 3.
**Testcase4-Single Element Array**
arr = [42]
operations = [[0, 0]]
Expected Output: [42]
Explanation: A single-element array remains unchanged regardless of the operation.
**Testcase5-No Operations**
arr = [1, 2, 3]
operations = []
Expected Output: [1, 2, 3]
Explanation: No operations, so the array remains unchanged.
**Testcase6-Consecutive Segment Reversals**
arr = [1, 2, 3, 4, 5, 6]
operations = [[1, 4], [2, 3]]
Expected Output: [1, 5, 4, 3, 2, 6]
Explanation: First reverse [2, 3, 4, 5] to get [1, 5, 4, 3, 2, 6], then reverse [4, 3], which does not change the array further.
**Testcase7-Overlapping Reversals**
arr = [10, 20, 30, 40, 50, 60]
operations = [[0, 2], [1, 4]]
Expected Output: [30, 50, 40, 20, 10, 60]
Explanation: First reverse [10, 20, 30] to get [30, 20, 10, 40, 50, 60], then reverse [20, 10, 40, 50] to obtain the final output.

**Question2-Counting duplicate products**
**Problem**
Given three arrays: name, price, and weight, each describing a list of products where:

name[i] is the name of the product.
price[i] is the price of the product.
weight[i] is the weight of the product.
Two products are considered duplicates if they have the same name, price, and weight. 
The goal is to count the number of such duplicate products.
Explanation of the Code
The function numDuplicates(name, price, weight) takes three arrays as input and uses a set to track unique products represented as tuples.
Each product is represented as a tuple (name[i], price[i], weight[i]).
If a product tuple is already in the set, it is counted as a duplicate.
The function returns the total count of duplicate products.

**Testcase1-Basic Test Case**

Input: ["ball", "bat", "glove", "glove", "glove"], [2, 3, 1, 1, 1], [2, 5, 1, 1, 1]
Expected Output: 1 duplicate (glove, 1, 1 appears twice)
Explanation:
We have the following products:
Product 1: ("ball", 2, 2)
Product 2: ("bat", 3, 5)
Product 3: ("glove", 1, 1)
Product 4: ("glove", 1, 1) — Duplicate of Product 3
Product 5: ("glove", 1, 1) — Duplicate of Product 3
Product 3 is duplicated twice (Products 4 and 5), so we count them as duplicates.

**Testcase2-No Duplicates**

Input: ["apple", "banana", "cherry"], [5, 6, 7], [1, 2, 3]
Expected Output: 0 duplicates
Explanation:
We have the following products:
Product 1: ("apple", 5, 1)
Product 2: ("banana", 6, 2)
Product 3: ("cherry", 7, 3)
All products are unique in terms of name, price, and weight.

**Testcase3-All Elements are Duplicates**

Input: ["pen", "pen", "pen"], [1, 1, 1], [1, 1, 1]
Expected Output: 2 duplicates
Explanation:
We have the following products:
Product 1: ("pen", 1, 1)
Product 2: ("pen", 1, 1) — Duplicate of Product 1
Product 3: ("pen", 1, 1) — Duplicate of Product 1
Product 1 is duplicated twice (Products 2 and 3).

**Testcase4-Single Product**

Input: ["notebook"], [10], [5]
Expected Output: 0 duplicates
Explanation:
We only have one product:
Product 1: ("notebook", 10, 5)
Since there's only one product, there can't be any duplicates.

**Testcase5-Mixed Products with some duplicates**

Input: ["phone", "tablet", "phone", "tablet", "laptop"], [500, 300, 500, 350, 800], [200, 150, 200, 150, 700]
Expected Output: 1 duplicate (phone, 500, 200 appears twice)
Explanation:
We have the following products:
Product 1: ("phone", 500, 200)
Product 2: ("tablet", 300, 150)
Product 3: ("phone", 500, 200) — Duplicate of Product 1
Product 4: ("tablet", 350, 150) — Not a duplicate (different price)
Product 5: ("laptop", 800, 700)
Product 1 is duplicated once (by Product 3).

**Testcase6-Edge Case with large inputs (no duplicates)**

Input: Names: ["item0", "item1", ..., "item999"], Prices: [0, 1, ..., 999], Weights: [0, 1, ..., 999]
Expected Output: 0 duplicates
Explanation:
We have 1000 unique products, each with distinct names, prices, and weights.
Since all products have unique attributes, there are no duplicates.

**Testcase7-Duplicate Names with different attributes**

Input: ["chair", "chair", "chair"], [20, 20, 25], [5, 10, 5]
Expected Output: 0 duplicates (all attributes are different)
Explanation:
We have the following products:
Product 1: ("chair", 20, 5)
Product 2: ("chair", 20, 10) — Not a duplicate (different weight)
Product 3: ("chair", 25, 5) — Not a duplicate (different price)
None of the products are duplicates since the attributes are different.

