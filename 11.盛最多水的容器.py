#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        width=len(height)
        L=0
        R=len(height)-1
        for w in range(width-1,0,-1):
            if height[L]>height[R]:
                max_area=max(w*height[R],max_area)
                R-=1
            else:
                max_area=max(w*height[L],max_area)
                L+=1                
        return max_area

# @lc code=end

