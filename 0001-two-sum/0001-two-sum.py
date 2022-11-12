class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for number, n in enumerate(nums):
                if target - n in nums[number + 1:]:
                    return [number, nums[number + 1:].index(target - n) + number + 1]
            