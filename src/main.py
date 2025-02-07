import os
import download_audio
import transcribe_audio
import text_to_speech

# Caminhos dos arquivos
video_urls_file = "../inputs/video_urls.txt"
audio_file = "../outputs/audio/audio.mp3"
transcript_file = "../outputs/transcript/"
tts_audio_file = "../outputs/audio/gtts_audio.mp3"

# 1. Baixa o áudio
download_audio.download_audio(video_urls_file)

# 2. Transcreve e traduz
transcribe_audio.transcribe_and_audio(audio_file, transcript_file)

# 3. Converte texto em fala
text_to_speech.text_to_speech(transcript_file, tts_audio_file)

print("Processo concluído!")
