class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        l = 0
        r = len(nums) -1

        while l <= r :
            mid = l + ((r-l)//2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

def main():
    nums = [-1,0,2,4,6,8]
    target = 4
    res = Solution()
    print(res.search(nums, target))

if __name__ == "__main__":
    main()