class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []

        for num in range(n+1):
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            res.append(count)
        return res

def main():
    n = 4
    res = Solution()
    print(res.countBits(n))

if __name__ == "__main__":
    main()