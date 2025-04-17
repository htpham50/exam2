"""
Define a class named Set.

Instance variables: A dictionary to store the elements of the set.
Instance methods:
__init__: Initializes the dictionary
add(val): Adds a new element val to the set if it doesn’t already exist.
find(val): Return True if the element val exists in the set, and False otherwise.

Create a Set object named "my_set" and invoke the add method twice to add the values 1 and 5 to the set.

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE
class Set:
    def __init__(self):
        self.elements = {}
    
    def add(self, val):
        if val not in self.elements:
            self.elements[val] = True
    
    def find(self, val):
        return val in self.elements

my_set = Set()
my_set.add(1)
my_set.add(5)
















#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
expected = [True, True]
result = [my_set.find(1), my_set.find(5)]
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
expected = [False]
result = [my_set.find(2)]
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 3
ntestcases+=1
my_set.add(2)
expected = [True, True, False]
result = [my_set.find(2), my_set.find(5), my_set.find(4)]
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")