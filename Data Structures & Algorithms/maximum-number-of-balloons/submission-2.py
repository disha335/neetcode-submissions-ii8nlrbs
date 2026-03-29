class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cntBallon = Counter("balloon")
        cntText = Counter(text)
        res = len(text)

        for ch in cntBallon:
            res = min(res, cntText[ch]//cntBallon[ch])

        return res