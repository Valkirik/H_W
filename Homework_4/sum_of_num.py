def range_sum(start: int, end: int) -> int:
    l = [start, end]
    for i in l:
        if start > end:
            start, end = end, start
    print(l)
    lst_range = list(range(start, end+1))
    return sum(lst_range)


print(range_sum(start=5, end=10))





