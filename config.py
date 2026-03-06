import google.generativeai as genai

genai.configure(api_key="AIzaSyCd6DEvd3SzZN7PewEtX2CicI6iyX9Wc6M")

model = genai.GenerativeModel("gemini-pro")
