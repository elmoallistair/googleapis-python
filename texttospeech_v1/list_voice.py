# List of voices supported for synthesis

from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

voices = client.list_voices()

for voice in voices.voices:
    print("Voice name    : {}".format(voice.name))
    print("SSML Gender   : {}".format("MALE" if voice.ssml_gender == 1 else "FEMALE"))
    print("Language code : {}\n".format(voice.language_codes))
