class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        longest = 0
        d = {}

        while r<len(s):
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1

            w = r-l +1
            maxfreq = max(d.values())
            if w - maxfreq <= k:
                longest = max(longest, w)
            else:
                d[s[l]] -= 1
                l += 1
            r+= 1
        return longest

def main():
    s = "AAABABB"
    k = 1
    res = Solution()
    print(res.characterReplacement(s, k))

if __name__ == "__main__":
    main()