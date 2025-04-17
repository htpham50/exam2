"""
Define a function named "swap" that swaps the first half of its string argument with its second half and returns the result.
If the length of the string is odd, the character in the middle of the string must remain in place.
You must use string slicing and concatenation to perform the task.

For example:
If the argument is "abcd", the function should return "cdab"
Notice that "cd" and "ab" swap places.

If the argument is "abcde", the function should return "decab"
Notice that "de" and "ab" swap places but "c" remains in place.

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE

def swap(s):
    if len(s) % 2 == 0:
        mid = len(s) // 2
        return s[mid:] + s[:mid]
    else:
        mid = len(s) // 2
        return s[mid + 1:] + s[mid] + s[:mid]














#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
expected="cdab"
result = swap("abcd")
passed = result == expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 1
ntestcases+=1
expected="decab"
result = swap("abcde")
passed = result == expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")