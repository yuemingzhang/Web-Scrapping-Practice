# get html page
import urllib.request
url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
page = urllib.request.urlopen(url)

# extract names from the html page
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')
soup.find_all('span',itemprop="name")

# check the length, confirm there are 100 book titles with 100 author names
len(soup.find_all('span',itemprop="name"))

# save the book titles and authors in the dataframe
import pandas as pd
book_list = []
for i in range(0, len(soup.find_all('span',itemprop="name")), 2):
    book_title = soup.find_all('span',itemprop="name")[i].string
    author = soup.find_all('span',itemprop="name")[i+1].string
    book_list.append({'book_title': book_title,
                      'author': author})
df = pd.DataFrame(book_list, columns = ['book_title', 'author'])
df

# extract urls from the html page
links = []
for i in soup.find_all(itemprop="url"):
    link = i.get("href")
    links.append(link)
links

# check the number of urls, confirm there are 100 book short url and 100 author links
len(links)

# save book links in the dataframe
book_links = []
for i in range(0, len(links), 2):
    book_links.append('https://www.goodreads.com'+links[i])
    df['book_link'] = pd.DataFrame(book_links)
df
