#%%
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob
import nltk
import re
text = strip_headers(load_etext(60457)).strip()
answerUser = strip_headers(load_etext(1524)).strip()
blob = TextBlob(text)

source= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Week 6/book.txt', 'w', encoding="utf-16", newline='\n')
source2= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Week 6/book2.txt', 'w', encoding="utf-16", newline='\n')
source.write(text)
source2.write(answerUser)
source.close
source2.close

pride = source.read()
print(pride[:1000])





#%%
