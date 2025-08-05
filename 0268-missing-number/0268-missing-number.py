class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        while n>=0 :
            if n not in nums:
                return n
                break
                
            else:
                n-=1

        