from random import choice
print("hi")
from textblob import TextBlob
import nltk
questions = ["Why the sky is blue?", "Why the clouds are not pink? I love pink color? why?", "Why there is a face on the moon?", "Are you a pirate?", "Where are all the dinasours", "Why I must go to school every single day?"]
z = []
x = choice(questions)
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
        