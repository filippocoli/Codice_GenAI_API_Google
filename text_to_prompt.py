"""
Questo modulo gestisce la generazione di testo basata su input testuali utilizzando modelli generativi.
La funzione generate_response prende in input un testo e genera una risposta
utilizzando un modello generativo specifico, restituendo la risposta generata come output.
In questo caso il modello ha un compito specifico: trasformare l'input semplice dell'utente in un prompt testuale dettagliato
che andrà in input al modello di generazione di descrizione da immagini per ottimizzare la richiesta.
"""

import vertexai
import vertexai.preview.generative_models as generative_models
from vertexai.preview.generative_models import GenerativeModel, Part
from config import GOOGLE_CLOUD_API_KEY
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_CLOUD_API_KEY

def generate_response(input_text):
  vertexai.init(project="clear-vision-417509", location="us-central1")
  textsi_1 = """Sei un agente che deve interpretare la richiesta dell\'utente per un dispositivo per non vedenti che risponde alle domande dell\'utilizzatore basandosi sull\'immagine ricevuta. Utilizza tecniche di NLP per comprendere il significato della richiesta dell\'utente e estrarre le informazioni rilevanti. In base all\'analisi del linguaggio naturale, genera un prompt che includa le informazioni estratte dalla richiesta dell\'utente e che sia ottimizzato per l\'algoritmo che analizza le immagini. Il prompt dovrebbe essere formulato in modo da guidare l\'algoritmo nell\'ottenere l\'informazione desiderata dall\'immagine. La richiesta non deve essere troppo lunga e generica. Ometti la scritta: "Prompt per l\'algoritmo di analisi dell\'immagine:".
  Per esempio:
  Ad esempio, se l\'utente chiede \"Aiutami a capire dove mi trovo\", il prompt potrebbe essere formulato come \"Genera una descrizione verbale dettagliata dell\'ambiente circostante sulla base dell\'immagine fornita. L\'obiettivo è fornire informazioni utili e significative per aiutare i non vedenti a comprendere il contesto e le caratteristiche dell\'ambiente. Assicurarsi di includere dettagli come la disposizione degli oggetti, la presenza di persone o animali, le caratteristiche dell\'architettura circostante, il terreno e altre informazioni rilevanti per consentire una comprensione completa e sicura dello spazio. Includete anche l\'avvertimento di alcuni potenziali pericoli. Iniziare la frase con ″Si trova....″. Non includere la descrizione dei suoni.\""""

  generation_config = {
      "max_output_tokens": 8192,
      "temperature": 1,
      "top_p": 0.95,
  }

  safety_settings = {
      generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
  }
  model = GenerativeModel(
    "gemini-1.5-pro-preview-0409",
    system_instruction=[textsi_1]
  )
  chat = model.start_chat()
  response = chat.send_message(
      [input_text],
      generation_config=generation_config,
      safety_settings=safety_settings
  )
  return response