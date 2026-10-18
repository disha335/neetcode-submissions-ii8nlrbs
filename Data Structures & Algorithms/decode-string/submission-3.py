class Solution:
    def decodeString(self, s: str) -> str:
        stck=[]
        for ch in s:
            if ch!=']':
                stck.append(ch)
            else:
                currStr=""
                while stck and stck[-1]!='[':
                    currStr=stck.pop()+currStr
                stck.pop() # pop ]
                k=""
                while stck and stck[-1].isdigit():
                    k=stck.pop()+k
                stck.append(int(k)*currStr)
        return "".join(stck)


