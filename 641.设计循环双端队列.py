#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.headqeue=[]
        self.tailqeue=[]
        self.maxlen=k

    def insertFront(self, value: int) -> bool:
        if len(self.headqeue)+len(self.tailqeue) >= self.maxlen:
            return False
        self.headqeue.append(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.headqeue)+len(self.tailqeue) >= self.maxlen:
            return False
        self.tailqeue.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.headqeue)+len(self.tailqeue)<=0:
            return False
        if len(self.headqeue)!=0:
            self.headqeue=self.headqeue[:-1]
            return True
        else:
            self.tailqeue=self.tailqeue[1:]
            return True

        

    def deleteLast(self) -> bool:
        if len(self.headqeue)+len(self.tailqeue)<=0:
            return False
        if len(self.tailqeue)!=0:
            self.tailqeue=self.tailqeue[:-1]
            return True
        else:
            self.headqeue=self.headqeue[1:]
            return True


    def getFront(self) -> int:
        if len(self.headqeue)+len(self.tailqeue)<=0:
            return -1
        if len(self.headqeue)!=0:
            return self.headqeue[-1]
        else:
            return self.tailqeue[0]


    def getRear(self) -> int:
        if len(self.headqeue)+len(self.tailqeue)<=0:
            return -1
        if len(self.tailqeue)!=0:
            return self.tailqeue[-1]
        else:
            return self.headqeue[0]

    def isEmpty(self) -> bool:
        if len(self.headqeue)+len(self.tailqeue)<=0:
            return True
        return False

    def isFull(self) -> bool:

        if len(self.headqeue)+len(self.tailqeue) == self.maxlen:
            return True
        return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

