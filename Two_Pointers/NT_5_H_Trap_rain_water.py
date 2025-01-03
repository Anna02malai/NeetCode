class Solution:
    def trap(self, height: list[int]) -> int:
        
        if not height: return 0

        l, r = 0, len(height) -1
        max_l, max_r = height[l], height[r]
        trap = 0

        while l < r:                
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                trap += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                trap += max_r - height[r]
                        
        return trap

def main():
    height = [0,2,0,3,1,0,1,3,2,1]
    res = Solution()
    print(res.trap(height))

if __name__ == "__main__":
    main()