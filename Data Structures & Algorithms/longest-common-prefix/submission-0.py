class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ##identify the smallest word
        ##the prefix is determind from the smallest word
        smallest = strs[0]
        for word in strs:
            if len(word) < len(smallest):
                smallest = word
        ##loop through the rest of the list and see if the word contian
        ##the prefix of the smallest word
        n = len(smallest)
        longest_prefix = ""
        for i in range(n):
            letter_at_i = strs[0][i]
            valid = True
            for s in strs:
                if s[i] != letter_at_i:
                    valid = False
                    break
            if not valid:
                break
            longest_prefix += strs[0][i]

        return longest_prefix

        