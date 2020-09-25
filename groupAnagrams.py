



def groupAnagrams(strs):
    
    anagram_list = []
    word_dictionary = {}
    
    for word in strs: 
        letter_dict = {}
        for char in word: 
            letter_dict[char] = letter_dict.get(char, 0) + 1
        word_dictionary[word] = letter_dict

        print(letter_dict)
    print(word_dictionary)



    #  """Returns list of index positions of large groups.
    #     >>>groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    #     [["bat"],["nat","tan"],["ate","eat","tea"]]
       
    # """
# if __name__ == '__main__':
#     import doctest

#     result = doctest.testmod()
#     if result.failed == 0:
#         print('ALL TESTS PASSED')
        
            