class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-1):
            nums_tmp = nums[i+1:]
            left, right = 0, len(nums_tmp) - 1
            while not left == right:
                if nums[i] + nums_tmp[left] + nums_tmp[right] > 0:
                    right -= 1
                elif nums[i] + nums_tmp[left] + nums_tmp[right] < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums_tmp[left], nums_tmp[right]])
                    right -= 1
        return list(set([tuple(i) for i in answer]))