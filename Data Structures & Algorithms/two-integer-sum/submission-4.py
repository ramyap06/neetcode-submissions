class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if n in nums_dict:
                return [nums_dict[n], i]
            diff  = target - n
            nums_dict[diff] = i
        
