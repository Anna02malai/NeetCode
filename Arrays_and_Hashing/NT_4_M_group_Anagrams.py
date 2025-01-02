from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            hmap[tuple(count)].append(s)
    
        return hmap.values()

def main():
    strs = ["act","pots","tops","cat","stop","hat"]
    res = Solution()
    print(res.groupAnagrams(strs))

if __name__ == "__main__":
    main()

