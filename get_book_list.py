import requests
import os
# extract the book name and corresponding url from the Best_Books_Ever_Goodreads.html
url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever'
response = requests.get(url)
with open(os.path.join(url.split('/')[-1]), mode='wb') as file:
        file.write(response.content)
