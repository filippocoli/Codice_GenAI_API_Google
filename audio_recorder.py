"""
Questo modulo fornisce una classe per la registrazione dell'audio.
La classe AudioRecorder permette di registrare l'audio da un dispositivo di input,
come un microfono, e ottenere i dati audio sotto forma di array di byte.
"""

import pyaudio

class AudioRecorder:
    def __init__(self):
        self.frames = []

    def record(self, chunk=1024, rate=16000, channels=1):
        audio = pyaudio.PyAudio()

        stream = audio.open(format=pyaudio.paInt16,
                            channels=channels,
                            rate=rate,
                            input=True,
                            frames_per_buffer=chunk)

        print("Premi Invio per iniziare la registrazione...")
        input("")

        print("Registrazione in corso... Premi Ctrl+C per interrompere.")

        try:
            while True:
                data = stream.read(chunk)
                self.frames.append(data)
        except KeyboardInterrupt:
            print("\nRegistrazione interrotta.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

    def get_audio_data(self):
        return b"".join(self.frames)
