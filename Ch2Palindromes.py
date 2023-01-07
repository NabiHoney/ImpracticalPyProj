"""Palindrome finder for word lists(one word per line)"""
pali_list = []
with open ('yourfilehere.txt','r',encoding="utf-8") as file:
    for line in file:
        for word in line.split():
            wordr = word[::-1]
            if len(word) > 1 and wordr == word:
                pali_list.append(word)
print(pali_list)
