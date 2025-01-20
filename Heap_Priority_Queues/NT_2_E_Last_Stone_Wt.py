import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        self.stoneHeap = [int(-x) for x in stones]
        heapq.heapify(self.stoneHeap)

        while len(self.stoneHeap)>1:
            x = heapq.heappop(self.stoneHeap)
            y = heapq.heappop(self.stoneHeap)
            if y > x:
                heapq.heappush(self.stoneHeap, x - y)      
        
        if self.stoneHeap:
            return -1 * self.stoneHeap[0]
        else:
            return 0

def main():
    stones = [2,3,6,2,4]
    res = Solution()
    print(res.lastStoneWeight(stones))

if __name__ == "__main__":
    main()