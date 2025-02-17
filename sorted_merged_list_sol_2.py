def merge_sorted_lists(l1,l2):
    p1 = 0
    p2 = 0

    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] > l2[p2]:
            l1.insert(p1, l2[p2])
            p1 += 1
            p2 += 1
        else:
            p1 += 1
    if p2 < len(l2):
        l1.extend(l2[p2:])
    
    return l1
