def linear_search(l, x):
    """
    Where, l  -> is list of elements to be searched for finding element
    x -> is the element to be searched
    If element is not found then text "No element is found" will be returned
    """

    for i in range(len(l)):
        if i == x:
            return "Element found in index " + str(i)
    return "Element not found"


l = [1, 2, 3, 4]
x = 567

res = linear_search(l, x)
print(res)