"""
    给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
    注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

    示例：
        输入：nums = [10,2]
        输出："210"
    
    本题只是应用了一个简单的冒泡排序算法。在这道题中，更高级的排序算法没有明显的性能优势。
    注意，排序的依据是两个字符串的拼接结果。
    若结果不合法（以 0 开头），需要去掉 0。
"""
def largestNumber(nums: list):
    strings = [str(num) for num in nums]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i] + strings[j] < strings[j] + strings[i]:
                strings[i], strings[j] = strings[j], strings[i]
    string = ""
    for i in range(len(strings)):
        string += strings[i]
    return "0" if string.startswith("0") else string
print(largestNumber([10, 2]))