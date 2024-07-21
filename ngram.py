def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)
    
    return list(anagrams.values())


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(a)
print(result)  # خروجی: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]