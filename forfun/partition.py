def partition(array, left, right, pivot_index):
    pivot_value = array[pivot_index]
    array[pivot_index], array[right] = array[right], array[pivot_index]
    index = left
    for i in range(left, right):
        if array[i] < pivot_value:
            array[i], array[index] = array[index], array[i]
            index = index + 1
    array[index], array[right] = array[right], array[index]
    return index

def quick_sort(array, left, right):
    if left >= right:
        return
    pivot_index = (left + right) / 2
    index = partition(array, left, right, pivot_index)
    quick_sort(array, left, index)
    quick_sort(array, index+1, right)

def nth_of_array(array, left, right, n):
    if left == right:
        return array[left]
    pivot_index = (left + right) / 2
    index = partition(array, left, right, pivot_index)
    if index == n:
        return array[n]
    elif index > n:
        return nth_of_array(array, left, index, n)
    else:
        return nth_of_array(array, index+1, right, n)

def nth_of_array_non_recur(array, left, right, n):
    if left == right:
        return array[left]
    while True:
        pivot_index = (left + right) / 2
        index = partition(array, left, right, n)
        if index == n:
            return array[index]
        elif index > n:
            right = index-1
        else:
            left = index + 1

if __name__ == '__main__':
    array = [6, 2, 5, 3, 1, 4]
    #quick_sort(array, 0, len(array)-1)
    #print nth_of_array(array, 0, len(array)-1, 1)
    print nth_of_array_non_recur(array, 0, len(array)-1, 1)
