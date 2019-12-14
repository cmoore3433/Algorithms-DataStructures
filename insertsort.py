def insertSort(array=[]):
    for i in range(len(array)):
        key= array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

        