# Simple integración de ChatGTP con Streamlit

Desarrollado con Streamlit, cuenta con una interfaz gráfica sencilla y la capacidad para descargar un archivo con las respuestas obtenidas.

## Instalación

    git clone https://github.com/maarojasga/ChatGTP
    cd ChatGTP
    pip install -r requirements.txt

## API KEY

1. Ve a la página de OpenAI y haz clic en "Get Started for Free" o "Sign up" en la esquina superior derecha.

2. Ingresa tu dirección de correo electrónico y haz clic en "Get Started".

3. Sigue las instrucciones en pantalla para crear una cuenta. Deberás proporcionar algunos detalles personales y de la empresa (si es que corresponde).

4. Una vez que hayas creado tu cuenta, inicia sesión en el dashboard de OpenAI y haz clic en la pestaña "API Keys" en la barra lateral izquierda.

5. Haz clic en "Create API Key" y sigue las instrucciones para crear una nueva API key.

6. Copia tu API key y guárdala en un lugar seguro.

## Siguientes pasos

1.  Reemplaza con la llave que generaste.

    openai.api_key = os.getenv('KEY') # API KEY -> ChatGTP

2. Ejecuta

    streamlit run app.py





