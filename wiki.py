from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
tokenizer = RegexpTokenizer(r'\w+')
filterdText=tokenizer.tokenize('Hello Guru99, You have build a very good site and I love visiting your site.')
sent_text=sent_tokenize('Hello Guru99, You have build a very good site and I love visiting your site.')
print(sent_text)
print(filterdText)