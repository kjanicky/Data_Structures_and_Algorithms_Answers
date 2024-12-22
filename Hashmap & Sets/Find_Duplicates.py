class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        duplicates = []
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
                if my_dict[num] == 2:
                    duplicates.append(num)
            else:
                my_dict[num] = 1
        if not duplicates:
            return False
        else:
            return True
# https://leetcode.com/problems/contains-duplicate/description/