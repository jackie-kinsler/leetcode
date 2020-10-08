def isAnagram(s, t): 
    s_letter_count = {}
    t_letter_count = {}

    for char in s: 
        s_letter_count[char] = s_letter_count.get(char, 0) + 1

    for char in t: 
        t_letter_count[char] = t_letter_count.get(char, 0) + 1
    print(s_letter_count)
    print(t_letter_count)

isAnagram('anagram', 'nagaram')
    