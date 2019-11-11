count = 0
debug = False

def partition(L, start, end):
	mid = start + (end - start)//2
	left = start
	right = end
	pivot = L[mid]
	print("pivot=",pivot)
	while left < right:
		while L[left] < pivot:
			left += 1
		while L[right] > pivot:
			right -= 1
		if left < right:
			temp = L[left]
			L[left] = L[right]
			L[right] = temp
			left += 1
			right -= 1
	return right

def quicksort(numbers, i, k):
	if (debug):print(">>> quicksort: ",numbers,"i=",i,"k=",k)
	if i >= k: return
	j = partition(numbers, i, k)
	if (debug):print("partition returned, j=",j)
	quicksort(numbers, i, j)
	quicksort(numbers, j+1, k)

mylist = [60, 30, 50, 40, 10, 20, 90, 40]

import random
mylist = [random.randint(1,100) for x in range(25)]
#mylist = list(set(mylist))

mylist = [90, 50, 40, 50, 20, 70, 20, 90, 50]
#mylist = [90, 50, 20, 70, 40, 60, 10, 88]

print(mylist)
'''
j = partition(mylist, 0, len(mylist)-1)
print ("partition returned j=",j)
print(mylist)
'''

quicksort(mylist, 0, len(mylist)-1)

print(mylist)