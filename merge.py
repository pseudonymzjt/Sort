def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    for interval in intervals:
        if res and res[-1][1] >= interval[0]:
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)
    print(res)

merge([[1,3],[2,6],[8,10],[15,18]])
