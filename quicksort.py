from statistics import median

def quickSortStart(array, p=0):
    r=len(array)-1
    if p<r:
        q=partition(array,p,r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)

def quickSort(array, p, r):
    if p<r:
        q=partition(array,p,r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)

def partition(array, p, r):
    x=array[r]
    i=p-1
    for j in range(p,r):
        if array[j]<=x:
            i=i+1
            temp=array[j]
            array[j]=array[i]
            array[i]=temp
    temp=array[i+1]
    array[i+1]=array[r]
    array[r]=temp
    return i+1
        
def exchange(array,index1,index2):
    dex1=array[index1]
    array[index1]=array[index2]
    array[index2]=dex1

def quickSortM3(array, p=0):
    r=len(array)-1
    if p<r:
        n=r-p+1
        m=median3(array,p,p+n//2,r)
        temp=array[m]
        array[m]=array[r]
        array[r]=temp
        q=partition(array,p,r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)
             
def median3(array,i,j,k):
    temp=[array[i],array[j],array[k]]
    m=0
    for n in temp:
        if n==median(temp):
            return m
        m+=1