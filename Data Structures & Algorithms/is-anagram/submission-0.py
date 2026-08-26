class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        for x in s:
            count[ord(x) - ord('a')] += 1
        for y in t:
            count[ord(y)-ord('a')] -= 1
        
        for i in count:
            if i != 0:
                return False
        return True
        