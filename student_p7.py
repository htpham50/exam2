"""
Write a function named count_vowels that takes in a string argument and returns the number of vowels (aeiuo) in the string.
You must use a while loop to iterate over the string.
The string contains only lower case characters.

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    index = 0
    
    while index < len(s):
        if s[index] in vowels:
            count += 1
        index += 1
    
    return count 
















#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
s = "apple pie"
expected = 4
result = count_vowels(s)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
s = "bcdfg"
expected = 0
result = count_vowels(s)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 3
ntestcases+=1
s = "uioea"
expected = 5
result = count_vowels(s)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 4
ntestcases+=1
s = "uioeaaueio"
expected = 10
result = count_vowels(s)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")


print(f"Passed {npass} of {ntestcases} tests")