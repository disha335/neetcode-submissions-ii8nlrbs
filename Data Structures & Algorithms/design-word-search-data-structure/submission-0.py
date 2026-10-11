class TrieNode:
    def __init__(self):
        self.links = {}
        self.flag=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.links:
                node.links[ch]=TrieNode()
            node=node.links[ch]
        node.flag=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            node=root
            for i in range(j,len(word)):
                ch=word[i]
                if ch=='.':
                    for link in node.links.values():
                        if dfs(i+1,link)==True:
                            return True
                    return False
                else:
                    if ch not in node.links:
                        return False
                    node=node.links[ch]
            return node.flag    
        return dfs(0,self.root)
