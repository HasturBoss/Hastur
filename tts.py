import pyttsx3

str = "C://Users//micor//Desktop//YouTube//pyttsx3//test.mp3"
txt = "C://Users//micor//Desktop//YouTube//pyttsx3//test.txt"

def tts(str):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    volume = engine.getProperty('volume') 
    engine.setProperty('volume',1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    f = open(txt, "r")
    text = f.read()
    f.close()

    engine.save_to_file(text, str)
    engine.runAndWait()

if __name__=='__main__':
    tts(str)