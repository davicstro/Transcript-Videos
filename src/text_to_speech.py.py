from gtts import gTTS

#Ler texto do arquivo
with open(f'/mnt/c/Users/Davi/Documents/ksjakd/transcript/Ad7D2pkFNdA-base.txt', "r") as text_file:
    transcription = text_file.read()
#print(audio_transcription)

tts = gTTS(transcription, lang ="pt" ,tld="com.br")
gtts_audio_file = f'/mnt/c/Users/Davi/Documents/ksjakd/gtts/Ad7D2pkFNdA-gtts.mp3'
tts.save(gtts_audio_file)

from IPython.display import Audio

Audio(gtts_audio_file)