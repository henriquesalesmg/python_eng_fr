# pylint: disable=invalid-name
'''Module translator'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-10-18',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_Text):
    '''Translate English to French'''
    french_Text = language_translator.translate(
        text = english_Text,
        model_id = 'en-fr').get_result()
    return french_Text
    #print(json.dumps(french_Text, indent=2))

def frenchToEnglish(french_Text):
    '''Translate French to English'''
    english_Text = language_translator.translate(
        text = french_Text,
        model_id = 'fr-en').get_result()
    return english_Text
    #print(json.dumps(english_Text, indent=2))
