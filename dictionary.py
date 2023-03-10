import requests.api as api

INVALID_MESSAGE = "Page or revision not found."

def fetch_word(word : str):
    if not word:
        return INVALID_MESSAGE
    
    # Finding word info with api call
    payload = api.get("https://en.wiktionary.org/api/rest_v1/page/definition/" + word)
    data = payload.json()
    print(data)

    if "detail" in data and data["detail"] == INVALID_MESSAGE:
        return INVALID_MESSAGE

    return data["en"] # TODO - Let user choose language
