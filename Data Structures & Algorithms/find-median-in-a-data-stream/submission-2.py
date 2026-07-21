class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)

        # if max of small > min of large: move to large
        if (self.small and self.large and (self.large[0] < -1 * self.small[0])):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

        # if n of small > n of large + 1: move max to large
        if len(self.small) > (len(self.large) + 1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # if n of large > n of small + 1: move min to small
        if len(self.large) > (len(self.small) + 1):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            heap_sum = float((-1 * self.small[0]) + self.large[0])
            return heap_sum / 2
        