

"""
回溯全排列
"""

nums=[1,2,3,4,5,6]
used=[0]*len(nums)
res=[]


def backtrack(nums):
    if len(res)==len(nums):
        return

    for i in range(len(nums)):
        if used[i]==1:
            continue

        res.append(nums[i])
        used[i]=1

        backtrack(nums)

        del(nums[-1])

