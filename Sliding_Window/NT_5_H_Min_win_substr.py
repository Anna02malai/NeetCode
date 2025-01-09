class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        countT, wdw = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            wdw[c] = 1 + wdw.get(c, 0)

            if c in countT and countT[c] == wdw[c]:
                have += 1
            
            while have == need:
                if (r -l + 1) < resLen:
                    res = [l, r]
                    resLen = r -l + 1

                wdw[s[l]] -= 1
                if s[l] in countT and wdw[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""

def main():
    s = "OUZODYXAZV"
    t = "XYZ"
    res = Solution()
    print(res.minWindow(s, t))

if __name__ == "__main__":
    main()
