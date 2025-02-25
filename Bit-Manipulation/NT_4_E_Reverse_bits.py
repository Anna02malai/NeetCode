class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        
        return res

def main():
    n = 21
    res = Solution()
    print(res.reverseBits(n))

if __name__ == "__main__":
    main()