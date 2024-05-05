"""
Questo modulo gestisce la sintesi vocale del testo in audio utilizzando l'API Google Cloud Text-to-Speech.
La funzione synthesize_text prende in input un testo e utilizza l'API per generare
un file audio contenente la pronuncia del testo, che può essere riprodotto o salvato come file MP3.
"""
import sounddevice as sd
import numpy as np
from config import GOOGLE_CLOUD_API_KEY
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_CLOUD_API_KEY

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="it-IT",
        name="it-IT-Wavenet-A",  # Imposta il nome della voce Wavenet
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        # name_variant="Wavenet-A"  # Specifica la variante della voce Wavenet
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # Audio binario.
    audio_data = response.audio_content

    # Converte l'audio in NumPy array
    audio_np = np.frombuffer(audio_data, dtype=np.int16)

    # Riproduce l'audio
    sd.play(audio_np, samplerate=16000, blocking=True)

    # Da attivare se vuoi salvare il file audio.
    '''
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    '''