class solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        low  = 0
        high = x

        # run the code until the desired value is found
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
        
    

mySoln  = solution()
print(mySoln.mySqrt(16))  # 4
print(mySoln.mySqrt(8))  # 2


