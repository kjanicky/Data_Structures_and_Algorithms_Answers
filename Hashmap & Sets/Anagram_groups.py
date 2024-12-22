def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]

    return list(anagram_groups.values())


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))