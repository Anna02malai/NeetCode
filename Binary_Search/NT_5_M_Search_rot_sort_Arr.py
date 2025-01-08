class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -  1
            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
        
        return -1
    
def main():
    nums = [3,4,5,6,1,2]
    target = 1
    res = Solution()
    print(res.search(nums, target))

if __name__ == "__main__":
    main()