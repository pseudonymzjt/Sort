from collections import Counter

def findPairs(nums: list, k: int):
    if k < 0:
        return 0
    counts = Counter(nums)
    if k == 0:
        return sum(1 for count in counts.values() if count > 1)
    else:
        res = 0
        for num in counts:
            if num + k in counts:
                res += 1
        return res

print(findPairs([3, 1, 4, 1, 5], 2))