from google.cloud import translate_v2

client = translate_v2.Client()

result = client.translate(
    values="Android is a mobile operating system",
    source_language="en",
    target_language="id"
)

print(u"Source text : {}".format(result["input"]))
print(u"Translation : {}".format(result["translatedText"]))