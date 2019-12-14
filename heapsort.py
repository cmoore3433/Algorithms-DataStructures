def heapSort(array):
    n=len(array)
    buildMaxHeap(array, n)
    for i in range(len(array)-1, -1, -1):
        dex1=array[0]
        array[0]=array[i]
        array[i]=dex1
        n-=1
        maxHeapify(array, n, 0)
        
    
def buildMaxHeap(array, heapSize):
    for i in range(heapSize//2-1, -1, -1):
        maxHeapify(array, heapSize, i)
    
def maxHeapify(array, heapSize, i):
    l=2*i+1
    r=2*i+2
    if l<heapSize and array[l]>array[i]:
        largest=l
    else:
        largest=i
    if r<heapSize and array[r]>array[largest]:
        largest=r
    if i != largest:
        temp=array[i]
        array[i]=array[largest]
        array[largest]=temp
        maxHeapify(array, heapSize, largest)
