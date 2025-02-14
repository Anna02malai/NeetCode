class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1: ]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res

def main():
    intervals = [[1,3],[1,5],[6,7]]
    res = Solution()
    print(res.merge(intervals))

if __name__ == "__main__":
    main()