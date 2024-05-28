class Solution(object):
    """To find the maximum repeating substring"""
    def maxRepeating(self, sequence: str, word: str) -> int:
        maximum_repeating = sequence.count(word)
        return maximum_repeating
    

mySoln = Solution()
print(mySoln.maxRepeating("ababc","ab"))
print(mySoln.maxRepeating("ababc","ba"))
print(mySoln.maxRepeating("ababc","ac"))
