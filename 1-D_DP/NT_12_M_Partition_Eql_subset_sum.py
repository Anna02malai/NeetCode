class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for ele in dp:
                if (ele + nums[i] == target):
                    return True
                nextDP.add(ele + nums[i])
                nextDP.add(ele)
            dp = nextDP

        return False

def main():
    nums = [1,2,3,4]
    res = Solution()
    print(res.canPartition(nums))

if __name__ == "__main__":
    main()