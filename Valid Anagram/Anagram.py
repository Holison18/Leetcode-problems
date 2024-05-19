class Solution(object):
    def valid_anagram(self,s:str,t:str)->bool:
        # sort both s and t into separate variables
        sorted_s = sorted(s.lower())
        sorted_t = sorted(t.lower())

        if sorted_s == sorted_t:
            return True
        else:
            return False
    


mySoln = Solution()
print(mySoln.valid_anagram("anagram","nagaram"))
print(mySoln.valid_anagram("car","rat"))
print(mySoln.valid_anagram("a","ab"))
print(mySoln.valid_anagram("a","a"))