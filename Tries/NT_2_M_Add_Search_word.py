class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:

        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                return curr.endOfWord
            
            return dfs(0, self.root)
    
def main():
    inp = ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
    res = WordDictionary()
    print(WordDictionary.addWord(inp))

if __name__ == "__main__":
    main()