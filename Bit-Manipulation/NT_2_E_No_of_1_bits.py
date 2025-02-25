class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res

        # res = 0
        # while n:
        #     if n %2: 
        #         res += 1
        #     n = n >> 1
        # return res

def main():
    n = 23
    res = Solution()
    print(res.hammingWeight(n))

if __name__ == "__main__":
    main()