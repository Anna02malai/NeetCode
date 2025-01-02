class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        d = {}
        freq = [[] for i in range(len(nums) +1)]

        for i in nums:
            d[i] = 1 + d.get(i, 0)
        
        for num, count in d.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq)-1,0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res        
        

def main():
    nums = [1,2,2,3,3,3]
    k = 2
    res = Solution()
    print(res.topKFrequent(nums, k))

if __name__ == "__main__":
    main()