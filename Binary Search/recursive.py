def binary_search(l, x, low, high):
    """
    Where,
          l -> list of element to be searched
          x -> element to be searched
    """

    if high >= low:

        mid = low + (high - low) // 2

        if l[mid] == x:
            return "Element found at index " + str(mid)
        elif l[mid] > x:
            return binary_search(l, x, low, mid - 1)
        else:
            return binary_search(l, x, mid + 1, high)
    else:
        return "Element not found"
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
res = binary_search(l, x, 0, len(l) - 1)
print(res)
