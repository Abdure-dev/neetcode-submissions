from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #we are given array
        # we need to find a contiguos array
        count = 0
        #it passed the test, so now improve it
        p = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            p += num
            count += seen[p-k]
            seen[p] += 1

                
        return count
        
        