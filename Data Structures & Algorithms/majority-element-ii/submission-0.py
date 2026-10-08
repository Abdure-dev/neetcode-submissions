class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = {}
        #construct an array to hold each numbers and how many times they apperad
        for _,val in enumerate(nums):
            if val not in counter:
                counter[val] = 0
            counter[val] += 1
        #then itrate through the dictionary
        output = []
        for key,value in counter.items():
            if value > n/3:
                output.append(key)
        return output
        

        