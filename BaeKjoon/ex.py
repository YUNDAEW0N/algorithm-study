def bubblesort(arr,size: int):
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp



T=int(input())
arr=[]

for i in range(T):
    n=int(input())
    arr.append(n)


bubblesort(arr,5)
print(arr)