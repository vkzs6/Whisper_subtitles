# 🎬 Legendador Automático de Vídeos com Whisper + Flask

Um sistema web simples e elegante para gerar legendas automáticas em vídeos `.mp4` enviando pelo navegador, usando [OpenAI Whisper](https://github.com/openai/whisper), [ffmpeg](https://ffmpeg.org/), e [Flask](https://flask.palletsprojects.com/). O vídeo já sai legendado e pronto para baixar ou assistir online na mesma página!

---

## 🚀 Funcionalidades

- Upload de vídeos `.mp4` pela interface web.
- Geração automática das legendas com Whisper.
- Legenda embutida diretamente no vídeo (áudio e vídeo preservados).
- Player web para assistir o resultado imediatamente.
- Download do vídeo legendado.
- Interface moderna e responsiva.

---

## 🖥️ Requisitos

- Python 3.8+
- ffmpeg instalado no sistema (e disponível no PATH)
- Pip (gerenciador de pacotes Python)

---

## ⚙️ Instalação

Clone este repositório e acesse a pasta do projeto:


git clone https://github.com/vkzs6/Whisper_subtitles.git
cd seuprojeto

text

Crie um ambiente virtual e ative:

python -m venv venv

Ative no Windows:
venv\Scripts\activate

Ou Linux/Mac:
source venv/bin/activate

text

Instale as dependências:

pip install flask openai-whisper ffmpeg-python

text

Certifique-se de que o ffmpeg está instalado e disponível no path (você pode baixar de https://ffmpeg.org/).

---

## ▶️ Como executar

1. Rode o servidor Flask:
    ```
    python app.py
    ```

2. Abra o navegador em:
    ```
    http://127.0.0.1:5000
    ```

3. Envie um vídeo `.mp4` (quanto menor, mais rápido o processo).

4. Aguarde o processamento. Você poderá:
    - Assistir o vídeo legendado direto no browser.
    - Baixar o arquivo legendado.

---

## 🧠 Como funciona?

O fluxo é:

1. O usuário envia um .mp4 pelo navegador.
2. O Whisper transcreve o áudio para gerar o `.srt`.
3. O ffmpeg embute a legenda no vídeo, gerando um novo arquivo `.mp4`.
4. O resultado pode ser visto e baixado na web.

---

## ❗ Observações

- O processamento é pesado: prefira vídeos curtos para demonstração local.
- Não deixe o Flask "dev server" aberto em ambientes públicos.
- Utilize um WSGI (gunicorn, waitress) e reverso para servidores de produção.
- Ajuste limites de upload conforme necessidade.

---

## 📃 Licença

MIT - Sinta-se à vontade para usar e modificar!

---

Feito com 💙 por [vksz6](https://github.com/vkzs6)