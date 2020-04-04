"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        if x == 1 or x == 2 or x == 3:
            return int(1)
        for i in range(1,x//2+1):
            if (i+1)*(i+1)>x:
                return i 
"""

class Solution:
    # @param x, an integer
    # @return an integer
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x ==1 or x==2 or x==3:
            return 1
        i = 1; j = int(x / 2 + 1)
        while( i <= j ):
            center = ( i + j ) / 2
            if center ** 2 == x:
                return int(center)
            elif center ** 2 > x:
                j = int(center)
            elif i == int(center):
                i += 1
            else:
                i = int(center)
            if (i+1)**2 > x:
                return int(i)


test1=Solution().mySqrt(6)
print(test1)