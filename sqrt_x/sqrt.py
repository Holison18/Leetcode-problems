class solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            low  = 0
            high = x

            # run the code until the desired value is found
            while low < high:
                mid = (low + high) // 2
                square = mid * mid

                if square == x:
                    return mid
                elif square < x:
                    low = mid + 1
                else:
                    high = mid
            return low - 1
        
    

mySoln  = solution()
print(mySoln.mySqrt(16))  # 4
print(mySoln.mySqrt(8))  # 2


