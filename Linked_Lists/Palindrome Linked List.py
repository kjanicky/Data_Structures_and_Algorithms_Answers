class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:  # find the middle node
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:  # reverse
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        first_half = head
        second_half = prev

        while second_half:  # checking the halves
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True