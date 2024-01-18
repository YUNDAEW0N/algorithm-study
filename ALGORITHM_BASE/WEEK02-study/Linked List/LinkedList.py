#링크드 리스트 구현해보기

class ListNode:
    # value 값과 next를 저장하는 노드만들기
    def __init__(self,val):
        self.val=val
        self.next=None


class SLinkedList:
    #노드 생성
    def __init__(self):
        self.head=None

    #노드의 헤드에 데이터 집어넣기  O(1)
    def addAtHead(self,val):
        node=ListNode(val)
        node.next=self.head
        self.head=node
    #노드의 맨 뒤에 데이터 집어넣기  O(n)
    def addBack(self,val):
        node=ListNode(val)
        crnt_node=self.head
        while crnt_node.next:
            crnt_node=crnt_node.next
        crnt_node.next=node
    #원하는 value 값의 데이터 찾기 O(n)
    def find(self,val):
        crnt_node=self.head
        while crnt_node is not None:
            if crnt_node.val==val:
                return crnt_node
            crnt_node=crnt_node.next
        raise RuntimeError('Node not found')
    #원하는 노드 뒤에 데이터 넣기 O(1)
    def addAfter(self,node,val):
        new_node=ListNode(val)
        new_node.next=node.next
        node.next=new_node
    #노드의 다음노드 삭제하기 O(1)
    def deleteAfter(self,prev_node):
        if prev_node.next is not None:
            prev_node.next=prev_node.next.next
        




#itreable
def printNodes(node:ListNode):
    crnt_node=node
    while crnt_node is not None:
        print(crnt_node.val, end='')
        crnt_node=crnt_node.next