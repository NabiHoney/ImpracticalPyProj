"""Pig latin program."""
print("Enter word to translate: ")
word = input()
to_change = list(word)
new_word = (to_change)
last = to_change[0]
vow_add = ('w', 'a', 'y')
con_add = ('a', 'y')

def change_word():
    """Transpose and add letters."""
    if word[0] == 'aeiou':
        to_change.append(last)
        del to_change[0]
        to_change.extend(vow_add)
    else:
        to_change.append(last)
        del to_change[0]
        to_change.extend(con_add)

change_word()
print(''.join(map(str, new_word)))
