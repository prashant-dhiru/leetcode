# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        x = 2 
        
        while(x < n):
            dp[x] = dp[x-1] + dp[x-2]
            x+=1 

        return dp[n-1]