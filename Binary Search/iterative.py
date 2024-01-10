def binary_search(l, x):
    """
    Where,
          l -> list of element to be searched
          x -> element to be searched
    """

    low = 0
    high = len(l) - 1

    while low <= high:

        mid =  low + (high - low) // 2

        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            return "Element found at index " + str(mid)
    return "Element not found"


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = 14
res = binary_search(l, x)
print(res)