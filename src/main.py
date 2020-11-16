from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException
import pyttsx3
# import PyPDF2

# book = open('book.pdf', 'rb')

def text_to_speech(text, gender):
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)
    engine.say(text)
    engine.runAndWait()


app = Flask(__name__)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def hello_world():
    return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"

@app.route('/read')
def read_pdf():
    
    text_to_speech("hello samir, how are you tonight?", "Male")
    text_to_speech("hello samir, how are you tonight?", "Female")


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)