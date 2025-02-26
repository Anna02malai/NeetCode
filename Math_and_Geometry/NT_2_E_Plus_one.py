class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i <len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    one = 1
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]
    
def main():
    digits = [9, 9, 9]
    res = Solution()
    print(res.plusOne(digits))

if __name__ == "__main__":
    main()
        