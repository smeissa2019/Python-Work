#%%
from random import choice
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob
import nltk
text = strip_headers(load_etext(60457)).strip()
answerUser = strip_headers(load_etext(1524)).strip()
blob = TextBlob(text)

source= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Week 6/book.txt', 'w', encoding="utf-16", newline='\n')
source2= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Week 6/book2.txt', 'w', encoding="utf-16", newline='\n')
source.write(text)
source2.write(answerUser)
source.close
source2.close

z = []
x = choice(text)
answerUser = input(x).strip().lower()
y = 1
while y >= 1:
    if answerUser != "lol stop it":
        answerUser = input("but Why?").strip().lower()
        def analysis():
         obj= TextBlob(answerUser)
         z= obj.sentiment.polarity
        if z == 0:
             print("I am not sure if you like me or not")
        elif z == 1:
             print("I'm happy you like my questions so far, here is another one")
        else:
             print("but why are you mad?")
             
    else:
        print("Oh ..Okay")
        exit()

        


