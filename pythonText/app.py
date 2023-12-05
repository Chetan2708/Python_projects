from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import fitz  
from pathlib import Path
from openai import OpenAI
import re

client = OpenAI()
app = Flask(__name__)


# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "C:/Users/Chetan Gupta/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"



@app.route('/')
def hello():
    return 'hello world'
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_number in range(doc.page_count):
            page = doc.load_page(page_number)
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_text_from_file(file_path):
    file_extension = Path(file_path).suffix.lower()
    if file_extension in ['.png', '.jpg', '.jpeg']:
        return extract_text_from_image(file_path)
    elif file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return None

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    try:
        # Get the file path from the request
        file_path = request.json['file_path']

        # Extract text from the file
        extracted_text = extract_text_from_file(file_path)

        # Create a chat completion
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You have to extract what is the name of the course and organization in the certificate data provided."},
                {"role": "user", "content": extracted_text}
            ]
        )

        # Extract information from the generated completion
        generated_text = completion.choices[0].message 
        
        return jsonify(str(generated_text))

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5002)





