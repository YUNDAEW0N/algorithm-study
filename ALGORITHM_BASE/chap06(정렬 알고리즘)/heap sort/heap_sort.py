# 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

# def heap_sort(a: MutableSequence)->None:
#     """힙 정렬"""

#     def down_heap(a: MutableSequence,left: int,right: int)->None:
#         """a[left]~a[right]를 힙으로 만들기"""
#         temp=a[left]         #루트

#         parent=left
#         while parent<(right+1)//2:
#             cl=parent*2+1   #왼쪽 자식
#             cr=cl+1         #오른쪽 자식
#             child=cr if cr<= right and a[cr]> a[cl] else cl   #큰값을 선택
#             if temp>=a[child]:
#                 break
#             a[parent]=a[child]
#             parent=child
#         a[parent]=temp

#     n=len(a)

#     for i in range((n-1)//2,-1,-1):     #a[i]~a[n-1]을 힙으로 만들기
#         down_heap(a,i,n-1)              #a[0]~a[i-1]을 힙으로 만들기

#     for i in range(n -1,0,-1):
#         a[0], a[i]=a[i],a[0]
#         down_heap(a,0,i-1)


def heap_sort(a: MutableSequence,size: int):
  
    #heapify
    #배열을 max heap으로 변경 -> heapify
    for i in range(size//2 -1, -1, -1):
        shiftDown(a,i,size)
    
    # heap_sort
    # N만큼 반복하면서 shiftDown
    for i in range(size-1, -1 , -1):
        a[0],a[i]=a[i],a[0]
        shiftDown(a,0,i)



def shiftDown(a,parent: int,size: int):
    left=2*parent+1
    right=left+1
    large=parent
    if left<size and a[left]>a[large]: large=left
    if right<size and a[right]>a[large]: large=right

    if large!=parent:
        temp=a[large]
        a[large]=a[parent]
        a[parent]=temp
        shiftDown(a,large,size)


     

a=[6,4,8,2,5,7,9,1,3,10]

heap_sort(a,10)

print(a)
