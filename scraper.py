import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(keyword):
    url = f"https://en.wikipedia.org/wiki/{keyword}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        paragraphs = soup.find_all('p')
        content = ' '.join([p.text for p in paragraphs if len(p.text) > 50])

        return {
            'title': title,
            'url': url,
            'content': content
        }
    
    else:
        return None