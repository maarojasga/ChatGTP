
import streamlit as st
import openai
from PIL import Image

image = Image.open('latin.png')

st.image(image, width=200)

lang = st.radio(
    "Lenguaje - Language",
    ('Español', 'English'))

if lang == 'Español':

    st.title('Instrucciones de uso')
    st.text('Usamos la tecnología de ChatGTP para dar respuesta a tus preguntas y\nte permitimos poder descargarlas en un archivo de texto')

    openai.api_key = "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" 

    question = st.text_input("Escribe tu pregunta: ")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": question},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content



    st.write('La respuesta es:\n', result)


    st.download_button('Descarga', result, 'resultado.txt')

else:
    st.title('Instrucciones de uso')
    st.text('We use ChatGTP technology to answer your questions and allow\nyou to download them as a text file.')

    openai.api_key = "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" 

    question = st.text_input("Write your question: ")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": question},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content



    st.write('Your answer is:\n', result)


    st.download_button('Download', result, 'result.txt')

