class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res

def main():
    nums = [7,6,6,7,8]
    res = Solution()
    print(res.singleNumber(nums))

if __name__ == "__main__":
    main()