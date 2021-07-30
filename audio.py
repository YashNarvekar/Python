from gtts import gTTS
import os
try:
    text = 'Hello everyone!! lets learn python'
    language= 'es'
    obj = gTTS(text=text,lang=language,slow=False)
    obj.save("text_to_audio.mp3")
    os.system("text_to_audio.mp3")
    print("completed")
except:
    print("Sorry...cant convert ur command")