class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        if x < 0: 
            negative = True 
            x *= -1
        else: 
            negative = False
            
        int_str = str(x)

        char_lst = []

        for char in int_str: 
            char_lst.append(char)
        
        reversed_str = ''
        char_lst.reverse()
        reversed_str = reversed_str.join(char_lst).strip('0')
        
        integer = int(reversed_str)
        if integer < (2**31 -1) and integer > (-2**31):
            if negative == True: 
                return -1*int(reversed_str)
            else: 
                return int(reversed_str)
        else: 
            return 0
        
        
        