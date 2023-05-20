from machinetranslation import translator
#from .translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_to_french= translator.english_to_french(textToTranslate)
    return translated_to_french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_to_english = translator.french_to_english(textToTranslate)
    return translated_to_english

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
