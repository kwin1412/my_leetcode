#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for w in strs:
            key=tuple(sorted(w))
            if key not in d.keys():
                d[key]=[]
            d[key].append(w)

        ans=[]
        for key in d.keys():
            ans.append(d[key])
        return ans

# @lc code=end

