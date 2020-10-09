def isValid(s):
        parens = []
        latest_char = 'empty'
        if s[0] == ']' or s[0] == ')' or s[0] == '}':
            return False 
        
        for char in s: 
            if char == '(' or char == '[' or char == '{':
                parens.append(char)
            elif latest_char == '(' and char == ')':
                parens.pop()
            elif latest_char == '[' and char == ']':
                parens.pop()   
            elif latest_char == '{' and char == '}':
                parens.pop()
            else: 
                parens.append(char)
            if len(parens) == 0: 
                latest_char = 'empty'
            else:
                latest_char = parens[-1]
        if len(parens) == 0: 
            return True
        return False


# print(isValid('[](){}'))
# print(isValid('[]()(('))
print(isValid('(])'))

