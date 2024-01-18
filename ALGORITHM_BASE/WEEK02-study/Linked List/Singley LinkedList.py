class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


head_node=ListNode(1)
head_node.next=ListNode(2)
head_node.next.next=ListNode(3)
head_node.next.next.next=ListNode(4)


#itreable
def printNodes(node:ListNode):
    crnt_node=node
    while crnt_node is not None:
        print(crnt_node.val, end='')
        crnt_node=crnt_node.next

#recur
def printNodeRecur(node:ListNode):
    print(node.val,end='')
    if node.next is not None:
        printNodeRecur(node.next)



printNodes(head_node)
print()
printNodeRecur(head_node)