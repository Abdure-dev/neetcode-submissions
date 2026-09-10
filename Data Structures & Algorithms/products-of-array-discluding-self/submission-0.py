class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]*n
        left = [1]*n
        result = [1]*n

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            right[j] = right[j+1]*nums[j+1]
        for i in range(n):
            result[i] = right[i]*left[i]
        return result


        
        