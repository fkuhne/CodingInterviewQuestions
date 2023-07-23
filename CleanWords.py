# Clean Words from Turing
# Given a string s, return the longest clean word in s. A clean word is a word where every character in it
# exists in both uppercase and lowercase. If multiple clean words are found, return the first occurence.
# If none are found, return an empty string.

#
# THIS IS NOT YET WORKING 100%
#

def add_item_value(list, char, num):
    for index, item in enumerate(list):
        if list[index][0] == char:
            list[index][1] |= {num}
            return
    s = set()
    s |= {num}
    list.append([char, s])

def get_substring_from_indexes(s, indexes):
    word = []
    for index in indexes:
        word += s[index]
    word = ''.join(word)
    return word

def check_clean_word(word):
    print("Checking word",word,"- len(word) =",len(word))
    print("(word[0] * len(word))",(word[0] * len(word)))
    if len(word) > 1 and word != (word[0] * len(word)):
        print(True)
        return True
    else:
        print(False)
        return False

def find_first_clean_word(s, list):
    for item in list:
        word = get_substring_from_indexes(s, item[1])
        if check_clean_word(word):
            return word
    return ''

def find_longest_clean_word(s, list):
    max_size = -1
    for item in list:
        if len(item[1]) > max_size:
            max_size = len(item[1])
            word = get_substring_from_indexes(s, item[1])
    print(word)
    if check_clean_word(word):
        return word
    return ''

def solution(s:str) -> str:
    list = []
    l = s.lower()
    for i, c in enumerate(l):
        add_item_value(list, c, i)
    # find_longest_clean_word(s, list)
    find_first_clean_word(s, list)
    
a='NatbBbyn'
print(a)
print(solution(a))

# b='asdefFfytrRrRriwytequiwyteXxXXXXxxx'
# print(solution(b))

