def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[14,23,2,67, 87, 900, 5, 65, 1, 2, 3, 4, 27]
bubbleSort(arr)
print(arr)