#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
   
    def change(self, amount: int, coins: List[int]) -> int:
        a=amount
        c=len(coins)
        dp=[]
        for i in range(c+1):
            dp.append([0]*(a+1))

        for i in range(amount):
            for j in range(c):
                if i-coins[j]>=0:
                    dp[j][i]=max(dp[i-1][j]+)
        print(dp)

# @lc code=end

