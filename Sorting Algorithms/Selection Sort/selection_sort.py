def selection_sort(l):

    for i in range(len(l)):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j

        l[i], l[min_idx] = l[min_idx], l[i]


l = [9, 8, 7, 6, 2, 1, 0]
selection_sort(l)
print(l)
