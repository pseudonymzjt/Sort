def wiggleSortSimple(nums: list):
    for i in range(1, len(nums)):
        if i % 2 == 0:
            if nums[i - 1] <= nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        else:
            if nums[i - 1] >= nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
    return nums

print("wiggleSort I:" + str(wiggleSortSimple([1,5,1,1,6,4])))

"""
    给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
    你可以假设所有输入数组都可以得到满足题目要求的结果。
"""
"""
    首先使用三路分区找到中位数，然后使用索引映射将较大的元素放在奇数位置，较小的元素放在偶数位置
"""
def wiggleSort(nums: list):
    n = len(nums)

    def get_median(k):
        left, right = 0, n - 1
        while left <= right:
            import random
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            if store_idx == k:
                return nums[store_idx]
            elif store_idx < k:
                left = store_idx + 1
            else:
                right = store_idx - 1

    mid = get_median(n // 2)

    def A(i):
        return (1 + 2 * i) % (n | 1)

    i, j, k = 0, 0, n - 1
    while j <= k:
        idx_j = A(j)
        if nums[idx_j] > mid:
            idx_i = A(i)
            nums[idx_i], nums[idx_j] = nums[idx_j], nums[idx_i]
            i += 1
            j += 1
        elif nums[idx_j] < mid:
            idx_k = A(k)
            nums[idx_k], nums[idx_j] = nums[idx_j], nums[idx_k]
            k -= 1
        else:
            j += 1
    return nums

data = [1, 5, 1, 1, 6, 4]
print("wiggleSort II:" + str(wiggleSort(data)))