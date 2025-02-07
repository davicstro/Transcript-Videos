# Transcript-Videos

Este repositório contém um script Python para baixar áudio de vídeos do YouTube e gerar transcrições a partir do áudio. Ele utiliza a biblioteca `yt-dlp` para baixar o áudio e outras ferramentas para processar e transcrever o conteúdo.

## Funcionalidades

- **Download de Áudio**: Baixa o áudio de vídeos do YouTube em formato MP3.
- **Transcrição de Áudio**: Converte o áudio baixado em texto (transcrição).
- **Organização de Arquivos**: Salva os arquivos de áudio e transcrição em pastas específicas.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Biblioteca `yt-dlp` (para download de vídeos/áudio do YouTube)
- Biblioteca `pytube` (opcional, para manipulação de URLs do YouTube)
- FFmpeg (para conversão de formatos de áudio)

### Instalação das Dependências

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/Transcript-Videos.git
   cd Transcript-Videos