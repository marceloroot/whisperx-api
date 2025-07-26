# 🧠 WhisperX API com FastAPI — Guia de Instalação

Este projeto oferece uma API local para transcrição de áudios utilizando o modelo **WhisperX** da OpenAI, com suporte a **CUDA** para aceleração via GPU (NVIDIA), integração com **FastAPI**, e recursos opcionais como **diarização** de falas.

---

## ✅ Pré-requisitos

- Python 3.8 ou superior
- Placa de vídeo NVIDIA com suporte CUDA (recomendado: GTX 1060 ou superior)
- Git instalado
- Conta gratuita no site da NVIDIA (para baixar o cuDNN)

---

## 🚀 Passo a Passo de Instalação

### 🧬 Clone o repositório

```bash
git clone https://github.com/marceloroot/whisperx-api.git
cd seu-repo
```

---

### 1. 🔄 Atualize o pip

```bash
python -m pip install --upgrade pip
```

---

### 2. ⚡ Instale o PyTorch com suporte a CUDA 11.8

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

### 3. 📦 Instale as dependências principais da API

```bash
pip install whisperx fastapi uvicorn python-multipart
```

---

### 4. 🧑‍🤝‍🧑 (Opcional) Instale a biblioteca de **diarização** de áudio

```bash
pip install pyannote.audio
```

---

### 5. 🎙️ Instale o **FFmpeg** (obrigatório para processar áudios)

- **Windows:**
  1. Baixe em: https://ffmpeg.org/download.html
  2. Extraia e adicione a pasta `bin` ao **PATH** do sistema.

- **Linux (Ubuntu):**

```bash
sudo apt update
sudo apt install ffmpeg
```

---

### 6. 🧬 Instale o WhisperX diretamente do repositório oficial

```bash
pip install git+https://github.com/m-bain/whisperx.git
```

---

### 7. 🧪 Instale o projeto localmente para desenvolvimento

Se você clonou o repositório localmente, entre na pasta:

```bash
cd whisperx
pip install -e .
cd ..
```

---

### 8. ⚙️ Configure o cuDNN para compatibilidade com CUDA 11.8

#### 🔍 Verifique a versão CUDA compatível com o PyTorch  
> Neste projeto: **CUDA 11.8**

#### 🔗 Baixe o cuDNN

1. Acesse: [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)  
   (É necessário criar uma conta gratuita)

2. Vá até a seção **cuDNN Archive**:  
   🔗 https://developer.nvidia.com/rdp/cudnn-archive

3. Role até `cuDNN v8.9.4 (August 15th, 2023)`

4. Baixe:  
   `Download cuDNN v8.9.4 (local) for CUDA 11.x` →  
   **cuDNN Library for Windows (x64)**

---

#### 📁 Extraia e copie os arquivos

- Extraia o `.zip` baixado
- Copie os arquivos `.dll` (ex: `cudnn_ops_infer64_8.dll`) para:

```
C:\Program Files\NVIDIA\CUDNN\v8.9.4\bin
```
- Se tiver outra versao renomei para old
---

#### 🛠️ Adicione ao PATH do sistema

1. Pressione `Win + S` e procure por **variáveis de ambiente**  
2. Vá em:  
   `Configurações Avançadas do Sistema > Variáveis de Ambiente`
3. Em **Variáveis do sistema**, edite `Path`  
4. Clique em **Novo** e adicione:

```
C:\Program Files\NVIDIA\CUDNN\v8.9.4\bin
```

5. Clique em OK e **reinicie o computador**

✅ Certifique-se de que o arquivo `cudnn_ops_infer64_8.dll` esteja na pasta `bin` e o caminho esteja corretamente no PATH.

---

### 9. ▶️ Execute a API com Uvicorn

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Acesse a documentação interativa da API em:  
📍 http://localhost:8000/docs

---

## 🧾 Licença

Este projeto é distribuído sob a licença MIT.  
Sinta-se livre para usar, modificar e contribuir!

---

## 🧠 Créditos

- [WhisperX](https://github.com/m-bain/whisperx)
- [FastAPI](https://fastapi.tiangolo.com/)
- [cuDNN - NVIDIA](https://developer.nvidia.com/cudnn)
