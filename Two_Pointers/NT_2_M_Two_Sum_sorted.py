class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        res = []
        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]    
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        
def main():
    nums = [1, 2, 3, 4]
    sum = 3
    res = Solution()
    print(res.twoSum(nums, sum))

if __name__ == "__main__":
    main()