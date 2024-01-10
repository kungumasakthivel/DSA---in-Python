def linear_search(l, x, idx):
    """
    Where, l -> is list of elements to be searched
           x -> is element to be searched
           idx -> is total number of element
    """
    idx = idx - 1

    if idx == -1:
        return "Element not found"
    elif x == l[idx]:
        return "Element fouund at index " + str(idx)
    else:
        return linear_search(l, x, idx)

l = [1, 2, 3, 11, 4, 9]
x = 1
idx = len(l)

print(linear_search(l, x, idx))
    