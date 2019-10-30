#%%
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob
import nltk
import re
text = strip_headers(load_etext(60457)).strip()
blob = TextBlob(text)
source= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Lab2/book.txt', 'w', encoding="utf-16", newline='\n')
source.write(text)
source.close
sahar = TextBlob(text)
sahar.word_counts['girl'] # it counts how many times the word girl appears
#%%
max = 5
x = 0


#%%
#we don't have access to create the tables

       
    





       
       

     






