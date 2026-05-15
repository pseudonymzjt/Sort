def threeSum(nums: list[int], target: int = 0) -> list[list[int]]:
    """
    题目要求：
    给定一个整数数组 nums 和一个整数 target，
    找出数组中所有满足 a + b + c == target 且不重复的三元组 [a, b, c]。
    答案中不可以包含重复的三元组。

    实现思路：
    1. 排序：先将数组排序，便于后续双指针查找以及去重。
    2. 固定一个数，双指针找另外两个数。
    3. 去重。
    4. 若 nums[i] 与后面最小的两个数之和已大于 target，直接结束循环，否则，跳过当前 i。
    时间复杂度：O(n^2)，其中 n 为数组长度。排序 O(n log n)，双指针 O(n^2)。
    空间复杂度：O(1)（不计结果存储所用的空间）。
    """
    nums.sort()
    L = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] + nums[i + 1] + nums[i + 2] > target:
            break

        if nums[i] + nums[n - 2] + nums[n - 1] < target:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                L.append([nums[i], nums[left], nums[right]])

                # 跳过重复
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return L


if __name__ == "__main__":
    print(threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]))
    # 测试 target 不为 0 的情况
    print(threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10], target=5))