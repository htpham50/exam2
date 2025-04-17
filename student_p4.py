"""
Write a Python function "trim_string" that takes in a string as well as a prefix and suffix lengths. 
Using string slicing, the function should return a trimmed string with the prefix and suffix removed.

Make sure the sliced words do not include any leading or trailing space characters.
If the combined prefix and suffix is longer than the string, return an empty string.

Demonstrate the usage of the function to convert the string  "    Funny " to "Fun", save the return value of this call in a variable named "trimmed". 

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE
def trim_string(input_string, prefix_length, suffix_length):
    # Strip leading and trailing spaces
    stripped_string = input_string.strip()
    # Check if prefix and suffix length exceeds the length of the string
    if prefix_length + suffix_length >= len(stripped_string):
        return ""
    # Perform the slicing to remove prefix and suffix
    return stripped_string[prefix_length:len(stripped_string) - suffix_length]

# Demonstrating the usage of the function
original_string = "    Funny "
trimmed = trim_string(original_string, 0, 3)
print(f'Trimmed result: "{trimmed}"')








#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
words = "trim me"
expected = "m m"
result = trim_string(words, 3, 1)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
words = "     Good morning!  "
expected = "Good morni"
result = trim_string(words, 2, 5)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 3
ntestcases+=1
words = "ABCD"
expected = ""
result = trim_string(words, 5, 5)
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 4
ntestcases+=1
expected = "Fun"
result = trimmed
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")