class Solution:
    def encode(self, strs: List[str]) -> str:
        #loop through the list and start encode
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s
        return code

    def decode(self, s: str) -> List[str]:
        result = []
        i= 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #s[i:j] length
            length = int(s[i:j])
            # the lenght is the content right after '#'
            start = j + 1
            word = s[start: start + length]
            result.append(word)
            i = start + length
        return result
        

