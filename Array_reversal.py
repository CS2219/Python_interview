#Array Segment Reversal
#Problem Statement:
#Given an integer array arr and a list of operations operations, each operation specifies a segment of arr to reverse. The operations list is a 2D integer array where each element operations[i] contains two integers:operations[i][0]: the starting index of the segment (inclusive).
#operations[i][1]: the ending index of the segment (inclusive).
#Your task is to reverse the specified segments of the array in the order they are given in operations and return the modified array.
#Constraints:
#•	1≤len(arr)≤1031 \leq \text{len}(arr) \leq 10^31≤len(arr)≤103
#•	0≤arr[i]≤1030 \leq \text{arr}[i] \leq 10^30≤arr[i]≤103
#•	0≤operations[i][0]≤operations[i][1]<len(arr)0 \leq \text{operations}[i][0] \leq \text{operations}[i][1] < \text{len}(arr)0≤operations[i][0]≤operations[i][1]<len(arr)

def performOperations(arr, operations):
    # Loop through each operation in the given order
    for op in operations:
        left, right = op  # Extract the left and right indices for the current operation
        # Reverse the segment of the array from `left` to `right` (inclusive)
        arr[left:right+1] = arr[left:right+1][::-1]
    return arr

def performOperations(arr, operations):
    for op in operations:
        left, right = op
        arr[left:right+1] = arr[left:right+1][::-1]
    return arr

# Test Case 1: Basic Test Case (Single Reversal)
arr1 = [0, 1, 2, 3, 4]
operations1 = [[1, 3]]
result1 = performOperations(arr1[:], operations1)
print(f"Test Case 1 - Input: {arr1}, Operations: {operations1}, Result: {result1}")

# Test Case 2: Multiple Reversals
arr2 = [1, 2, 3, 4, 5]
operations2 = [[1, 3], [0, 4]]
result2 = performOperations(arr2[:], operations2)
print(f"Test Case 2 - Input: {arr2}, Operations: {operations2}, Result: {result2}")

# Test Case 3: Reverse Entire Array
arr3 = [9, 8, 7, 6]
operations3 = [[0, 3]]
result3 = performOperations(arr3[:], operations3)
print(f"Test Case 3 - Input: {arr3}, Operations: {operations3}, Result: {result3}")

# Test Case 4: Single Element Array
arr4 = [42]
operations4 = [[0, 0]]
result4 = performOperations(arr4[:], operations4)
print(f"Test Case 4 - Input: {arr4}, Operations: {operations4}, Result: {result4}")

# Test Case 5: No Operations
arr5 = [1, 2, 3]
operations5 = []
result5 = performOperations(arr5[:], operations5)
print(f"Test Case 5 - Input: {arr5}, Operations: {operations5}, Result: {result5}")

# Test Case 6: Consecutive Segment Reversals
arr6 = [1, 2, 3, 4, 5, 6]
operations6 = [[1, 4], [2, 3]]
result6 = performOperations(arr6[:], operations6)
print(f"Test Case 6 - Input: {arr6}, Operations: {operations6}, Result: {result6}")

# Test Case 7: Overlapping Reversals
arr7 = [10, 20, 30, 40, 50, 60]
operations7 = [[0, 2], [1, 4]]
result7 = performOperations(arr7[:], operations7)
print(f"Test Case 7 - Input: {arr7}, Operations: {operations7}, Result: {result7}")
