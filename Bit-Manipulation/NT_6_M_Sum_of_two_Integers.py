class Solution:
    def getSum(self, a: int, b: int) -> int:
        while (b!=0):
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp
        return a

def main():
    a = 4
    b = 7
    res = Solution()
    print(res.getSum(a, b))

if __name__ == "__main__":
    main()