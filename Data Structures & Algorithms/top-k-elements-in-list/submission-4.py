class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for num in nums:
            mapping[num] = mapping.get(num,0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num,freq in mapping.items():
            bucket[freq].append(num)

        result = []
        for feq in range(len(bucket) -1, 0, -1):
            for nu in bucket[feq]:
                result.append(nu)
                if len(result) == k:
                    return result
        



        