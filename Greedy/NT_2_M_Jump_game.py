class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

def main():
    nums = [1,2,0,1,0]
    res = Solution()
    print(res.canJump(nums))

if __name__ == "__main__":
    main()