class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        vol = 0
        l, r = 0, len(heights) -1

        while l < r:
            
            water = min(heights[l], heights[r]) * (r - l)
            vol = max(vol, water)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return vol

def main():
    height = [1,7,2,5,4,7,3,6]
    res = Solution()
    print(res.maxArea(height))

if __name__ == "__main__":
    main()