arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# arr1 = [  2, 3,5, 6, 7, 8, 9, 10,1]
def findpivot(arr,left,right):
	if right<left:
		return -1
	if right==left:
		return left
	mid = int((left+right)/2)
	if mid<right and arr[mid]>arr[mid+1]:
		return mid
	if left<mid and arr[mid]<arr[mid-1]:
		return mid-1
	if arr[mid]<=arr[left]:
		return findpivot(arr,left,mid-1)
	return findpivot(arr,mid+1,right)
def binarysearch(arr,left,right,key):
	if left>right:
		return -1
	mid = int((left+right)/2)
	if key==arr[mid]:
		return mid
	if key>arr[mid]:
		return binarysearch(arr,mid+1,right,key)
	return binarysearch(arr,left,mid-1,key)

def pivotsearch(arr,key):
	pivot=findpivot(arr,0,len(arr)-1)
	if pivot==-1:
		return binarysearch(arr,0,len(arr)-1,key)
	if arr[pivot] == key:
		return pivot
	if arr[0]<=key:
		return binarysearch(arr,0,pivot,key)
	return binarysearch(arr,pivot+1,len(arr)-1,key)
	print(pivot)
print(pivotsearch(arr1,5))