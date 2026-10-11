class TrieNode:
    def __init__(self):
        self.links=[None]*26
        self.flag=False

class PrefixTree:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            i=ord(ch)-ord('a')
            if node.links[i]==None:
                node.links[i]=TrieNode()
            node=node.links[i]
        node.flag=True

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            i=ord(ch)-ord('a')
            if node.links[i]==None:
                return False
            node=node.links[i]
        return node.flag

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            i=ord(ch)-ord('a')
            if node.links[i]==None:
                return False
            node=node.links[i]
        return True
        
        