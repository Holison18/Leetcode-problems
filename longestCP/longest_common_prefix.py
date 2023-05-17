# This program checks the prefixes of a list of strings and returns the longest common prefix
class Solution:
    def longestCommonPrefix(self,strs) -> str:
        common_longest_prefix = ""
        if len(strs) == 0:
            return common_longest_prefix
        else:
            # find the shortest string in the list
            shortest_string = min(strs,key=len)
            for i in range(len(shortest_string)):
                for j in range(len(strs)):
                    # print(j)
                    if strs[j][i] != shortest_string[i]:
                        return common_longest_prefix
                common_longest_prefix += shortest_string[i]
            return common_longest_prefix


mysoln = Solution()
strs = ["flower","flow","flight"]
print(f"The longest common prefix is: {mysoln.longestCommonPrefix(strs)}")
strs = ["dog","racecar","car"]
print(f"The longest common prefix is: {mysoln.longestCommonPrefix(strs)}")