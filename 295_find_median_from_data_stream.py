import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower_heap = [] # used as a max heap
        self.upper_heap = [] # used as a min heap

    # T = O(lg(n))
    # 
    def addNum(self, num: int) -> None:
        if len(self.lower_heap) == len(self.upper_heap):
            heapq.heappush(self.upper_heap, -heapq.heappushpop(self.lower_heap, -num))
        else:
            heapq.heappush(self.lower_heap, -heapq.heappushpop(self.upper_heap, num))

    def findMedian(self) -> float:
        if len(self.lower_heap) == len(self.upper_heap):
            return float(self.upper_heap[0] - self.lower_heap[0]) / 2.0
        
        # If odd, upper heap with have (n/2) + 1 numbers to lower heap's (n/2).
        # Thusly we know we can just min of upper half of numbers
        else:
            return float(self.upper_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()