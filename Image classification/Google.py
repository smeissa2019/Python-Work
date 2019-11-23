from google_images_download import google_images_download  
  
response = google_images_download.googleimagesdownload()  
  
search_queries = [ 'John Locke', ] 
  
  source= open('C:/Users/sa418774/Desktop/PyWC/Python-Work/Week 6/book2.txt', 'w', encoding="utf-16", newline='\n')
source.write(text)
def downloadimages(query): 
        arguments = {"keywords": query, "format": "jpg", "limit":20,  "print_urls":True, "size": "medium"}
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
    print()  

    with open('data/locke/locke.txt', 'w') as f: 
    for query in search_queries:
        downloadimages(query)
        f.write("%s\n" % query))