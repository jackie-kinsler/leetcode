class Solution:
    def romanToInt(self, s: str) -> int:
        
        number_lst = []
        
        for char in s:
            if char == "I":
                number_lst.append(1)
            elif char == "V":
                number_lst.append(5)
            elif char == "X":
                number_lst.append(10)
            elif char == "L":
                number_lst.append(50)
            elif char == "C":
                number_lst.append(100)
            elif char == "D":
                number_lst.append(500)
            elif char == "M":
                number_lst.append(1000)
            
        total = number_lst[-1]
            
        for index in range(len(number_lst) - 1):
            current = number_lst.pop()
            next = number_lst[-1]
            if current > next: 
                total -= next
            else: 
                total += next

        return total 

            

                