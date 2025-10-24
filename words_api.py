import requests

import streamlit


word = streamlit.text_input('Enter a word')
btn = streamlit.button('Find', type='primary')
if btn:
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    res = response.json()
    streamlit.write(res[0]['meanings'][0]['definitions'][0]['definition'])