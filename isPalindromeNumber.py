class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: 
            return False
        if x >= 0 and x <= 9:
            return True
        
        num_str = str(x)
        reversed_str = num_str[::-1]
        
        if num_str == reversed_str: 
            return True
        return False 
        
        