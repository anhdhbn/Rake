from __future__ import absolute_import
from __future__ import print_function
import rake

stoppath = "data/stoplists/en.txt"

min_char_length = 2
max_words_length = 5
min_keyword_frequency = 1
rake_object = rake.Rake(stoppath, min_char_length, max_words_length, min_keyword_frequency)

sample_file = open("data/docs/en/test.txt", 'r', encoding="iso-8859-1")
text = sample_file.read()
keywords = rake_object.run(text)

# print(keywords)

# for k in keywords:
#     print(k[0], k[1])
# for k in keywords:
#     print(k[0], k[1])