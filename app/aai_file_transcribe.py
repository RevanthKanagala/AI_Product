# app/aai_file_transcribe.py
import os
import assemblyai as aai

# Read key from env var set with `setx ASSEMBLYAI_API_KEY "..."` (Windows)
api_key = os.getenv("ASSEMBLYAI_API_KEY")
if not api_key:
    raise SystemExit("ASSEMBLYAI_API_KEY not set. Close & reopen terminal, or set it and retry.")

aai.settings.api_key = api_key

# Create a transcriber and run a single-file transcription
transcriber = aai.Transcriber()
audio_path = r"D:\AIDI\AI_Product\anji2"   # <-- replace with your file path
transcript = transcriber.transcribe(audio_path)

# Basic error handling & output
if transcript.error:
    print("Transcription failed:", transcript.error)
else:
    print("--- TRANSCRIPT ---")
    print(transcript.text)
