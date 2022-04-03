#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.stack=[]
        self.freq_dict={}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.freq_dict.keys():
            self.freq_dict[val]=0
        self.freq_dict[val]+=1
        

    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        dd_list=sorted(self.freq_dict.items(),key=lambda x:x[1])
        print(dd_list)
        print(self.freq_dict)
        d=dd_list[-1][0]
        print(d)
        self.stack.remove(d)
        self.freq_dict[d]-=1
        return d

    def is_empty(self)->bool:
        if len(self.stack)==0:
            return True
        return False




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# if __name__=="__main__":
#     fs=FreqStack()
#     l=[2,2,3,4,5,6]
#     for i in l:
#         fs.push(i)
#     fs.pop()

# @lc code=end

