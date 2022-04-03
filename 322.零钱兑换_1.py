#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=[float("inf")]*(amount+1)
        def dp( n: int):
            # base ：when n is less than zero,no way to change
            # equal zero is ans
            if n <0:return -1
            if n == 0 :return 0

            # if memo table has value,do not compute
            # when memo[n] == -1,it means no way to coin change
            if memo[n]!=float("inf"):
                return memo[n]

            # bese case
            res=float("inf")

            # search each coin type,compute 
            for coin in coins:
                # compute each coin type
                sub_res=dp(n-coin)
                # if sub_res==-1,cannot change
                if sub_res==-1:continue
                res=min(res,sub_res+1)

            # if res ==float("inf"),any coin type has no way to change
            if  res ==float("inf"):
                memo[n]=-1
            else:
                # record compute result
                memo[n]=res
            # return result
            return memo[n]
        return dp(amount)
# @lc code=end

