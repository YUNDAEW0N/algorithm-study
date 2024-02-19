#include<stdio.h>

void heapSort(int *arr, int size);
void heapify(int *arr, int parendIdx,int size);

void heapSort(int *arr, int size)
{   
    int temp;

    // maxheap으로 heapify
    for (int i= (size>>1)-1; i>=0; i--)
    {
        heapify(arr , i , size);
    }

    for (int i= size-1 ; i > 0; i--)
    {
        temp= arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, 0, i);
    }
}

void heapify(int *arr, int parendIdx, int size)
{
    int leftIdx = (parendIdx<<1)+1;
    int rightIdx = leftIdx + 1;
    int largeIdx = -1;
    int temp;

    if (leftIdx < size)
        largeIdx = leftIdx;

    if (rightIdx < size && arr[largeIdx] < arr[rightIdx])
        largeIdx = rightIdx;

    if(largeIdx != -1 && arr[largeIdx] > arr[parendIdx])
    {
        temp = arr[largeIdx];
        arr[largeIdx] = arr[parendIdx];
        arr[parendIdx] = temp;
        heapify(arr,largeIdx,size);
    }
    
}


int main()
{
    int a[10]={6,4,8,2,5,10,9,1,3,7};
    int size = sizeof(a)/sizeof(int);
    printf ("before heapsort :[ ");
    for (int i = 0; i<size; i++)
    {
        printf("%d ",a[i]);
    }
    printf("]\n");
    heapSort(a,size);
    printf("after heapsort  :[ ");
    for ( int i =0; i<size;i++)
    {
        printf("%d ", a[i]);
    }
    printf("]\n");
}