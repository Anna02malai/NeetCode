class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amt in range(amount + 1):
            for c in coins:
                if amt- c >=0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        
        return dp[amt] if dp[amt] != amt+1 else -1

def main():
    coins = [1,5,10]
    amount = 12
    res = Solution()
    print(res.coinChange(coins, amount))

if __name__ == "__main__":
    main()