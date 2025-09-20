from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Check if the target exists in the list
        if target in nums:
            # If it exists, return its index
            return nums.index(target)
        else:
            # If it does not exist, return -1
            return -1