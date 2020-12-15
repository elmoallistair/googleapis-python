# Import libraries
from google.cloud import speech_v1p1beta1 as speech

# Instantiates a client
client = speech.SpeechClient()

# Loads audio from uri
# source_audio = "gs://cloud-samples-tests/speech/commercial_mono.wav"
# audio = speech.RecognitionAudio(uri=source_audio)

# Loads audio from local
speech_file = "res/commercial_mono.wav"
with open(speech_file, "rb") as audio_file:
    content = audio_file.read()
audio = speech.RecognitionAudio(content=content)

# Provides information to the recognizer
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code="en-US",
    enable_speaker_diarization=True,
    diarization_speaker_count=2,
)

# Perform speech recognition
print("Recognizing speakers...\n")
response = client.recognize(config=config, audio=audio)
result = response.results[-1]
words = result.alternatives[0].words

# Display the results
for word in words:
    print(u"Speaker {}: '{}'".format(word.speaker_tag, word.word))