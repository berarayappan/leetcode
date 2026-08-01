class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:  # ← Comes back HERE after elif/else!
            mid = (left + right) // 2  # ← Recalculates with NEW left/right!
            
            # ALL three conditions checked fresh each iteration:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # ← Update left
                # ↓ Loop goes back to while, NOT to elif!
            else:
                right = mid - 1  # ← Update right
                # ↓ Loop goes back to while, NOT to else!
        
        return -1  # ← Only reaches here if while becomes false