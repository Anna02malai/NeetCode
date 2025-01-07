class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stk = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                stkT,stkIdx = stk.pop()
                res[stkIdx] = (i -stkIdx)
            stk.append([temp, i])
        
        return res

def main():
    temp = [30,38,30,36,35,40,28]
    res = Solution()
    print(res.dailyTemperatures(temp))

if __name__ == "__main__":
    main()