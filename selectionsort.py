def selectionSort(array):
    for i in range(len(array)):
        min=i
        for j in range(i, len(array)):
            if array[j]<array[min]:
                min=j
        if i!=min:
            temp=array[i]
            array[i]=array[min]
            array[min]=temp
                