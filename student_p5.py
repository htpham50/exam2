"""
Create a "Sentence" class that is constructed with a string argument, splits it into words, and counts how many times each word appears (all computation must be done at object creation/initialization).
In addition, the class should have a method named "words" which returns the list of unique words, sorted alphabetically.
It should also have a method named "freq" which takes in a word as argument returns the frequency of that word (the frequency of a word that does not exist is 0)

Make sure to run your code and review the test cases.
The code must pass all test cases for full credit.
"""

#YOUR CODE BEGINS HERE
class Sentence:
    def __init__(self, text):
        self.word_counts = {}
        words = text.split()
        for word in words:
            self.word_counts[word] = self.word_counts.get(word, 0) + 1
    
    def words(self):
        return sorted(self.word_counts.keys())
    
    def freq(self, word):
        return self.word_counts.get(word, 0)













#YOUR CODE ENDS HERE

"""
Do NOT modify any code below this comment block.
"""

ntestcases=0
npass=0

#Test Case 1
ntestcases+=1
expected = ["cats", "dogs"]
s = Sentence("dogs cats cats")
result = s.words()
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 2
ntestcases+=1
expected = 2
s = Sentence("dogs cats cats")
result = s.freq("cats")
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

#Test Case 3
ntestcases+=1
expected = 0
s = Sentence("dogs cats cats")
result = s.freq("bats")
passed = result==expected
npass += passed 
print(f"{'PASS' if passed else 'FAIL'} [Test Case {ntestcases}]\nExpected: {expected}\nFound: {result}")

print(f"Passed {npass} of {ntestcases} tests")