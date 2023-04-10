from revChatGPT.V1 import Chatbot
import speech_recognition as speech
from gtts import gTTS
import os
import pygame
import time

class Main:
    """
    Classe principale encapsulant la logique du programme.
    """

    def __init__(self):
        self.chatbot = Chatbot(config={"session_token" : ""})
        self.wake_word = "Hey Pascal"
        self.audio_folder_location = "audio/"

    def get_audio_input(self):
        """
        Enregistre un message audio et retourne une transcription en texte.
        """
        # Initialize recognizer class (for recognizing the speech)
        recognize = speech.Recognizer()
        language = "fr"
        # Reading Microphone as source
        # listening the speech and store in audio_text variable
        with speech.Microphone() as source:
            print("Talk")
            recognize.adjust_for_ambient_noise(source, duration=0.2)

            audio_text = recognize.listen(source)
            print("Done listening")

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            speech_to_text_result = recognize.recognize_google(audio_text, language=language)

            return speech_to_text_result

        except:
            print("Sorry, I did not get that")
            return None

    def play_audio(self, audio_file):
        """
        Joue un fichier audio.
        """
        # Initialiser pygame
        pygame.init()

        # Charger le fichier MP3
        pygame.mixer.music.load(audio_file)

        # Jouer le fichier MP3
        pygame.mixer.music.play()

        # Garder le programme en cours d'exécution jusqu'à ce que le MP3 soit terminé
        while pygame.mixer.music.get_busy():
            continue

    def save_audio(self, response):
        """
        Enregistre un message audio dans un fichier et retourne le nom du fichier.
        """
        language = 'fr'
        tts = gTTS(text=response, lang=language)
        responseDynamique = int(time.time())
        tts.save("audio/"+ str(responseDynamique) + ".mp3")
        return str(responseDynamique) + ".mp3"

    def query_chat_gpt(self, message):
        """
        Interroge le chatbot GPT-3 avec un message et retourne la réponse.
        """
        for data in self.chatbot.ask(message):
            chat_gpt_answer = data["message"]
        return chat_gpt_answer

    def run(self):
        """
        Boucle principale qui écoute les entrées audio, traite les demandes et renvoie des réponses audio.
        """
        while True:
            speech_to_text_result = self.get_audio_input()

            if self.wake_word.lower() in speech_to_text_result.lower():
                speech_to_text_result = speech_to_text_result.replace(self.wake_word,"").strip()

            if speech_to_text_result:
                chat_gpt_answer = self.query_chat_gpt(speech_to_text_result)
                audio_file_name = self.save_audio(chat_gpt_answer)
                self.play_audio(self.audio_folder_location + audio_file_name)

if __name__ == "__main__":
    main = Main()
    main.run()
