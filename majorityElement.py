"""
    给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
    示例：
        输入：nums = [3,2,3]
        输出：[3]
"""
"""
    最初想法是排序后，出现超过 ⌊ n/3 ⌋ 次的元素，一定在排序后的数组中出现超过 ⌊ n/3 ⌋ 次的次数
    但是排序的时间复杂度是 O(nlogn)，空间复杂度是 O(1)，不符合要求。
    出现超过 ⌊ n/3 ⌋ 次的元素至多有 2 个，考虑采用摩尔投票法。下面说明这一算法的原理。
    我们选定最开始的两个元素为出现次数超过 ⌊ n/3 ⌋ 次的元素。
    指针每向前移动一次，若遇到两个元素中的一个，做一次自增操作，否则和现有元素次数抵消一次。
    若当前元素次数为 0，则将当前元素作为新的候选元素。遍历完数组后核验候选元素是否出现超过 ⌊ n/3 ⌋ 次。
    该算法可行的原因是，出现次数超过 ⌊ n/3 ⌋ 次的元素至多有 2 个。而每遍历三个元素，若都不相同，次数减 1 ，相当于进行了一次抵消操作，
    所以留下的元素中一定包含次数超过 ⌊ n/3 ⌋ 次的元素。
"""
def majorityElement(nums):
    if len(nums) <= 5:
        return nums
    cand1, cand2 = None, None
    cnt1, cnt2 = 0, 0
    for num in nums:
        if num == cand1:
            cnt1 += 1
        elif num == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1, cnt1 = num, 1
        elif cnt2 == 0:
            cand2, cnt2 = num, 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    result = []
    n = len(nums)
    for cand in [cand1, cand2]:
        if cand is not None and nums.count(cand) > n // 3:
            if cand not in result: 
                result.append(cand)           
    return result
print(majorityElement([1,2,3,1,5,6,7,1,9,1]))