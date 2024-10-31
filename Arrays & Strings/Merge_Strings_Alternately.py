#You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.
# link - https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_a = len(word1)
        len_b = len(word2)
        a = 0
        b = 0
        s = [] # we make it an array because string is not mutable object and will increase the complexity
        word = 1 # defining
        while a < len_a and b < len_b: # checking
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1

        while a < len_a:
            s.append(word1[a])
            a += 1

        while b < len_b:
            s.append(word2[b])
            b += 1

        return ''.join(s)

if __name__ == "__main__":
    solution = Solution()
    word1 = "abc"
    word2 = "12345"
    result = solution.mergeAlternately(word1, word2)
    print(result)