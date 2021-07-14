from gtts import gTTS
import os
import random
name = str(random.random())
fh = open(input("Enter Filename: "), "r")
newText = fh.read().replace("\n", "")
language = 'en'
output = gTTS(text=newText, lang=language, slow=False)
output.save(name+'.mp3')
fh.close()
os.system("start "+name+".mp3")

