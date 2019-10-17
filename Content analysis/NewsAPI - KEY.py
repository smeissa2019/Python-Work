#%% 
This is my API key
859ef63de36c423994589ced53a4ee68

#This code get the data in json file and print it
#%%
import requests
import json
import pandas

headers = {'Authorization': '859ef63de36c423994589ced53a4ee68'}
top_headlines_url = 'https://newsapi.org/v2/top-headlines'
everything_news_url = 'https://newsapi.org/v2/everything'
sources_url = 'https://newsapi.org/v2/sources'

headlines_payload = {'category': 'politics', 'country': 'us'}
everything_payload = {'q': 'Trump', 'language': 'en', 'sortBy': 'popularity'}
sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}
response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)
response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)
response = requests.get(url=sources_url, headers=headers, params=sources_payload)

pretty_json_output = json.dumps(response.json(), indent=4)
print(pretty_json_output)

# This takes it further to convert from Json to Python, then to save the data as an object data frame using Pandas, and export it in csv file
#%%
import requests
import json
import pandas

headers = {'Authorization': '859ef63de36c423994589ced53a4ee68'}
top_headlines_url = 'https://newsapi.org/v2/top-headlines'
everything_news_url = 'https://newsapi.org/v2/everything'
sources_url = 'https://newsapi.org/v2/sources'

headlines_payload = {'category': 'politics', 'country': 'us'}
everything_payload = {'q': 'Trump', 'language': 'en', 'sortBy': 'popularity'}
sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}
response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)
response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)
response = requests.get(url=sources_url, headers=headers, params=sources_payload)

pretty_json_output = json.dumps(response.json(), indent=4)
response_json_string = json.dumps(response.json())
response_dict = json.loads(response_json_string)
articles_list = response_dict["sources"]
df = pandas.read_json(json.dumps(articles_list))
df.to_csv("C:/Users/sa418774/Desktop/PyWC/Python-Work/Content analysis/Contentana.csv")

# this is the another way to get the top_headlines only
#%%
from newsapi import NewsApiClient
api = NewsApiClient(api_key='859ef63de36c423994589ced53a4ee68')
api.get_top_headlines(category='general',language='en')
api.get_everything(q='Trump')
api.get_sources(category='general', country='us')

# This code gets the top-headlines data as well but it is not recommeded becasue of adding the api key in the Url, but I wanted to try it
#%%
import requests
import json

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&' 'q=Trump&'
       'from=2019-10-16&'
       'sortBy=popularity&'
       'apiKey=859ef63de36c423994589ced53a4ee68')
response = requests.get(url)
print (response.json())


