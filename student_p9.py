"""
Define a function L2_norm that takes in a list of numerical values and performs L2 normalization in place (modifying the original list).

Steps:
1-Calculate the sum of squares of each element in the list.
2-Compute the magnitude by taking the square root of this sum. Use the math.sqrt function.
3-Divide each element in the list by the magnitude and update each element with the resulting value.

You must use a for loop with a range object.
You must use the math.sqrt function to calculate the square root.
Your function must modify the contents of the original list (do not return a new list)

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE
import math

def L2_norm(lst):
    sum_of_squares = sum(x**2 for x in lst)
    
    magnitude = math.sqrt(sum_of_squares)
    
    for i in range(len(lst)):
        lst[i] = lst[i] / magnitude
        














#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
a = [0.6, 0.8]
b = [3,4]
L2_norm(b)

diff=0
for i in range(len(a)):
    diff+=(a[i]-b[i])**2

expected=0.0
result = diff
passed = result<=0.001
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
a = [0.707,0.707]
b = [1,1]
L2_norm(b)

diff=0
for i in range(len(a)):
    diff+=(a[i]-b[i])**2

expected=0.0
result = diff
passed = result<=0.001
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 3
ntestcases+=1
a = [0.267,0.535,0.802]
b = [1,2,3]
L2_norm(b)

diff=0
for i in range(len(a)):
    diff+=(a[i]-b[i])**2

expected=0.0
result = diff
passed = result<=0.001
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")


print(f"Passed {npass} of {ntestcases} tests")