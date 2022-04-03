#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(nums: list[int],left:int,right:int):

            if left >= right:
                return
            # 基础在左边的话，先探测右边
            # 当只有两个数时[1,2]
            # 先探测左边，会把指针指向
            temp=nums[left]
            l=left
            r=right
            while l<r:
                # 必须要等于，不然的话当等于时就不前进了
                while nums[r]>=temp and l<r:
                    r-=1  
                while nums[l]<=temp and l<r:
                    l+=1
   
                if l<r:
                    t=nums[r]
                    nums[r]=nums[l]
                    nums[l]=t
            nums[left]=nums[l]
            nums[l]=temp

            quick_sort(nums,left,l-1)
            quick_sort(nums,r+1,right)

        
        quick_sort(nums,0,len(nums)-1)
        # nums.sort()
        return nums

if __name__=="__main__":
    s=Solution()
    nums=[9,8,7,6,5,4,3,2,1]
    print(s.sortArray(nums))

# @lc code=end

