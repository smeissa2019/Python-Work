#%%
This is my API key
859ef63de36c423994589ced53a4ee68
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

#%%
