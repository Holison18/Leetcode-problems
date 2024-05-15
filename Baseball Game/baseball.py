class Solution(object):
    def CalPoints(self, operations):
        record  = []
        for element in operations:
            if element.isdigit():
                record.append(element)
            elif element == '+':
                new_record = record[record.index(element)] + record[record.index(element) - 1]
                record.append(new_record)
            elif element == 'D':
                new_record = 2 * record[record.index(element) - 1]
                record.append(new_record)
            elif element == 'C':
                record.pop()
        return sum(record)
    

mySoln = Solution()
print(mySoln.CalPoints(['5','2','C','D','+']))

            



