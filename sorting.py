def swap(mylist, index1, index2):
    temp = mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp

def pivot(mylist, pivot_index, end_index):

    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index +=1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(mylist, left, right):

    if left < right:
        pivot_index = pivot(mylist, left, right)
        quick_sort_helper(mylist, left, pivot_index -1)
        quick_sort_helper(mylist, pivot_index+1, right)

    return mylist

def quick_sort(mylist):
    return quick_sort_helper(mylist, 0, len(mylist) - 1)


print(quick_sort([7,1,2,5,3]))

