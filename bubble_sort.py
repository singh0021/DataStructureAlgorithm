def bubble_sort(mylist):

    for i in range(len(mylist) -1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
    return mylist

print(bubble_sort([4,2,1,3,5]))

def selection_sort(mylist):
    for i in range(len(mylist)-1):
        min_index = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j
            if i != min_index:
                temp = mylist[i]
                mylist[i] = mylist[min_index]
                mylist[min_index] = temp
    return mylist

print(selection_sort([4,2,1,6,0]))


def insertion_sort(mylist):

    for i in range(1, len(mylist)):
        temp = mylist[i]
        j = i -1
        while temp < mylist[j] and j > -1:
            mylist[j+1] = mylist[j]
            mylist[j] = temp
            j -=1

    return mylist

print(insertion_sort([4,2,1,6,0]))

# only for sorted lists
def merge_helper(mylist1, mylist2):
    combined = []
    i =0
    j = 0
    while i < len(mylist1) and j < len(mylist2):
        if mylist1[i] < mylist2[j]:
            combined.append(mylist1[i])
            i +=1
        else:
            combined.append(mylist2[j])
            j +=1
    while i < len(mylist1):
        combined.append(mylist1[i])
        i +=1

    while j < len(mylist2):
        combined.append(mylist2[j])
        j +=1

    return combined


print(merge_helper([4,6,23], [1, 12, 90]))


def merge_sort(mylist):

    if len(mylist) == 1:
        return mylist
    mid = int(len(mylist)/2)
    left =  mylist[:mid]
    right = mylist[mid:]
    return merge_helper(merge_sort(left), merge_sort(right))


print(merge_sort([6,1,3,2,10]))

def swap(mylist, index1, index2):
    temp = mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp

def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

#mylist = [5,1,3,7,8,9]
#print(pivot(mylist, 0, 5))
#print(mylist)

def quick_sort_helper(mylist, left , right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quick_sort_helper(mylist, left, pivot_index-1)
        quick_sort_helper(mylist, pivot_index+1, right)

    return mylist

def quick_sort(mylist):
    return quick_sort_helper(mylist, 0, len(mylist)-1)

print(quick_sort([4,7,5,2,3,1]))