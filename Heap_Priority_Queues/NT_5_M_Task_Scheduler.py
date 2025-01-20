from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cnt = Counter(tasks)
        maxHeap = [-c for c in cnt.values()]
        heapq.heapify(maxHeap)

        t = 0
        q = deque()

        while maxHeap or q:

            t += 1

            if not maxHeap:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])                
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t

def main():
    tasks = ["X","X","Y","Y"]
    n = 2
    res = Solution()
    print(res.leastInterval(tasks, n))

if __name__ == "__main__":
    main()