class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = Counter(s1)
        window_map = Counter()

        k = len(s1)

        for i in range(len(s2)):
            # add current character to window
            window_map[s2[i]] += 1

            # remove left character if window size > k
            if i >= k:
                if window_map[s2[i - k]] == 1:
                    del window_map[s2[i - k]]
                else:
                    window_map[s2[i - k]] -= 1

            # compare maps
            if window_map == s1_map:
                return True
        
        return False