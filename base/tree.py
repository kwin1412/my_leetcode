
from cgitb import reset


class Queue:
    """
    example:
        q=Queue()
        nums=[1,2,3,4,5,6,7,8,9,10]
        for num in nums:
            q.pop(num)
        for num in nums:
            print(q.push())

    """
    q=[]
    def __init__(self) -> None:
        pass

    def pop(self,val):
        self.q.append(val)

    def push(self):
        val=self.q[0]
        self.q=self.q[1:]
        return val



class Tree:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
        pass




nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None,None,16]
def tree_init(nums)->Tree:
    """
    tree:
        preorder init 
    """
    
    root=None
    q=Queue()
    root = Tree(nums[0])
    q.pop(root)

    for i in range(1,len(nums),2):
        p=q.push()
        if nums[i]!=None:
            p.left=Tree(nums[i])
            q.pop(p.left)
        else:
            p.left=None

        if i+1<len(nums):
            if nums[i+1]!=None:
                p.right=Tree(nums[i+1])
                q.pop(p.right)
            else:
                p.right=None

    return root

def preorder_traverse(root:Tree):
    if root==None:
        return

    print(root.val,end=" ")
    preorder_traverse(root.left)
    preorder_traverse(root.right)

def midorder_traverse(root:Tree):
    if root==None:
        return

    
    midorder_traverse(root.left)
    print(root.val,end=" ")
    midorder_traverse(root.right)

def postorder_traverse(root:Tree):
    if root==None:
        return
    postorder_traverse(root.left)
    postorder_traverse(root.right)
    print(root.val,end=" ")

"""
Test1:
    nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            1
       2          3
    4    5     6     7
   8 9 10 11 12 13 14 15

    preorder:
        1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
    midorder:
        8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
    postorder:
        8 9 4 2 10 11 5 2 12 13 14 15 7 3 1

Test2:
    nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None,None,16]
                  1
           2             3
       4       5      6     7
    8     9  10 11  12 13  14 15
   N N 16

    preorder:
        1 2 4 8 9 16 5 10 11 3 6 12 13 7 14 15
    midorder:
        8 4 16 9 2 10 5 11 1 12 6 13 3 14 7 15
    postorder:
        8 16 9 4 10 11 5 2 12 13 6 14 15 7 3 1

Example:
    nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None,None,16]
    root=tree_init(nums)
    preorder_traverse(root)
    print()
    midorder_traverse(root)
    print()
    postorder_traverse(root)
"""

def depth_traverse(root):
    global res
    global depth

    if root==None:
        return
    
    depth+=1
    if root.left==None and \
        root.right==None:
        res=max(depth,res)
    depth_traverse(root.left)
    depth_traverse(root.right)
    depth-=1
    

def max_depth(root):
    global res
    global depth
    res=0
    depth=0
    depth_traverse(root)

    return res

"""
tree max depth :
    Example:
        nums=[3,9,20,None,None,15,7]
        root=tree_init(nums)
        print(max_depth(root))

    Output:
        3
"""

if __name__=="__main__":
    pass


