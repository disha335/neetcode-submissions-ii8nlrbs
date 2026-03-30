class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # build s1 frequency map
        s1_map = Counter(s1)
        # for ch in s1:
        #     s1_map[ch] = s1_map.get(ch, 0) + 1
        
        window_map = {}
        k = len(s1)

        for i in range(len(s2)):
            # add current char
            window_map[s2[i]] = window_map.get(s2[i], 0) + 1

            # remove left char if window size exceeds k
            if i >= k:
                left_char = s2[i - k]
                if window_map[left_char] == 1:
                    del window_map[left_char]
                else:
                    window_map[left_char] -= 1

            # ✅ compare maps
            if window_map == s1_map:
                return True
        
        return False