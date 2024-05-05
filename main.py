from PIL import Image
import io
from vertexai.preview.generative_models import Part
from text_to_speech import synthesize_text
from speech_to_text import recognize_audio
from audio_recorder import AudioRecorder
from text_to_prompt import generate_response
from prompt_to_description import generate_description
from get_photo import take_and_save_photo

if __name__ == '__main__':
    #Scatta la foto e la salva in una variabile
    istantanea = take_and_save_photo('photo.jpg')
    #Inizializza microfono
    recorder = AudioRecorder()
    #Inizia registrazione
    recorder.record()
    #Salva registrazione ottenuta
    audio_data = recorder.get_audio_data()
    if audio_data:
        text = recognize_audio(audio_data)
        print("Hai detto:", text)
        #Attivare per inserire prompt come testo
        '''input_text = input("Inserisci la tua domanda: ")'''
        #Passo al modello l'input vocale e lo trasormo in un prompt adatto ad ottenre una descrizione dell'immagine
        response = generate_response(text)
        prompt_input = response.text

        #Trasformo l'immagine in modo che sia gestibile dal modello
        image = Image.open('photo.jpg')
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='JPEG')  # Salva l'immagine come JPEG
        image1 = Part.from_data(data=image_bytes.getvalue(), mime_type="image/jpeg")

        #Ottiene la descrizione passando come parametro l'immagine e il prompt
        description = generate_description(prompt_input, image1)
        # Stampo la descrizione generata
        print(description)

        #Ottengo l'audio della descrizione passando come parametro il testo e lo riproduco
        synthesize_text(description)
