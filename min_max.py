def find_min_max(list):
    mn = list[0]
    mx = list[0]
    for el in list:
        if el < mn:
            mn = el
        if el > mx:
            mx = el
    return mn, mx
