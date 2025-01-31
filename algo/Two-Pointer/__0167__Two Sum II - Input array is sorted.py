class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None or len(numbers) == 0:
            return []
        
        left, right = 0, len(numbers) - 1
        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left + 1, right + 1]
            elif twoSum < target:
                left += 1
            else:
                right -= 1
        return []