#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo=[]
        for i in range(len(nums)):
            memo.append(1)

        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    memo[i]=max(memo[i],memo[j]+1)
        res=0
        for i in range(len(nums)):
            res=max(res,memo[i])
        return res
# @lc code=end

