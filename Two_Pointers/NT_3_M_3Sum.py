class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if i >0 and a == nums[i - 1]:
                continue

            l , r = i+1, len(nums) - 1                

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([[nums[i]], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
                elif (nums[l] + nums[r]) < -nums[i]:
                    l += 1
                else:
                    r -= 1
        
        return res

def main():
    nums = [-1,0,1,2,-1,-4]
    res = Solution()
    print(res.threeSum(nums))

if __name__ == "__main__":
    main()