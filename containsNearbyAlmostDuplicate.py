def containsNearbyAlmostDuplicate(nums: list, indexDiff: int, valueDiff: int):
    if indexDiff <= 0 or valueDiff < 0:
        return False
    
    # 使用桶，每个桶的大小为valueDiff+1
    bucket_size = valueDiff + 1
    buckets = {}
    
    for i in range(len(nums)):
        # 计算当前数字应该放入哪个桶
        bucket_id = nums[i] // bucket_size
        
        # 如果同一个桶中有元素，则它们的差值不超过valueDiff
        if bucket_id in buckets:
            return True
        
        # 检查相邻桶是否有符合条件的元素
        for neighbor_bucket in [bucket_id - 1, bucket_id + 1]:
            if neighbor_bucket in buckets and abs(buckets[neighbor_bucket] - nums[i]) <= valueDiff:
                return True
        
        # 将当前元素加入桶中
        buckets[bucket_id] = nums[i]
        
        # 维护窗口大小，移除超出indexDiff范围的元素
        if i >= indexDiff:
            old_bucket_id = nums[i - indexDiff] // bucket_size
            del buckets[old_bucket_id]
    
    return False

print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
print(containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
print(containsNearbyAlmostDuplicate([1,2,2,3,4,5], 3, 0))