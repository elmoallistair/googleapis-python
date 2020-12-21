from google.cloud import translate_v2

client = translate_v2.Client()

result = client.get_languages(
    # target_language="en"
)

print("Supported languages:")
for language in result:
    print("{name} ({language})".format(**language))