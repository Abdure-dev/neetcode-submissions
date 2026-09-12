class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)          # O(1) lookups, and removes duplicates
        longest = 0

        for x in num_set:
            if (x - 1) not in num_set:          # x is the START of a run
                length = 1
                current = x
                while (current + 1) in num_set: # walk the run rightward
                    current += 1
                    length += 1
                longest = max(longest, length)  # keep the best run seen

        return longest