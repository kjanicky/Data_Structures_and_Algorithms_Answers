class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations: # using stacks to check
            if o == 'C':
                record.pop()
            elif o == 'D':
                record.append(record[-1] * 2)
            elif o == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(o))
        return sum(record)
# https://leetcode.com/problems/baseball-game/