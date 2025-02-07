import whisper
import os

# Carrega o modelo Whisper
model = whisper.load_model("base")

# Diretórios de entrada e saída
input_dir = "../outputs/audio/"
output_dir = "../outputs/transcript/"

# Garante que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Lista todos os arquivos de áudio no diretório
audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]

for audio_file in audio_files:
    audio_path = os.path.join(input_dir, audio_file)

    print(f"Transcrevendo {audio_file}...")

    # Transcreve e traduz o áudio para português
    result = model.transcribe(audio_path, language='en')

    # Nome do arquivo de saída
    output_file = os.path.join(output_dir, f"{os.path.splitext(audio_file)[0]}.txt")
    

    # Salva o texto traduzido
    with open(output_file, "w", encoding="utf-8") as result_text_file:
        result_text_file.write(result["text"] + "\n")

    print(f"Transcrição salva em: {output_file}")

print("Processo concluído!")
