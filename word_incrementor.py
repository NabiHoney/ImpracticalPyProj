""" Incrementor for a single word. """
test_list = []
def iscs():
    """Multiplier"""
    with open("your_word.txt", "r", encoding="utf-8") as iput: #notepad, single word, caps
        for line in iput:
            word = line
            count = len(word)
            for i in range(count):
                test_list.append(word)
iscs()
incrms = []
I = ''.join([test_list[idx][:idx + 1]+(",") for idx in range(len(test_list))])
incrms.append(str(I))
print("Your word: ", test_list[0])
print("Incremented by 1: ", incrms)
