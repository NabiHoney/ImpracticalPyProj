"""Bar chart for etaoin."""
import pandas as pd

phrase = input()
phrase = phrase.lower().replace(" ","")
phrase_to_string = list(sorted(phrase))
count = pd.Series(phrase_to_string).value_counts()
count_dict = count.to_dict()
sort_dict=list(count_dict)
sort_dict.sort()
sorted_dict = {i: count_dict[i] for i in sort_dict}
for key, value in sorted_dict.items():
    print(key + ": " + str([key] * value))
