#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        for n in nums:
            if n not in nums_count:
                nums_count[n] = 1
            else:
                return True
        return False