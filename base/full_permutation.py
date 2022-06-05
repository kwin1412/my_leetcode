

"""
回溯全排列
"""

nums=[1,2,3,4,5,6,7,8,9,10]
used=[0]*len(nums)
res=[]
count=0

def backtrack(nums):
    global count
    if len(res)==len(nums):
        print(res)
        count+=1
        return

    for i in range(len(nums)):
        if used[i]==1:
            continue

        res.append(nums[i])
        used[i]=1

        backtrack(nums)

        del(res[-1])
        used[i]=0


def full_permutation_count(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans

if __name__=="__main__":
    backtrack(nums)
    print(count)
    print(full_permutation_count(len(nums)))