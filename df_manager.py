import pandas as pd 
from text_scraper import TextScraper
from nlp_tasks import NLP
class DataFrameManager(object):
    def __init__(self):
        pass
    def make_df(self, news, query):
        rows = self.make_rows_from_json(news, query)
        col_names = ['Publisher', 'Title', 'URL', 'Image URL', 'Date', 'Scrape', 'BART', 'NE_1']
        df = pd.DataFrame(rows, columns=col_names)
        return df 
    @staticmethod
    def make_rows_from_json(news, query):
        rows = []
        if news['totalResults'] != 0:
            for article in news['articles']:
                publisher = article['source']['name']
                title = article['title']
                url = article['url']
                image_url = article['urlToImage']
                date = article['publishedAt']
                scraper = TextScraper(url)
                scrape = scraper.scrape()
                nlp = NLP()
                if scrape == '':
                    BART = 'Not available...'
                else:
                    BART = nlp.summarise_with_BART(scrape)
                key_ent = nlp.NER_with_SpaCy(scrape, query)
                ent_1 = key_ent[0][0] 
                row = [publisher, title, url, image_url, date, scrape, BART, ent_1]
                rows.append(row)
        return rows