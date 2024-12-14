class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}
        for p in s:
            if p in mapping.values():
                stack.append(p)
            elif p in mapping.keys():
                if not stack or mapping[p] != stack.pop():
                    return False
        return not stack