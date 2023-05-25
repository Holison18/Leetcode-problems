import random as rd
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        points = 0
        # generate a random integer
        while (points < k):
            random_int = rd.randint(1,maxPts)
            points += random_int



