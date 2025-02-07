from gtts import gTTS

#Ler texto do arquivo
with open(f'../outputs/transcript/Ad7D2pkFNdA.txt', "r", encoding="utf-8") as text_file:
    transcription = text_file.read()
#print(audio_transcription)

tts = gTTS(transcription, lang ="pt" ,tld="com.br")
gtts_audio_file = f'../outputs/audio/Ad7D2pkFNdA_translated.mp3'
tts.save(gtts_audio_file)

from IPython.display import Audio

Audio(gtts_audio_file)