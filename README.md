# Applicazione di Assistenza per Non Vedenti

Questo è un'applicazione Python che fornisce assistenza per non vedenti utilizzando tecniche di intelligenza artificiale. L'applicazione consente agli utenti di ottenere descrizioni di immagini e riconoscimento di testo da audio.

## Dipendenze

È possibile installare le librerie necessarie utilizzando il file `requirements.txt`.

## Utilizzo

1. Assicurati di avere un ambiente Python 3.x configurato sul tuo sistema.
2. Clona il repository sul tuo sistema.
3. Attiva un ambiente virtuale (opzionale ma consigliato).
4. Installa le dipendenze eseguendo il seguente comando: pip install -r requirements.txt
5. Esegui l'applicazione eseguendo il seguente comando: python main.py


## Descrizione dei File

- `audio_recorder.py`: Contiene la classe per la registrazione dell'audio.
- `speech_to_text.py`: Gestisce il riconoscimento vocale utilizzando l'API Google Cloud Speech-to-Text.
- `text_to_prompt.py`: Gestisce la generazione di testo basata su input utilizzando modelli generativi.
- `prompt_to_description.py`: Gestisce la generazione di descrizioni per immagini utilizzando modelli generativi.
- `text_to_speech.py`: Gestisce la sintesi vocale del testo in audio utilizzando l'API Google Cloud Text-to-Speech.
- `requirements.txt`: Elenco delle librerie Python necessarie per l'applicazione.

## Contributi

I contributi sono benvenuti! Se desideri contribuire a questo progetto, per favore apri una pull request o un problema.

## Licenza

Questo progetto è distribuito con la licenza [MIT License](LICENSE).





