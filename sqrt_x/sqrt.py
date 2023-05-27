class solution:
    def mySqrt(self, x: int) -> int:
        low  = 0
        high = x

        # run the code until the desired value is found
        while True:
            mid = (low + high)//2
            if mid * mid == x:
                break
            elif mid * mid < 16:
                low = mid
            else:
                high = mid
        return mid
    

mySoln  = solution()
print(mySoln.mySqrt(16))  # 4
print(mySoln.mySqrt(8))  # 2


