class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev_term = self.countAndSay(n - 1)

            current_term = ""
            count = 1
            for i in range(1, len(prev_term)):
                if prev_term[i] == prev_term[i - 1]:
                    count += 1
                else:
                    current_term += str(count) + prev_term[i - 1]
                    count = 1
            current_term += str(count) + prev_term[-1]

            return current_term


mySoln = Solution()
print(mySoln.countAndSay(1))  # 1
print(mySoln.countAndSay(2))  # 11
print(mySoln.countAndSay(4))  # 1211
