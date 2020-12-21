from google.cloud import translate_v2

client = translate_v2.Client()

result = client.detect_language(
    values="Android is a mobile operating system"
)

print("Source text : {}".format(result["input"]))
print("Language code : {}".format(result["language"]))
print("Confidence : {}".format(result["confidence"]))
