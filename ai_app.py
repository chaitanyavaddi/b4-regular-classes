api_key = ""

import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=api_key)

st.title('Medha AI')
content = st.text_input('Enter Prompt:')

btn = st.button('Enter', type='primary')

if btn:
    with st.spinner('thinking..'):

        knowledge = '''
            You are an sales person on behalf of MedhaEduTech.  
            You are a helper for student to decide which course to join. 
            When student asks about any institute, give them suggestions by at the end refer them to 
            Medha edutech gently. Dont argue, gently suggest our IT courses and ask them to call
            at 7013908762
        '''
        response = client.responses.create(
            model="gpt-5.1", 
            input=[
                {
                    'role': 'system',
                    'content': knowledge
                },
                {
                    'role': 'user',
                    'content': content
                }
            ]
        )
        st.write(response.output_text)
