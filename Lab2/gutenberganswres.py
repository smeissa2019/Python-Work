# I merged 1 & 2
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
# 3. Create a TextBlob from the variable above. This may involve locating the end of the header. 
# Save the resulting TextBlob for use in the following cells. 
#%%
sahar = TextBlob(text)
sahar.word_counts['girl'] # it counts how many times the word girl appears

# Write code that finds the top 5 longest sentences in the work. You may store or display them however you choose, and you may build off of the code above that finds the longest sentence.
#%%
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob
from operator import itemgetter 
import nltk
import re
text = strip_headers(load_etext(60457)).strip()
blob = TextBlob(text)
source= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Lab2/book.txt', 'w', encoding="utf-16", newline='\n')
source.write(text)
source.close
max = 0
index = 0

z=[]

for key, sentence in enumerate(blob.sentences):
     z.append((sentence,len(sentence.words)))
     if(len(sentence.words) > max):
        max = len(sentence.words)
        index = key
sorted(z, key = itemgetter(1))


#%%
#we don't have access to create the tables

       
    





       
       

     






