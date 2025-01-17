class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for p, s in pair:
            stack.append((target - p)/s) 
            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack) 

def main():
    tgt = 10
    pos = [4,1,0,7]
    spd = [2,2,1,1]
    res = Solution()
    print(res.carFleet(tgt, pos, spd))

if __name__ == "__main__":
    main()
