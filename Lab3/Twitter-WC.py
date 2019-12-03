
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


get_ipython().system('curl -s https://course.fast.ai/setup/colab | bash')


# In[45]:


from fastai import *
from fastai.vision import *
from google_images_download import google_images_download 
import pandas as pd
import codecs


# In[5]:


folder = 'disney'
file = '43-0.txt'
file = 'princess.txt'


# In[6]:


path = Path('data')
dest = path/folder
dest.mkdir(parents=True, exist_ok=True)


# In[7]:


path.ls()


# In[8]:


path_img = path/"downloads/all"


# In[9]:


path_img.ls()


# In[9]:


dest = path/folder
dest.mkdir(parents=True, exist_ok=True)


# In[10]:


dest.ls()


# In[27]:


response = google_images_download.googleimagesdownload()  
source= open('data/disney/princess.txt', 'w', encoding="utf-8", newline='\n')

 
search_queries = [ 'alice disney', 'beauty disney', 'cinderella disney', 'ariel disney' ] 
arguments = {"keywords":"alice disney" "beauty disney" "cinderella disney" "ariel disney","limit":20,"print_urls":True}
paths = response.download(arguments)

def downloadimages(query): 
        arguments = {"keywords": query, "format": "jpg", "limit":20,  "print_urls":True, "size": "medium",}
        try: 
             response.download(arguments) 
        except FileNotFoundError: 
             arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":4, 
                     "print_urls":True,  
                     "size": "medium"}
        try: 
            
            response.download(arguments) 
        except: 
            pass  
        

for query in search_queries:
    downloadimages(query)
    source.write(str(paths))
    source.close()
        
     

    

    
       
      
    
    
       
    


# In[29]:


download_images(dest/file, dest, max_pics=200)


# In[13]:


text =  open(dest/'43-0.txt', "r")
print(text.read())


# In[181]:



fnames = get_image_files(path_img)
fnames[:3]


# In[183]:


from random import choice
randing = choice(fnames)


# In[184]:


img_f = randimg
img = open_image(img_f)
img.show(figsize=(5,5))
img.shape


# In[185]:


finallist = []
for i in fnames:
    finallist.append(img_f)
print(finallist)


# In[186]:


random2 = choice(finallist)
print(random2)


# In[187]:


for i in finallist:
    onlynames = []
    
    random3 = random2.name
    onlynames.append(random3)
print(onlynames)


# In[188]:


get_ipython().system('pip install pillow')


# In[189]:


finaltry3 = open_image(random2)
finaltry3.show(figsize=(5,5))


# In[191]:


text=open (dest/'43-0.txt').read()

color_image= np.array(open_image(random2))
color_image = color_image[::3, ::3]


mask = color_image.copy()
mask[color_image.sum(axis=2) == 0] = 255

# some finesse: we enforce boundaries between colors so they get less washed out.
# For that we do some edge detection in the image
edges = np.mean([gaussian_gradient_magnitude(color_image[:, :, i] / 255., 2) for i in range(3)], axis=0)
mask[edges > .08] = 255



cloud = WordCloud(background_color="white", max_words=2000, max_font_size=40, random_state=42, contour_width=3,  mask=mask).generate(text)
image_colors = ImageColorGenerator(mask)

plt.figure(figsize=[20,10])
plt.imshow(cloud.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")

plt.show()


# In[ ]:


import tweepy
from time import sleep



#cwd = os.getcwd() 
#files = os.listdir(cwd)  
#print("Files in %r: %s" % (cwd, files))
#file_lines = my_file.readlines()
#my_file.close()

text=open (dest/'43-0.txt').read()



consumer_key = 'HXJwIytG3G6L8d7MAbmuVkbR7'
consumer_secret = 'yGgw1oJ43EutwInSPifn9U2k4FAIrwrYu82hJzI2OR7wsoaBFK'
access_token = '1194456102529904640-TszAakWUWgP4rzBB0pQZPsMJl9KOok'
access_token_secret = '7DHlXD5gTzV9GCzxZZ4DklPUwoHBt8upELxT7QykFray4'

auth =tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

def tweets():
   for line in text:
    
    def wordcloud():
        cloud = WordCloud(background_color="white").generate(text)
        plt.imshow(cloud)
        plt.axis("off")
        plt.show()
        return plt.show()
    try:
        if line != '\n':
            
           api.update_status(status=wordcloud())
           sleep(300)
               
        else:
            pass
    except tweepy.TweepError as error:
        if error.api_code ==187:
            print(error.reason)
            sleep(2)

tweets()


# In[23]:


get_ipython().system('pip install tweepy')


# In[30]:


get_ipython().system('pip install wordcloud')

