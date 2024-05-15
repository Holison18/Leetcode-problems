class Solution(object):
    def CalPoints(self, operations):
        record  = []
        for element in operations:
            if element.lstrip('-').isdigit():
                record.append(int(element))
            elif element == '+':
                record.append(record[-1] + record[-2])
            elif element == 'D':
                record.append(2 * record[-1])
            elif element == 'C':
                record.pop()
        return sum(record)
    

mySoln = Solution()
print(mySoln.CalPoints(['5','2','C','D','+']))
print(mySoln.CalPoints(["5","-2","4","C","D","9","+","+"]))
print(mySoln.CalPoints(["1","C"]))

            



