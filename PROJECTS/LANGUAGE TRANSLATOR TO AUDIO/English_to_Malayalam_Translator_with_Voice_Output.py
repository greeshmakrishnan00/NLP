from googletrans import Translator
from gtts import gTTS
import os

# Initialize translator
translator = Translator()

# Get input from user
text = input("Enter text in English: ")

# Speak original English text
english_tts = gTTS(text=text, lang='en')
english_tts.save("english.mp3")

print("\nSpeaking English Text...")
os.system("start english.mp3")  # Windows

# Translate to Malayalam
translated = translator.translate(text, dest='ml')
malayalam_text = translated.text

# Display translation
print("\nMalayalam Translation:")
print(malayalam_text)

# Speak Malayalam translation
malayalam_tts = gTTS(text=malayalam_text, lang='ml')
malayalam_tts.save("malayalam.mp3")

print("\nSpeaking Malayalam Translation...")
os.system("start malayalam.mp3")  # Windows