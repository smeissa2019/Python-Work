The project: 
My goal was to build an artistic Twitter bot that reads from a file that contains Gutenberg book and transform this file into colored faces. However, I found out that it can't be done becasue to have
colored faces you need many words more than 140 charcters, so I changed the idea to count the words and represent them in colors. I also wanted it to be respond to the people when they mention the account

The code:
1- Building the Twitter developer account and getting the authentications Keys (4 keys)
2- I used Tweepy package and the time becasue if you send tweets without spacing betweeb them, Twitter will close the account
3- I built the tweet function with a loop to iterate over the book and pull sentences
4- I also found out that I must include them in try and except to understand the type of error because Twitter can cause different errors and it will not be effective if you don't know
which type stopped the program.
5- My first attempt worked by I got error 187 becasue of the repeated tweets. I searched online for how to solve this problems, I honestly did not found a good solution for it at all.
However, I found the id while I was searching but in another problem not related to the 187, so I tried to apply it and it worked fine inside the console.
6- I thought that print can also pass arguments to a variable not only prints but I was wrong, thanks for correcting that.