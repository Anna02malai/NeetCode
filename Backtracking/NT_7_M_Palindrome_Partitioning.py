class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res, part = [], []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

def main():
    s = "aab"
    res = Solution()
    print(res.partition(s))

if __name__ == "__main__":
    main()