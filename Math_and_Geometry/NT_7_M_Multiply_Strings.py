class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        
        res, start = res[::-1], 0
        while start < len(res) and res[start] == 0:
            start += 1
        
        res = map(str, res[start:])
        return "".join(res)

def main():
    num1 = "111"
    num2 = "222"
    res = Solution()
    print(res.multiply(num1, num2))

if __name__ == "__main__":
    main()