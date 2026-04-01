import copy

def permuteUnique(nums: List[int]) -> List[List[int]]:
    L = []
    if len(nums) <= 1:
        L.append(nums.copy())  # 使用 copy() 避免引用问题
        return L
    
    # 递归生成剩余数字的全排列
    L1 = permuteUnique(nums[1:])
    
    for l in L1:
        # 尝试在每个位置插入当前数字（包括末尾）
        for i in range(len(l) + 1):  # 注意这里是 len(l) + 1
            temp = copy.copy(l)
            temp.insert(i, nums[0])
            if temp not in L:
                L.append(temp)
    
    return L