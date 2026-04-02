"""
    给一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。
    找出满足下述条件的下标对 (i, j)：
    i != j,
    abs(i - j) <= indexDiff
    abs(nums[i] - nums[j]) <= valueDiff
    如果存在，返回 true ；否则，返回 false 。

    Example:
        输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
        输出：true
        解释：可以找出 (i, j) = (0, 3) 。
        满足下述 3 个条件：
        i != j --> 0 != 3
        abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
        abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
"""

"""
    考虑使用桶排序，将不同数值范围的元素分到不同的桶中。
    每个桶的大小为 valueDiff + 1，确保在桶桶之间的元素差值不超过 valueDiff。
    遍历数组，将每个元素分到对应的桶，同时动态的维护桶，使得索引差值不超过 indexDiff。
    若满足条件，那么当前元素和桶中元素要么在一个桶中，要么在相邻桶中，前者直接返回，后者需要检查差值是否不超过 valueDiff。
"""

"""
    或者使用更直观的滑动窗口法，我们动态的维护一个大小为 indexDiff 的有序滑动窗口。
    我们遍历数组并直接在窗口中查找满足要求的元素。这里使用了窗口的方法用以查找大于等于 nums[i] - valueDiff 的最小元素，
    并检查其是否小于等于 nums[i] + valueDiff。注意，由于SortedList的bisect_left的方法特性，在窗口中不存在大于等于 nums[i] - valueDiff 的元素时，
    bisect_left会返回窗口的长度，所以需要检查返回的索引是否超出窗口范围
"""
def containsNearbyAlmostDuplicate(option: str, nums: list, indexDiff: int, valueDiff: int):
    if option == "bucket_sort":
        if indexDiff <= 0 or valueDiff < 0:
            return False
        bucket_size = valueDiff + 1
        buckets = {}

        for i in range(len(nums)):
            bucket_id = nums[i] // bucket_size
            if bucket_id in buckets:
                return True
            for neighbor_bucket in [bucket_id - 1, bucket_id + 1]:
                if neighbor_bucket in buckets and abs(buckets[neighbor_bucket] - nums[i]) <= valueDiff:
                    return True
            buckets[bucket_id] = nums[i]
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]
        return False
    if option == "sliding_window":
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        from sortedcontainers import SortedList
        window = SortedList()
        for i in range(len(nums)):
            left_val = nums[i] - valueDiff
            pos = window.bisect_left(left_val)
            if pos < len(window) and window[pos] <= nums[i] + valueDiff:
                return True
            window.add(nums[i])
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])
        return False


print(containsNearbyAlmostDuplicate("sliding_window", [1,2,3,1], 3, 0))
print(containsNearbyAlmostDuplicate("sliding_window", [1,5,9,1,5,9], 2, 3))
print(containsNearbyAlmostDuplicate("sliding_window", [1,2,2,3,4,5], 3, 0))