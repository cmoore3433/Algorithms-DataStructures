def mergeSortStart(array):
    temp=[]
    temp=array[:]
    mergeSort(array, temp, 0, len(array)-1)


def mergeSort(array, temp, start, end):
    if start < end:
        mid=abs((start+end)//2)
        mergeSort(array, temp, start, mid)
        mergeSort(array, temp, mid+1, end)
        merge(array, temp, start, mid, end)


def merge(array, temp, start, mid, end):
    i=start
    j=mid+1
    for k in range(start,end+1):
        temp[k] = array[k]

    for k in range(start,end+1):
        if i>mid:
            array[k]=temp[j]
            j=j+1
        elif j>end:
            array[k]=temp[i]
            i=i+1
        elif temp[j]<temp[i]:
            array[k]=temp[j]
            j=j+1
        else:
            array[k]=temp[i]
            i=i+1
            
