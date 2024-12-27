class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d1, d2 = {}, {}

        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1

        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
        
        return d1 == d2


def main():
    s = "racecar"
    t = "carrace"
    res = Solution()
    print(res.isAnagram(s,t))

if __name__ == "__main__":
    main()