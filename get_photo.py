'''
Questo modulo permette di scattare una fotografia utilizzando la fotocamera principale del dispositivo.
L'immagine viene salvata in un file .jpg.
'''

import cv2

def take_and_save_photo(filename='photo.jpg'):
    # Inizializza il video capture object con l'ID della webcam (0 per la webcam predefinita)
    cap = cv2.VideoCapture(0)

    # Controlla se la webcam è stata aperta correttamente
    if not cap.isOpened():
        print("Impossibile aprire la webcam")
        return

    # Legge un frame dalla webcam
    ret, frame = cap.read()

    # Chiude la webcam
    cap.release()

    # Controlla se il frame è stato letto correttamente
    if not ret:
        print("Impossibile leggere il frame")
        return

    # Salva il frame come immagine
    cv2.imwrite(filename, frame)
    print(f"Immagine salvata come {filename}")

# Esempio di utilizzo della funzione
#take_and_save_photo('photo.jpg')