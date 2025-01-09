class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        unq_set = set()
        for r in range(len(s)):
                while s[r] in unq_set:
                    unq_set.remove(s[l])
                    l += 1

                unq_set.add(s[r]) 
                longest = max(longest, (r-l + 1))
        return longest

def main():
    s = "pwwkew"
    res = Solution()
    print(res.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()