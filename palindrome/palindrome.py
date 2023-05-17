class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reverse the number and save in another variable
        if x < 0:
            return False
        else:
            reversed_x = str(x)[::-1]
            reversed_x = int(reversed_x)
            if reversed_x == x:
                return True
            else:
                return False
            


mysoln = Solution()
x = 121
print(f"Is {x} a palindrome? {mysoln.isPalindrome(x)}")
x = -121
print(f"Is {x} a palindrome? {mysoln.isPalindrome(x)}")
x = 10
print(f"Is {x} a palindrome? {mysoln.isPalindrome(x)}")
x = 101
print(f"Is {x} a palindrome? {mysoln.isPalindrome(x)}")
x = 0
print(f"Is {x} a palindrome? {mysoln.isPalindrome(x)}")