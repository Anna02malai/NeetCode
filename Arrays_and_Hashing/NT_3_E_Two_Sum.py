class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        index = {}

        for i,n in enumerate(nums):
            index[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in index and index[diff] != i:
                return [i, index[diff]]


def main():
    nums = [3, 4, 5, 6, 7]
    target = 7
    res = Solution()
    print(res.twoSum(nums, target))

if __name__ == "__main__":
    main()