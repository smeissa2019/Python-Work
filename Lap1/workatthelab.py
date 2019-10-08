


#%%
import random
w = []
sahar = []        

def sum_random(y):
        x = random.randint(0,110) 
        for i in range(x):
            if i < int(y):
                z = x + 1
                w.append(z)
            if i ==y:
                break
        sahar = sum(w)
        print(sahar)

sum_random(6)

#%%
