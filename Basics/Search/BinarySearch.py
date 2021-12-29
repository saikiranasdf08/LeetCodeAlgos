'''
Binary Search
Can also use bisect.bisect_left(a, x, lo=0, hi=len(a))
'''

def binarysearch_recursive(arr, l, h, ele):
     if h < l:
         return -1
     mid = (h+l) // 2
     if arr[mid] == ele:
         return mid
     elif arr[mid] > ele:
         return binarysearch_recursive(arr, l,mid-1,ele)
     else:
         return binarysearch_recursive(arr, mid+1,h,ele)


a=[2, 4 ,7 ,9, 11 ,34 , 56]

print(binarysearch_recursive(a,0,len(a),34))


def binarySearch_Iterative(arr,ele):
    h=len(arr)-1
    l=0
    mid=0
    while l<=h:
         mid= (l+h) // 2
         if arr[mid]== ele:
             return mid
         elif arr[mid]> ele:
             h=mid-1
         else:
             l=mid+1
    return -1

a=[2, 4 ,7 ,9, 11 ,34 , 56]

print(binarySearch_Iterative(a,11))
