"""
lass Solution:
    def climbStairs(self, n: int) -> int:
        d =[]
        if n ==0:
            return 0
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [1 for i in range(n+1)]
        print(dp)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

test1 =Solution().climbStairs(1)
print(test1)
        

