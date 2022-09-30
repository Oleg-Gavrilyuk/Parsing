import bs4
import requests

KEYWORDS = ['web', 'basic', 'IT', 'python']
URL = 'https://habr.com'
response = requests.get(URL)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    h2 = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    href = h2.find(class_='tm-article-snippet__title-link').attrs['href']
    URL2 = f'{URL}{href}'
    response2 = requests.get(URL2)
    text2 = response2.text
    soup2 = bs4.BeautifulSoup(text2, features='html.parser')
    new_article = soup2.find('article')
    collection = new_article.find_all('p')

    for choice in collection:
        for words in KEYWORDS:
            if words in choice.text:
                date = article.find(class_='tm-article-snippet__datetime-published').text
                header = h2.find('span').text
                print(f'{date} - {header} - {URL2}')
                break
        break



