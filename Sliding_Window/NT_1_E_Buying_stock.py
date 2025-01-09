class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        for l in range(n):
            r = l+1
            while r <n:
                if prices[r] < prices[l]:
                    l = r
                else:
                    max_profit = max(max_profit, (prices[r]-prices[l]))
                    r += 1
        
        return max_profit

def main():
    prices = [10,1,5,6,7,1]
    res = Solution()
    print(res.maxProfit(prices))

if __name__ == "__main__":
    main()
