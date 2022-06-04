#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)

        dp[0]=0
        for i in range(len(dp)):
            for coin in coins:
                if i -coin<0:
                    continue
                dp[i]=min(dp[i], 1 + dp[i - coin])
        if (dp[amount] == amount + 1):
            res=-1
        else:
            res=dp[amount]
        return res
# @lc code=end

