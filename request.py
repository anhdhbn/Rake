import requests

sample_file = open("data/docs/vi/test.txt", 'r')
text = sample_file.read()

url = 'http://localhost:5000/api'
r = requests.post(url,json={
    'text':text,
    'lang':'vi',
    'min_char_length' : 2,
    'max_words_length' : 5,
    'min_keyword_frequency' : 4
    })
print(r.json())