def merge_sorted_lists(l1,l2):
    result = [None] * (len(l1) + len(l2))
    p1 = 0
    p2 = 0
    p3 = 0

    while (p1 < len(l1)) and (p2 < len(l2)):
        if (l1[p1] < l2[p2]):
            result[p3] = l1[p1]
            p1 += 1
            p3 += 1
        else:
            result[p3] = l2[p2]
            p2 += 1
            p3 += 1
    # if one of the lists still remains:
    while (p1 < len(l1)):
        result[p3] = l1[p1]
        p1 += 1
        p3 += 1
    while (p2 < len(l2)):
        result[p3] = l2[p2]
        p2 += 1
        p3 += 1
    
    return result