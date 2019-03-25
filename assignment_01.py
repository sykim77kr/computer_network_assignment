import sys

arr = sys.argv[4:]
arr = list(map(int, arr))

def quick_sort(left, right):
    i = left
    j = right-1
    pivot = arr[right]
    if left >= right:
        return
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1
    arr[right] = arr[i]
    arr[i] = pivot
    quick_sort(left, i-1)
    quick_sort(i+1, right)

if sys.argv[1] != '-o':
    print('Unknown option:', sys.argv[1])
else:
    if sys.argv[2] in ('A', 'D'):
        if sys.argv[3] == '-i':
            quick_sort(0, len(arr)-1)
            if sys.argv[2] == 'D':
                arr.reverse()
            print(arr)
        else:
            print('Unknown option:', sys.argv[3])
    else:
        print('Unknown option:', sys.argv[2])
