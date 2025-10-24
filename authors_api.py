




import requests
res = requests.get('https://poetrydb.org/author')
res = res.json()
authors = res['authors']

import streamlit


selected_author = streamlit.selectbox('Select Author', authors)


res2 = requests.get(f'https://poetrydb.org/author/{selected_author}/title')
res2 = res2.json()

# streamlit.write(res2)

for i, title in enumerate(res2):
    streamlit.write(f"{i}. {title.get('title')}")