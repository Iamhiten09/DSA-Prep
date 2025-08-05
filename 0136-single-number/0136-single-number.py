class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+= 1
            else:
                freq[num] = 1

        for key, val in freq.items():
            if val == 1:
                return key