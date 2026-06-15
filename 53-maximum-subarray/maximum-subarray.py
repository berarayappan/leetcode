class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        current_sum = nums[0]
        best_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # reset or continue
            best_sum = max(best_sum, current_sum)       # update best

        return best_sum