#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start


class MyQueue:

    def __init__(self):
        self.popstack=[]
        self.pushstack=[]

    def push(self, x: int) -> None:
        self.pushstack.append(x)

    def pop(self) -> int:
        if len(self.popstack)==0 and len(self.pushstack)!=0:
            for i in range(len(self.pushstack)-1,-1,-1):
                self.popstack.append(self.pushstack[i])
            self.pushstack=self.pushstack[0:0]
        elif len(self.popstack)==0 and len(self.pushstack)==0:
            return -1

        v=self.popstack[-1]
        self.popstack=self.popstack[0:-1]
        return v

    def peek(self) -> int:
        if len(self.popstack)==0 and len(self.pushstack)!=0:
            for i in range(len(self.pushstack)-1,-1,-1):
                self.popstack.append(self.pushstack[i])
            self.pushstack=self.pushstack[0:0]
        elif len(self.popstack)==0 and len(self.pushstack)==0:
            return -1
        v=self.popstack[-1]
        return v

    def empty(self) -> bool:
        if len(self.popstack)==0 and len(self.pushstack)==0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

