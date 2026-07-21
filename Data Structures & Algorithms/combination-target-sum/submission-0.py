class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(p, curr, total):
            if total == target:
                comb = curr.copy()
                res.append(comb)
                return
            if p >= len(nums) or total > target:
                return

            curr.append(nums[p])
            dfs(p, curr, total + nums[p])
            
            curr.pop()
            dfs(p + 1, curr, total)

        dfs(0, [], 0)
        return res