"""
Questo modulo si occupa del riconoscimento vocale utilizzando l'API Google Cloud Speech-to-Text.
La funzione recognize_audio prende in input i dati audio e utilizza l'API per
trascrivere il testo parlato, restituendo il testo riconosciuto come output.
"""
from google.cloud import speech_v1p1beta1 as speech
from config import GOOGLE_CLOUD_API_KEY
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_CLOUD_API_KEY
def recognize_audio(audio_data):
    client = speech.SpeechClient()

    config = {
        "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 16000,
        "language_code": "it-IT",
    }

    audio_input = speech.RecognitionAudio(content=audio_data)
    response = client.recognize(config=config, audio=audio_input)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript.strip()
