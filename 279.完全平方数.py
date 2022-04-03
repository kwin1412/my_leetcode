#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # def tab_count(d):
        #     if not hasattr(tab_count,"count"):
        #         tab_count.count=0
        #     tab_count.count+=d
        #     return tab_count.count

        memo=[float("inf")]*(n+1)
        def dp(m:int):
            import math
            # tab_count(1)
            # print("|"+"-"*tab_count.count*4,end=" ")
            # print("m=",m)

            # base case 
            if m < 0: 
                return -1
            if m == 0:
                return 0
            if memo[m]!=float("inf"):
                return memo[m]

            res = float("inf")
            for sq in range(1,math.isqrt(m)+1):
                sub_res=dp(m-sq**2)
                # tab_count(-1)

                if sub_res==-1:break
                res=min(sub_res+1,res)
            # print("res=",res)

            if res == float("inf"):
                memo[m]= -1
            else:
                memo[m]=res
            return memo[m]

        return dp(n)


# if __name__=="__main__":
#     s=Solution()
#     print(s.numSquares(2))

# @lc code=end

