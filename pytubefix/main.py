from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

# Solicita a URL do usuário
url = input("Digite a URL do vídeo: ").strip()

# Define o diretório de destino e cria se não existir
destino = "video"
os.makedirs(destino, exist_ok=True)

try:
    # Cria o objeto YouTube com callback de progresso
    yt = YouTube(url, on_progress_callback=on_progress)
    
    # Exibe o título do vídeo
    print(f"Baixando: {yt.title}")

    # Obtém a melhor resolução disponível e faz o download
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=destino)

    print("Download concluído!")

except Exception as e:
    print(f"Erro ao baixar o vídeo: {e}")
