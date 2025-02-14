"""
Definition of Interval:
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)

        for i in range(len(intervals)):
            l, r = i, i+1
            if i + 1 < len(intervals):
                ini_node, fin_node = intervals[l], intervals[r]
                if ini_node.end > fin_node.start:
                    return False
            
        return True

def main():
    intervals = [(0,30),(5,10),(15,20)]
    res = Solution()
    print(res.canAttendMeetings(intervals))

if __name__ == "__main__":
    main()