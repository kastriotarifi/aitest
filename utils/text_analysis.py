import spacy
from collections import Counter
from gtts import gTTS

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, num_keywords=5):
    doc = nlp(text)
    words = [token.text for token in doc if not token.is_stop and len(token.text) > 2]
    return [keyword[0] for keyword in Counter(words).most_common(num_keywords)]

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    filename = "output.mp3"
    tts.save(filename)
    return filename
