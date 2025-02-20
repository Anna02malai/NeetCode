class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s, d, p in flights: #source, destination and price
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]

def main():
    n = 4
    flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
    src = 0
    dst = 3
    k = 1
    res = Solution()
    print(res.findCheapestPrice(n, flights, src, dst, k))

if __name__ == "__main__":
    main()