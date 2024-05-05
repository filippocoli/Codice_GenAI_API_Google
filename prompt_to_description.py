"""
Questo modulo si occupa della generazione di descrizioni per immagini utilizzando modelli generativi.
La funzione generate_description prende in input una prompt e un'immagine,
utilizzando un modello generativo per generare una descrizione dell'immagine,
restituendo la descrizione generata come output.
"""
import vertexai
import vertexai.preview.generative_models as generative_models
from vertexai.preview.generative_models import GenerativeModel
from config import GOOGLE_CLOUD_API_KEY
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_CLOUD_API_KEY

def generate_description(prompt_input,image):
    vertexai.init(project="clear-vision-417509", location="europe-west9")
    model = GenerativeModel("gemini-1.0-pro-vision-001")
    response = model.generate_content(
        [
            prompt_input,
            image
        ],
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.1,
            "top_p": 1,
            "top_k": 32
        },
        safety_settings={
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        stream=False,  # Imposto stream a False per ottenere la stringa direttamente
    )

    # Concateno tutte le risposte in una singola stringa
    description = response.text
    return description
