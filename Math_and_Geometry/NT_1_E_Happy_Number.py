class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sum_of_squares(n)

            if n == 1:
                return True
        return False

    
    def sum_of_squares(self, num):
        output = 0 
        while num:
            digit = num %10
            digit = digit ** 2
            output += digit
            num = num //10
        return output

def main():
    n = 19
    res = Solution()
    print(res.isHappy(n))

if __name__ == "__main__":
    main()