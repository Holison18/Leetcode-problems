class solution:
    def mySqrt(self, x: int) -> int:
        low  = 0
        high = x

        # run the code until the desired value is found
        while low + 1 < high:
            mid = (low + high)//2
            square = mid * mid
            if abs(square) == 0.001:
                break
            elif square < x:
                low = mid
            else:
                high = mid
        return mid
    

mySoln  = solution()
print(mySoln.mySqrt(16))  # 4
print(mySoln.mySqrt(8))  # 2


