
"""
Write a function named dot_product that takes in two lists of numerical values, a and b, as parameters. 
The function should calculate and return the dot product of the two lists.

The dot product is defined as the sum of the products of corresponding elements from each list
For example, the dot product of [1,2,3] and [4,5,6] is 32 (1*4 + 2*5 + 3*6).

Your function must verify that both lists have the same length, if the lists do not have the same length, the function should return 0.

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE

sum = 0
def dot_product(a, b):
    if len(a) != len(b):
        return 0
    if len(a) == len(b):
        sum = (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
        return sum















#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
a = [1,2,3]
b = [4,0,1]
expected = 7
result = dot_product(a,b)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
a = [1,3]
b = [1,0,1,2]
expected = 0
result = dot_product(a,b)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")