

class LinkNode():
    def __init__(self,val,next=None) -> None:
        self.val=val
        self.next=next

        pass


def link_list_init():
    nums=[1,2,3,4,5,6,7,8,9,10,11,12]
    p=None
    for num in nums:
        if p==None:
            head=LinkNode(val=num)
            p=head
        else:
            p.next=LinkNode(val=num)
            p=p.next
    return head

    
def preorder_traverse(head:LinkNode):
    """
    前序遍历，链表顺序输出
    """
    if head==None:
        return
    
    print(head.val)
    preorder_traverse(head.next)
    # print(head.val)

def postorder_traverse(head:LinkNode):
    """
    后序遍历，链表顺序输出
    """
    if head==None:
        return
    
    
    postorder_traverse(head.next)
    print(head.val)
    # print(head.val)

"""
link list example:
    head=link_list_init()
    preorder_traverse(head)
    postorder_traverse(head)
"""



if __name__=="__main__":
    head=link_list_init()
    preorder_traverse(head)
    postorder_traverse(head)


