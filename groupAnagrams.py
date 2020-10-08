def groupAnagrams(strs):
    anagram_list = []
    anagram_dictionary = {}
    for word in strs: 
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dictionary:
            anagram_dictionary[sorted_word] = [word]
        else: 
            words_list = anagram_dictionary.get(sorted_word)
            words_list.append(word)
            anagram_dictionary[sorted_word] = words_list
    for item in anagram_dictionary.values():
        anagram_list.append(item)
    return anagram_list
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))

