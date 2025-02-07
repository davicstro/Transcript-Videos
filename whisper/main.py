import whisper

# Carrega o modelo Whisper
model = whisper.load_model("base")

# Transcreve e traduz o áudio para português
result = model.transcribe("/mnt/c/Users/Davi/Documents/ksjakd/transcript/Ad7D2pkFNdA.mp3", language='en', task='translate')
print(f'Translation to Portuguese: \n{result["text"]}')

# Salva o texto traduzido em um arquivo
with open('Ad7D2pkFNdA-base.txt', "w") as result_text_file:
    text = result["text"].split('.')
    for sentence in text:
        sentence = sentence.strip()  # Remove espaços extras
        if sentence:  # Evita escrever linhas vazias
            result_text_file.write(sentence)
            result_text_file.write('\n')
