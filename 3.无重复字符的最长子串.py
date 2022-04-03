#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        if n==0:
            return 0

        max_res=0
        for i in range(n+1):
            d=dict()
            count=0
            for j in range(i,n):
                if s[j] in d.keys():
                    break
                else:
                    d[s[j]]=1
                    count+=1
            max_res=max(count,max_res)
        return max_res







# @lc code=end

