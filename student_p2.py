"""
Write a function named unique that takes in a list as its only argument. 
The function should return a new list containing only the unique elements from the input list.

For example, the unique values in list [1,2,1,3,2] are [1,2,3].

You must utilize a dictionary in your function.

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE

def unique(lst):
    seen = {}
    for num in lst:
        seen[num] = True
    return list(seen.keys())








#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""


ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
a = [1,2,3]
expected = [1,2,3]
result = unique(a)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
a = [1,2,3,2,1]
expected = [1,2,3]
result = unique(a)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 3
ntestcases+=1
a = [1,1,1,1]
expected = [1]
result = unique(a)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")