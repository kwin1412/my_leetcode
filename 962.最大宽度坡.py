#
# @lc app=leetcode.cn id=962 lang=python3
#
# [962] 最大宽度坡
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0

        for i in range(n):
            for j in range(n-1,i,-1):
                if nums[i]<=nums[j]:
                    ans=max(ans,j-i)
        return ans
# @lc code=end

