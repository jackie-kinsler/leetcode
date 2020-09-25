



def groupAnagrams(strs):
    
    final_list = []
    anagram_list = []
    word_dictionary = {}
    
    for word in strs: 
        letter_dict = {}
        for char in word: 
            letter_dict[char] = letter_dict.get(char, 0) + 1
        word_dictionary[word] = letter_dict
        
    print(word_dictionary)
    # {
    # 'eat': {'e': 1, 'a': 1, 't': 1}, 
    # 'tea': {'t': 1, 'e': 1, 'a': 1}, 
    # 'tan': {'t': 1, 'a': 1, 'n': 1}, 
    # 'ate': {'a': 1, 't': 1, 'e': 1}, 
    # 'nat': {'n': 1, 'a': 1, 't': 1}, 
    # 'bat': {'b': 1, 'a': 1, 't': 1}
    # }
    for key in word_dictionary:
        intermediate_list = []
        for word, letters in word_dictionary.items(): 
            if word_dictionary[key] == letters:
                intermediate_list.append(word)
        anagram_list.append(intermediate_list)
    
    anagram_tuple_list = []

    for group in anagram_list: 
        anagram_tuple_list.append(tuple(group))
    
    for group in list(set(anagram_tuple_list)):
        final_list.append(list(group))
    
    return final_list





    #  """Returns list of index positions of large groups.
    #     >>>groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    #     [["bat"],["nat","tan"],["ate","eat","tea"]]
       
    # """
# if __name__ == '__main__':
#     import doctest

#     result = doctest.testmod()
#     if result.failed == 0:
#         print('ALL TESTS PASSED')
        
            