#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
# the sum of the two preceding ones, starting from 0 and 1. That is, Given n, calculate F(n).
# link - https://leetcode.com/problems/fibonacci-number/description/ #dd
class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return 0
        if n == 1:
            return 1 # this 2 cases are different we have do calculate them first
        else:
            for i in range(1,n): # this loop is calculating our sum and then we are changing our variable b as the sum of previous elements and a is now previous element of b
                c = a + b
                a = b
                b = c
        return b
