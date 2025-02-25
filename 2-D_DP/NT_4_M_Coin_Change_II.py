class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(len(coins)-1, -1, -1):
            nextDp = [0]* (amount+1)
            nextDp[0] = 1

            for a in range(1, amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a - coins[i]]
            dp = nextDp
        
        return dp[amount]

def main():
    amount = 4
    coins = [1,2,3]
    res = Solution()
    print(res.change(amount, coins))

if __name__ == "__main__":
    main()