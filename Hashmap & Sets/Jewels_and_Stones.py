class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)  # making ("a","A") set
        count = 0  # defining counter - our var to return
        for stone in stones:
            if stone in s:
                count += 1  # every time there is a stone in jewel add 1 to counter

        return count

