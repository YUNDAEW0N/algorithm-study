#머지소트로 풀어보기
import sys
input=sys.stdin.readline


def merge_sort(arr):
    if len(arr)<2:
        return arr
    
    mid=len(arr)//2
    low=merge_sort(arr[:mid])
    high=merge_sort(arr[mid:])

    temp=[]
    l=h=0

    while l <len(low) and h <len(high):
        if low[l]<high[h]:
            temp.append(low[l])
            l+=1
        else:
            temp.append(high[h])
            h+=1

    temp+=low[l:]
    temp+=high[h:]

    return temp

T=int(input())
s=[]

for i in range(T):
    n=int(input())
    s.append(n)


a = merge_sort(s)
for i in range(len(a)):
    print(a[i])