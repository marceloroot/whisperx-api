from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import whisperx
import torch
import os

app = FastAPI()

# Verifica se há GPU disponível
device = "cuda" if torch.cuda.is_available() else "cpu"

# Carrega o modelo WhisperX (você pode trocar por "medium", large-v2, "small"...)
model = whisperx.load_model("small", device=device)

@app.post("/transcribe")
async def transcribe_api(
    file: UploadFile = File(...),
    language: str = "en",
    diarize: bool = False,
    hf_token: str = None
):
    print(f"Recebi arquivo: {file.filename}, language: {language}, diarize: {diarize}, hf_token: {hf_token}")
    # Salva o áudio em arquivo temporário
    audio_path = f"/tmp/{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    # Carrega áudio e transcreve
    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio, batch_size=4, language=language)

    # Alinhamento de palavras
    align_model, align_metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], align_model, align_metadata, audio, device)

    # Diarização (opcional)
    if diarize:
        if not hf_token:
            return JSONResponse({"error": "hf_token required for diarization"}, status_code=400)
        diar_model = whisperx.DiarizationPipeline(use_auth_token=hf_token, device=device)
        diar_segs = diar_model(audio, min_speakers=1, max_speakers=2)
        result = whisperx.assign_word_speakers(diar_segs, result)

    # Deleta o arquivo temporário
    os.remove(audio_path)

    # Retorna resultado
    transcription_text = " ".join([seg["text"] for seg in result["segments"]])
    return JSONResponse(content={"text": transcription_text})
