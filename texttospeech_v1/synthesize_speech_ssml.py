# Synthesizes speech synchronously

from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

ssml_file = "sample/text.ssml"
with open(ssml_file, "r") as f:
    ssml = f.read()
    input_text = texttospeech.SynthesisInput(ssml=ssml)

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

output_path = "output/speech_ssml.mp3"
with open(output_path, "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to '{}'".format(output_path))