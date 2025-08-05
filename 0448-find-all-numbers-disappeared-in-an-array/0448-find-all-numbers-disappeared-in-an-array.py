class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        complete = set(range(1,n+1))
        new_nums = set(nums)
        result = complete - new_nums
        return list(result)