import streamlit as st
from news_fetcher import NewsFetcher
from df_manager import DataFrameManager
if __name__ == "__main__":
    st.title('ABC Public Relations News App')
    query = st.text_input('Enter your client\'s name, or their company name:')
    if st.button('Get news summaries'):
        if query == '':
            st.write('Searchable query missing. Please try again.')
        else:
            news_fetcher = NewsFetcher(query)
            news = news_fetcher.get_everything() 
            df_manager = DataFrameManager()
            df = df_manager.make_df(news, query) 
            if df.empty:
                st.write('Your search did not return any news. Please try again.')
            else:
                def display_news_element(title, image_url, body, ent_1, url, publisher):
                    st.subheader(title)
                    st.image(image_url, width=200)
                    st.write('Summary: ', body)
                    if ent_1 != None:
                        st.write('Key relative entity: ', str(ent_1))
                    link = '[' + publisher + '](' + url + ')'
                    st.write('Source: ', link)
                    st.text('')
                for i in range(len(df)):
                    title = df['Title'][i]
                    image_url = df['Image URL'][i]
                    summary = df['BART'][i][0]
                    ent_1 = df['NE_1'][i]
                    url = df['URL'][i]
                    publisher = df['Publisher'][i] 
                    display_news_element(title, image_url, summary, ent_1, url, publisher)