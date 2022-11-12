class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for index, number in enumerate(nums):
            value = target - number
            if value in hashtable:
                return [hashtable[value], index]
            hashtable[number] = index
            