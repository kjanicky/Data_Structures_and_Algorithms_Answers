# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.
# link - https://leetcode.com/problems/find-closest-number-to-zero/

from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Returns the closest number to zero from the list nums.
        If the closest number is negative but its positive counterpart exists in nums, it returns that positive value.
        """
        closest_number = nums[0]  # Zakładamy, że pierwszy element to najbliższa liczba
        for n in nums:
            if abs(n) < abs(closest_number):
                closest_number = n  # Aktualizujemy najbliższą liczbę

        # Sprawdzamy, czy najbliższa liczba jest ujemna i ma odpowiadającą dodatnią wartość w nums
        if closest_number < 0 and abs(closest_number) in nums:
            return abs(closest_number)
        else:
            return closest_number

# Validation
if __name__ == "__main__":
    solution = Solution()
    nums = [2, -7, -3, 4, 9]
    result = solution.findClosestNumber(nums)
    print("Najbliższa liczba:", result)
