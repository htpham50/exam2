"""
Write a function named filter that takes in three parameters:
source: a list of numerical values.
min_allowed: the minimum allowed value.
max_allowed: the maximum allowed value.
The function should return a new list containing only the elements from source that are within the range min_allowed and max_allowed, inclusive, sorted in ascending order. 

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE

def filter(source, min_allowed, max_allowed):
    newlist = []
    for i in source:
        if i >= min_allowed and i <= max_allowed:
            newlist.append(i)
            newlist.sort()
    return newlist














#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
a = [7,6,5,4,3,2,1]
expected = [3,4,5]
result = filter(a,3,5)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
a = [7,6,5,4,4,3,3,2,1]
expected = [2,3,3,4,4]
result = filter(a,2,4)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")