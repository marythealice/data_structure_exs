def minimum_element(list):
    minimum = list[0]

    for i in range(1,len(list)):
        if list[i] < minimum:
            minimum = list[i]
    return minimum
