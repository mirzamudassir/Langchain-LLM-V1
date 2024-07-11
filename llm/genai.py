import google.generativeai as genai
import os
from dotenv import load_dotenv

#load vars
load_dotenv()

api_key=os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("The opposite of hot is")
print(response.text)