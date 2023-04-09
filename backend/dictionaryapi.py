import requests.api as api
import urllib.parse

INVALID_MESSAGE = "No Definitions Found"

def fetch_word(word : str):
    if not word:
        return INVALID_MESSAGE
    
    # Finding word info with api call
    word = urllib.parse.quote(word)
    payload = api.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    data = payload.json()

    if type(data) == dict and data["title"] == INVALID_MESSAGE:
        return INVALID_MESSAGE

    return data
