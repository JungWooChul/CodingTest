class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for idx in range(len(nums)):
            if nums[idx] == target:
                if start == -1:
                    start, end = idx, idx
                else:
                    end = idx
        return [start, end]
        