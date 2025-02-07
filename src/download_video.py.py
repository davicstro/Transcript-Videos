# Script para baixar vídeos usando ffmpeg
# Extrair audio usando ffmpeg

import yt_dlp

video_url = 'https://www.youtube.com/watch?v=Ad7D2pkFNdA'

ydl_opts = {
    'format': 'bestaudio/best',  # Corrigido para 'bestaudio/best'
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',  # Qualidade do áudio (opcional)
    }],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'outtmpl': '%(id)s.%(ext)s',  # Corrigido para 'outtmpl'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

