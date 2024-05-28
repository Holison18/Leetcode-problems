class Solution(object):
    """To find the maximum repeating substring"""
    def maxRepeating(self, sequence: str, word: str) -> int:
        maximum_repeated = 0
        repeated_word = word
        while repeated_word in sequence:
            maximum_repeated += 1
            repeated_word += word
        return maximum_repeated
    

mySoln = Solution()
print(mySoln.maxRepeating("ababc","ab"))
print(mySoln.maxRepeating("ababc","ba"))
print(mySoln.maxRepeating("ababc","ac"))
print(mySoln.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba"))

