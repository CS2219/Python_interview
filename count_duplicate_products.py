#Problem Statement:
#You are given three arrays: name[], price[], and weight[], each of the same length n, where:
#name[i] represents the name of the i-th product.
#price[i] represents the price of the i-th product.
#weight[i] represents the weight of the i-th product.
#Two products are considered duplicates if they have the same name, price, and weight. Write a function to return the number of duplicate products in the list.

#Constraints:
#•	1≤n≤1031 \leq n \leq 10^31≤n≤103
#•	0≤price[i],weight[i]≤1030 \leq \text{price}[i], \text{weight}[i] \leq 10^30≤price[i],weight[i]≤103

def numDuplicates(name, price, weight):
    # Create a set to track unique products
    product_set = set()
    duplicates_count = 0

    # Iterate over all products
    for i in range(len(name)):
        # Create a tuple (name, price, weight) for each product
        product_tuple = (name[i], price[i], weight[i])

        # Check if this product already exists in the set
        if product_tuple in product_set:
            duplicates_count += 1
        else:
            product_set.add(product_tuple)
    
    return duplicates_count

# Test Case 1: Basic Test Case with duplicates
name1 = ["ball", "bat", "glove", "glove", "glove"]
price1 = [2, 3, 1, 1, 1]
weight1 = [2, 5, 1, 1, 1]
result1 = numDuplicates(name1, price1, weight1)
print(f"Test Case 1 - Names: {name1}, Prices: {price1}, Weights: {weight1}, Result: {result1}")

# Test Case 2: No Duplicates
name2 = ["apple", "banana", "cherry"]
price2 = [5, 6, 7]
weight2 = [1, 2, 3]
result2 = numDuplicates(name2, price2, weight2)
print(f"Test Case 2 - Names: {name2}, Prices: {price2}, Weights: {weight2}, Result: {result2}")

# Test Case 3: All Elements are Duplicates
name3 = ["pen", "pen", "pen"]
price3 = [1, 1, 1]
weight3 = [1, 1, 1]
result3 = numDuplicates(name3, price3, weight3)
print(f"Test Case 3 - Names: {name3}, Prices: {price3}, Weights: {weight3}, Result: {result3}")

# Test Case 4: Single Product
name4 = ["notebook"]
price4 = [10]
weight4 = [5]
result4 = numDuplicates(name4, price4, weight4)
print(f"Test Case 4 - Names: {name4}, Prices: {price4}, Weights: {weight4}, Result: {result4}")

# Test Case 5: Mixed Products with some duplicates
name5 = ["phone", "tablet", "phone", "tablet", "laptop"]
price5 = [500, 300, 500, 350, 800]
weight5 = [200, 150, 200, 150, 700]
result5 = numDuplicates(name5, price5, weight5)
print(f"Test Case 5 - Names: {name5}, Prices: {price5}, Weights: {weight5}, Result: {result5}")

# Test Case 6: Edge Case with large inputs (no duplicates)
name6 = ["item" + str(i) for i in range(1000)]
price6 = [i for i in range(1000)]
weight6 = [i for i in range(1000)]
result6 = numDuplicates(name6, price6, weight6)
print(f"Test Case 6 - Large Input with No Duplicates, Result: {result6}")

# Test Case 7: Duplicate Names with different attributes
name7 = ["chair", "chair", "chair"]
price7 = [20, 20, 25]
weight7 = [5, 10, 5]
result7 = numDuplicates(name7, price7, weight7)
print(f"Test Case 7 - Names: {name7}, Prices: {price7}, Weights: {weight7}, Result: {result7}")

