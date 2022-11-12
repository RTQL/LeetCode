class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for index, number in enumerate(nums):
            if target - number in hashtable:
                return [hashtable[target - number], index]
            hashtable[number] = index
            