# class Solution:
#     def largeGroupPositions(self, s: str) -> List[List[int]]:
          
#         index_lst = []
#         char_lst = []
        
#         index = len(s) - 1
        
#         for char in s: 
#             char_lst.append(char)
        
#         initial_length = len(char_lst)
        
#         for count in range(initial_length - 1):
#             if len(char_lst) > 1: 
#                 length_now = len(char_lst)
#                 current = char_lst.pop()
#                 next = char_lst[-1]
#                 group_length = 1
#                 while current == next: 
#                     group_length += 1
#                     if len(char_lst) > 1:
#                         current = char_lst.pop()
#                         next = char_lst[-1]
#                     else: 
#                         break
#                 if group_length >= 3: 
#                     index_lst.append([len(char_lst), length_now - 1])
            
#         return sorted(index_lst)

import unittest


def largeGroupPositions(s):

    """Returns list of index positions of large groups.
        >>> largeGroupPositions("abbxxxxzzy")
        [[3, 6]]
        >>> largeGroupPositions("abc")
        []
        >>> largeGroupPositions("abcdddeeeeaabbbcd")
        [[3, 5], [6, 9], [12, 14]]
        >>> largeGroupPositions("aaa")
        [[0, 2]]
    """
        
    index_lst = []
    char_lst = []
    for char in s: 
        char_lst.append(char)

    def check_group_length(input_lst): 
        group = 1
        while len(input_lst) > 1: 
            current_char = input_lst.pop()
            next_char = input_lst[-1]
            if current_char == next_char: 
                group += 1
            else: 
                break
            if group >= 3 and len(char_lst) == 1:
                char_lst.pop()
                break
        return group

    while len(char_lst) > 1:
        group = check_group_length(char_lst)
        if group >= 3:
            index_lst.append([len(char_lst), len(char_lst) + group - 1])
    
    return sorted(index_lst)

class MyUnittest(unittest.TestCase):

    def test_largeGroupPositions(self): 
        assert largeGroupPositions("abbxxxxzzy") == [[3, 6]]

    def test_largeGruopPositions_2(self):
        self.assertEqual(largeGroupPositions("aaa"), [[0, 2]])

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     import doctest

#     result = doctest.testmod()
#     if result.failed == 0:
#         print('ALL TESTS PASSED')


            

