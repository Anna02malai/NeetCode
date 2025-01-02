class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numSet = set(nums)
        long_seq = 0

        for n in numSet:
            if n-1 not in numSet:
                l = 1
                while(n + l) in numSet:
                    l +=1
                
                long_seq = max(long_seq, l)
        
        return long_seq

def main():
    nums = [0, 1, 4, 5, 3, 2, 6]
    res = Solution()
    print(res.longestConsecutive(nums))

if __name__ == "__main__":
    main()