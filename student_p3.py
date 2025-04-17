
"""
Define class Rectangle.
Rectangle class must contain:
2 instance variables: width and height.
2 instance methods: __init__ and area

__init__ takes in width and height as arguments to initialize the Rectangle object.
area does not take any arguments and returns the area of the Rectangle object(width*height) when invoked.

Create two instances of Rectangle named "a" and "b" 
a must be initialized with width 4 and height 3.
b must be initialized with width 2 and height 7.

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

a = Rectangle(4, 3)

b = Rectangle(2, 7)












#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
expected = 12
result = a.area()
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")


#Test Case 2
ntestcases+=1
expected = 14
result = b.area()
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")