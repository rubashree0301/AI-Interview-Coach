from google import genai

client = genai.Client(api_key="AIzaSyCd6DEvd3SzZN7PewEtX2CicI6iyX9Wc6M")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Give one Java interview question"
)

print(response.text)
