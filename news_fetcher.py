import requests
import streamlit as st
from newsapi import NewsApiClient
class NewsFetcher(object):
    API_KEY = '6e581b364f2c47579d6f636e186a164a' 
    def __init__(self, query):
        self.query = query  
        self.api = NewsApiClient(api_key=NewsFetcher.API_KEY)
    def get_everything(self):
        from datetime import datetime
        try:
            news = self.api.get_everything(q=self.query, 
                                    language='en',
                                    page_size=5, 
                                    sort_by='relevancy') 
            return news
        except requests.exceptions.ConnectionError:
            pass