# 퀵 정렬 알고리즘 구현하기

from typing import MutableSequence

def qsort(arr: MutableSequence,left: int,right: int)->None:
    """a[left]~a[right]를 퀵정렬"""
    pl=left
    pr=right
    pivot=arr[(left+right)//2]

    while pl<=pr:
        while arr[pl]<pivot: pl+=1
        while arr[pr]>pivot: pr-=1
        if pl<=pr:
            arr[pl],arr[pr]=arr[pr],arr[pl]
            pl+=1
            pr-=1

    if left < pr: qsort(arr,left,pr)
    if pl<right: qsort(arr,pl,right)

arr=[]


for i in range(8):
    n=int(input())
    arr.append(n)

print(arr)
qsort(arr,0,7)
print(arr)