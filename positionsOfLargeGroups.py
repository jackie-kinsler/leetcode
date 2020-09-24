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


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
          
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
            return group

        while len(char_lst) > 1:
            group = check_group_length(char_lst)
            if group >= 3:
                index_lst.append([len(char_lst), len(char_lst) + group - 1])
        
        return sorted(index_lst)



            

