import streamlit as st
import requests


res = requests.get('https://openwhyd.org/hot/electro?format=json')

if res.status_code == 200:

    res = res.json()
    tracks = res['tracks']


    cols = st.columns([1])


    with cols[1]:
        st.subheader('Musicon')
        search_phrase = st.text_input('Search a Track', placeholder='🔍  Search a Track', label_visibility='collapsed')
        st.table(tracks)
        # for track in tracks:
        #     if search_phrase in track['name']:
        #         with st.container(border=True):
        #             cols1 = st.columns([3, 2])
        #         with cols1[0]:
        #             title = track['name']
        #             st.write(title[:35] + '...')
        #             #  st.divider()
        #             st.write(f"🎙️ {track['uNm']}")
        #             url = track['trackUrl']
        #             st.link_button('Play Now', f"https:{url}", type='primary')
        #         with cols1[1]:
        #             st.image(track['img'])




