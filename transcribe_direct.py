import whisper
import sys
import os

if len(sys.argv) < 2:
    print("Veuillez fournir le chemin vers le fichier audio.")
    sys.exit(1)

chemin_fichier = sys.argv[1]

# Vérifie si le fichier existe
if not os.path.exists(chemin_fichier):
    print("Le fichier audio spécifié n'existe pas.")
    sys.exit(1)

# Charge le modèle Whisper
model = whisper.load_model("base")
print("Modèle chargé avec succès.")

# Charge le fichier audio
audio_data = whisper.load_audio(chemin_fichier)
print("Audio chargé avec succès.")

# Essaie de transcrire le fichier audio
try:
    transcription = model.transcribe(audio_data, language="english")
    print("Transcription réussie !")
    print(transcription["text"])
except Exception as e:
    print(f"Erreur lors de la transcription : {str(e)}")
