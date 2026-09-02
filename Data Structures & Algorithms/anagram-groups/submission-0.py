class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in dicts:
                dicts[key] = []
            dicts[key].append(s)
        empty_list = []
        for num in dicts.values():
            empty_list.append(num)
        return empty_list
