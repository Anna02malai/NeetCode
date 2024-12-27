class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        
        a = set(nums)
        
        if len(nums) == len(a):
            return False
        else: 
            return True

def main():
    nums = [1, 2, 3, 3, 4, 5]
    res = Solution()
    print(res.hasDuplicate(nums))

if __name__ == "__main__":
    main()