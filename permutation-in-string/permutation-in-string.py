class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_seen = [0] * 26
        s2_seen = [0] * 26

        for i in range(len(s1)):
            s1_seen[ord(s1[i]) - ord('a')] += 1
            s2_seen[ord(s2[i]) - ord('a')] += 1

        l=0
        for r in range(len(s1), len(s2)):
            if s1_seen == s2_seen:
                return True

            s2_seen[ord(s2[r]) - ord('a')] += 1
            s2_seen[ord(s2[l]) - ord('a')] -= 1
            l += 1

    
        return s1_seen == s2_seen