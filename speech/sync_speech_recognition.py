# Import libraries
from google.cloud import speech
import io
import os

# Instantiates a client
client = speech.SpeechClient()

# Loads audio from uri
# source_audio = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
# audio = speech.RecognitionAudio(uri=source_audio)

# Loads audio from local
source_audio = "path/to/audio"
with io.open(source_audio, "rb") as audio_file:
        content = audio_file.read()
audio = speech.RecognitionAudio(content=content)

# Provides information to the recognizer
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Perform synchronous speech recognition
print("Transcribing audio from {}...\n".format(os.path.basename(source_audio)))
response = client.recognize(config=config, audio=audio)

# Display the results
print("Result:")
for result in response.results:
    print("{} (confidence: {:.2f})".format(
        result.alternatives[0].transcript, result.alternatives[0].confidence))
