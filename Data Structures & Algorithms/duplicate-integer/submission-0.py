class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            num_set.add(n)
        return len(num_set) != len(nums)
                
        