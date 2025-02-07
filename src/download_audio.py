import yt_dlp

def download_audio(video_url_file):
    # Abre o arquivo e lê todas as URLs
    with open(video_url_file, "r") as file:
        video_urls = [line.strip() for line in file.readlines() if line.strip()]  # Remove linhas vazias

    if not video_urls:
        print("Erro: Nenhuma URL encontrada no arquivo.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'outputs/%(id)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_urls)  # Passando a lista de URLs corretamente

if __name__ == "__main__":
    download_audio("../inputs/video_urls.txt")
