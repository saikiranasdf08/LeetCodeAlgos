'''
Linear Search
Searching element in a list or Array
'''

def search(arr, ele):
    for i in range(len(arr)):
        if ele == arr[i]:
            return i
    return -1


a=[20,21,22,23,24,25]
print(search(a,24))

