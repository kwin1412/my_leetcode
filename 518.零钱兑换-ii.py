#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
   
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(amount: int):
            if amount <0:
                return -1
            if amount==0:
                return 0

            for coin in coins:
                res=dp(amount-coin)
                if res==-1:continue
                if res==
                
        dp(amount)
        return self.ans

# @lc code=end

