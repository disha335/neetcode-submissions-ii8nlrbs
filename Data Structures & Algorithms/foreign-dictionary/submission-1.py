class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = [[] for _ in range(26)]
        indegree = [0]*26
        present = set()
        ans=""
        q=deque()
        for i in range(len(words)-1):
            s1=words[i]
            s2=words[i+1]
            if len(s1)>len(s2) and s1.startswith(s2):
                return ""
            for ptr in range(min(len(s1),len(s2))):
                if s1[ptr]!=s2[ptr]:
                    u=ord(s1[ptr])-ord('a')
                    v=ord(s2[ptr])-ord('a')
                    adj[u].append(v)
                    break
            
        for word in words:
            for ch in word:
                present.add(ord(ch)-ord('a'))

        for i in range(26):
            for nei in adj[i]:
                indegree[nei]+=1
        for i in present:
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            ans+=chr(node+ord('a'))
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(present)!=len(ans):
            return ""
        return ans
