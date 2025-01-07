class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []
        for idx, hgt in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > hgt:
                i, h = stack.pop()
                maxArea = max(maxArea, h *(idx - i))
                start = i
            stack.append((start, hgt))
        
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea

def main():
    heights = [7,1,7,2,2,4]
    res = Solution()
    print(res.largestRectangleArea(heights))

if __name__ == "__main__":
    main()