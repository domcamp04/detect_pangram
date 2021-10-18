# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# ex.1
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# ex.2
# Input: sentence = "leetcode"
# Output: false
str1= 'abcdefghijklmnopqurstuvxwyz'
def check_pangram(str):
    if len(set('abcdefghijklmnopqrstuvwxyz') - set(str.lower())) ==  0 :
        return True

    return False

if(check_pangram('the quick brown fox jumps over the lazy dog')):
    print("This is a pangram")
else:
    print("This is not a pangram")
if(check_pangram('leetcode')):
    print("This is a pangram")
else:
    print("This is not a pangram")


def pana(st):
    my_list = []
    for i in st:
        if i not in my_list:
            my_list.append(i)
    if len(my_list) == 26:
        return True
    return False
print(pana("thequickbrownfoxjumpsoverthelazydog"))
print(pana("leetcode"))
print(pana("qweryuiopasdfghjklzxcvbnnncdsfsdf"))