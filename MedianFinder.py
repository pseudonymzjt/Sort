"""
    中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
    例如 arr = [2,3,4] 的中位数是 3 。
    例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
    实现 MedianFinder 类:
    MedianFinder() 初始化 MedianFinder 对象。
    void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
    double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10^{-5} 以内的答案将被接受。

    示例：
        输入
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
            [[], [1], [2], [], [3], []]
        输出
            [null, null, null, 1.5, null, 2.0]

    使用双堆法保证插入和查找都是 O(log n) 时间复杂度。
    维护一个小顶堆 queMin 和一个大顶堆 queMax。两个堆的大小差至多为 1，确保中位数可以快速获取。
    细节上 queMax 大小可以比 queMin 大 1，此时可知总数是奇数， 中位数为 queMax 的堆顶元素。
    否则，queMin 与 queMax 大小相等，此时可知总数是偶数， 中位数为 (queMax 的堆顶元素 + queMin 的堆顶元素) / 2。
"""
import heapq

class MedianFinder(object):
    def __init__(self):
        # Python 默认是小顶堆，大顶堆需要存负数来模拟
        self.queMin = [] 
        self.queMax = [] 

    def addNum(self, num):
        if not self.queMax or num <= -self.queMax[0]:
            heapq.heappush(self.queMax, -num)
            if len(self.queMax) > len(self.queMin) + 1:
                heapq.heappush(self.queMin, -heapq.heappop(self.queMax))
        else:
            heapq.heappush(self.queMin, num)
            if len(self.queMin) > len(self.queMax):
                heapq.heappush(self.queMax, -heapq.heappop(self.queMin))

    def findMedian(self):
        if len(self.queMax) > len(self.queMin):
            return float(-self.queMax[0])
        return (-self.queMax[0] + self.queMin[0]) / 2.0