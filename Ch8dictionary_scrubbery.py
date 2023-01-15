"""Websters dictionary from Proj. Gutenberg (txt). This
should return a list of unique words, [mostly] cleaned up. """

def step_one():
    """Extracts CapWords"""
    original_file = "GutenDict.txt"
    temp_file = "postscrub1.txt"
    with open(original_file,"r",encoding="utf-8") as iput:
        with open(temp_file, "w",encoding="utf-8") as oput:
            for line in iput:
                if line.isupper() is True:
                    oput.write(line)

def step_two():
    """Remove periods and number 1"""
    original_file = "postscrub1.txt"
    temp_file = "postscrub2.txt"
    with open(original_file, "r",encoding="utf-8") as iput:
        with open(temp_file, "w",encoding="utf-8") as oput:
            for line in iput:
                if ('.' not in line) and ('1' not in line):
                    oput.write(line)

def step_three():
    """Removes dashes."""
    original_file = "postscrub2.txt"
    temp_file = "postscrub3.txt"
    with open(original_file, "r",encoding="utf-8") as iput:
        with open(temp_file, "w",encoding="utf-8") as oput:
            for line in iput:
                oput.write(line.replace('-', ''))

def step_four():
    """Splits to new line for semicolons."""
    original_file = "postscrub3.txt"
    temp_file = "postscrub4.txt"
    with open(original_file, "r",encoding="utf-8") as iput:
        with open(temp_file, "w",encoding="utf-8") as oput:
            for line in iput:
                oput.write(line.replace('; ', '\n'))

def step_five():
    """Kept some title and backmatter words, split to new lines."""
    original_file = "postscrub4.txt"
    temp_file = "postscrub5.txt"
    with open(original_file, "r",encoding="utf-8") as iput:
        with open(temp_file, "w",encoding="utf-8") as oput:
            for line in iput:
                leng = len(line.split())
                if leng <= 4 :
                    oput.write(line.replace(' ', '\n'))

step_one()
step_two()
step_three()
step_four()
step_five()

def rem_dups():
    """Removes all duplicates. This takes a few minutes."""
    original_file = "postscrub5.txt"
    temp_file = "postscrub6.txt"
    unq_words = []
    with open(original_file, "r",encoding="utf-8") as iput:
        with open(temp_file, "w",encoding="utf-8") as oput:
            for line in iput:
                if line not in unq_words:
                    oput.write(line)
                    unq_words.append(line)

rem_dups()
