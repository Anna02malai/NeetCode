class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {} #key (i, buying), value max Profit

        def dfs(i , buying):
            #base cases:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)


def main():
    prices = [1,3,4,0,4]
    res = Solution()
    print(res.maxProfit(prices))

if __name__ == "__main__":
    main()