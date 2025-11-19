api_key = "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"

from openai import OpenAI
import streamlit as st
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
