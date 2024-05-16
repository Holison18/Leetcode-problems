class Solution(object):
    def crawlerLogFolder(self, logs):
       
        stack = [] # create a variable to store the current state or folder
        for log in logs:
            if log == "../":
                if len(stack) != 0:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)


mySoln = Solution()
print(mySoln.crawlerLogFolder(["d1/", "d2/", "../", "d21/", "./"]))
print(mySoln.crawlerLogFolder(["d1/","d2/","./","d3/","../","d31/"]))
print(mySoln.crawlerLogFolder(["d1/","../","../","../"]))
