class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] +=1
        sorted_by_value = dict(sorted(mapping.items(), key=lambda item: item[1], reverse=True))
        list_print = []
        i = 1
        for key,value in sorted_by_value.items():
            if i >k:
                break
            list_print.append(key)
            i += 1
        return list_print



        