import requests
from bs4 import BeautifulSoup
resp = requests.get("https://subslikescript.com/movies_letter-M")

movie_website = resp.text

soup = BeautifulSoup(movie_website, 'lxml')

article = soup.find('article', class_ = 'main-article')

link_movie = article.find_all('a', href =True)

BASE_URL = "https://subslikescript.com/"
# print(type(link_movie))
for data in link_movie:
    print()
    link = data.get('href')
    # print(link)

    new_req = requests.get(BASE_URL + link)
    context = new_req.text

    new_soup = BeautifulSoup(context, 'lxml')

    movie_title = new_soup.find('h1')
    print(movie_title)

    try:
        plot = new_soup.find('p',class_="plot")
        print(plot.getText())
    except AttributeError as e:
        plot = ''

    sub_title = new_soup.find('div', class_ ='full-script')
    print(sub_title.getText())
