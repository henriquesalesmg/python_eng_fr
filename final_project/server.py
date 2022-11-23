from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_To_French():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.englishToFrench(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def french_To_English():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.frenchToEnglish(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    return render_template ('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
