def longest_consecutive_sequence(nums):
    longest_streak = 0
    nums = set(nums)
    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums:
                current_streak += 1
                current_num += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak