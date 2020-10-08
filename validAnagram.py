def isAnagram(s, t): 
    s_letter_count = {}
    t_letter_count = {}
    for char in s: 
        s_letter_count[char] = s_letter_count.get(char, 0) + 1
    for char in t: 
        t_letter_count[char] = t_letter_count.get(char, 0) + 1
    if s_letter_count == t_letter_count:
        return True
    return False 

print(isAnagram('anagram', 'nagaram'))
print(isAnagram('rat', 'car'))
    