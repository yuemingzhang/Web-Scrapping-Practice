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

# Open each book's link to get the book information
for book_link in df['book_link']:
    link = urllib.request.urlopen(book_link)
    soup = BeautifulSoup(link, 'html.parser')
    soup.find_all('span', itemprop="name")
    # test below

    # first book's link
    df['book_link'][0]
    
    # get star ratings
    import re
    link = urllib.request.urlopen(df['book_link'][0])
    booksoup = BeautifulSoup(link, 'html.parser')
    rating_details = booksoup.find_all('script', type="text/javascript+protovis")[0].string
    five_star = int(re.findall(r'\d+', rating_details)[0])
    four_star = int(re.findall(r'\d+', rating_details)[1])
    three_star = int(re.findall(r'\d+', rating_details)[2])
    two_star = int(re.findall(r'\d+', rating_details)[3])
    one_star = int(re.findall(r'\d+', rating_details)[4])
    
    # get rating count
    rating_count = int(booksoup.find_all('meta', itemprop="ratingCount")[0]['content'])
    rating_count
    
    # get review count
    review_count = int(booksoup.find_all('meta', itemprop="reviewCount")[0]['content'])
    review_count
    
    # get genres list
    genre = booksoup.find_all('div', class_="elementList ")
    genre1 = genre[0].text.strip().split('\n')[-4].strip()
    genre2 = genre[1].text.strip().split('\n')[-4].strip()
    genre3 = genre[2].text.strip().split('\n')[-4].strip()
    genre4 = genre[3].text.strip().split('\n')[-4].strip()
    genre1,genre2,genre3,genre4
    
    genre5 = booksoup.find_all('div', class_="elementList elementListLast")[0].text.strip().split('\n')[-4].strip()
    genre5

# get 5 reviews
review = []
for i in range(5):
    path = booksoup.find_all('div', class_="reviewText stacked")[i]
    anchors = path.find_all('span', style="display:none")[-1]
    review.append(anchors.text.replace("\\", "").replace("\n", ""))
review
    
# year published
path = booksoup.find('div', id_="details")
anchors = path.find_all('div', class_="row")
