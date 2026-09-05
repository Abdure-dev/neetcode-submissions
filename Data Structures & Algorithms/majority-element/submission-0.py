class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        input: list[int]
        output: int
        majority element always exists.
        the majority eleemnt is the element that appears more than n/2
        """
        n = len(nums)
        maj_size = n/2
        maj_element = nums[0]
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] +=1
        for key,val in mapping.items():
            if val > maj_size:
                maj_element = key
        return maj_element
        