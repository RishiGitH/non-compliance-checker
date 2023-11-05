import requests
from bs4 import BeautifulSoup
from api.utills.exceptions import CustomAPIException

class WebScraper:
    def __init__(self, url):
        self.url = url

    def get_website_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.RequestException as err:
            raise CustomAPIException(detail='Unable to scrape the given URL. Please check the URl provided', status_code=400)

        return response.text

    def extract_paragraphs(self):
        webpage_content = self.get_website_content()
        soup = BeautifulSoup(webpage_content, 'html.parser')
        paragraphs = soup.find_all('p')

        return [paragraph.text for paragraph in paragraphs]