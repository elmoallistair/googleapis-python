# Synthesizes speech synchronously

from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

text_file = "sample/text.txt"
with open(text_file, "r") as f:
    text = f.read()
    input_text = texttospeech.SynthesisInput(text=text)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

print("Synthesizes speech...")
response = client.synthesize_speech(
    input=input_text, 
    voice=voice, 
    audio_config=audio_config
)

output_path = "output/speech_text.mp3"
with open(output_path, "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to '{}'".format(output_path))