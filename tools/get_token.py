
import requests
import webbrowser
import urllib.parse
import json
from dotenv import load_dotenv
import os

# Spotify-App-Daten aus .env laden
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = os.getenv("SCOPE")
path = os.getenv("TOKEN_PATH")

# Schritt 3: Access Token abrufen
token_url = 'https://accounts.spotify.com/api/token'

def get_tokens():
    #Schritt 1: Nutzer zur Autorisierung öffnen
    auth_url = (
        'https://accounts.spotify.com/authorize?' +
        urllib.parse.urlencode({
            'client_id': client_id,
            'response_type': 'code',
            'redirect_uri': redirect_uri,
            'scope': scope
        })
    )

    print('Öffne diesen Link im Browser, logge dich ein und kopiere den Code aus der URL:')
    print(auth_url)
    webbrowser.open(auth_url)

    # Schritt 2: Nutzer gibt den Code ein
    auth_code = input('Code aus URL hier einfügen: ')

    data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
}
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens['access_token']
        refresh_token = tokens['refresh_token']
        print('Access Token:', access_token)
        print("Refresh_token:", refresh_token)
        respons_data = {
            "refresh_token": refresh_token,
            "auth_token": access_token,
    }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(respons_data, f, indent=4, ensure_ascii=False)


    else:
        print('Fehler beim Token-Abruf:', response.status_code, response.text)

def refresh_token():
    try:
        with open(path, "r", encoding="utf-8") as f:
            data_out = json.load(f)
            refreshToken = data_out.get("refresh_token")
        print("Refreshed Token")
    except (FileNotFoundError, json.JSONDecodeError):
        print("erro")

    data = {
    'grant_type': 'refresh_token',
    'refresh_token': refreshToken,
    }
    # BQCebP1IaeYHEfFIzMSMQpE98NG7m4B0Rqw7IftbJtxDfDJ9W2lDd4jeFE9TJfN4fymtTjvdYa64gMm-oAVg-4pZJamkYkggSzw3RCSc82NRO8V18BkfAeAYarZFLhTKSl7WLddPp_It2AwwJQYUttnFUMGpTpk8QHjQIwMQjjPOWOqNj9WYdishI0yFp4rWwzSMrv2qi_R8Kq0hty2dfEG2hydk9HtaGK8KLV9v62AwBfd6fxeCEuk
    # 
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens['access_token']
        refresh_token = tokens['refresh_token']
        print('Access Token:', access_token)
        print("Refresh_token:", refresh_token)
        respons_data = {
            "refresh_token": refresh_token,
            "auth_token": access_token,
    }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(respons_data, f, indent=4, ensure_ascii=False)
# ...existing code...

def refresh_access_token():
    try:
        with open(path, "r", encoding="utf-8") as f:
            data_out = json.load(f)
            refreshToken = data_out.get("refresh_token")
        print("Refreshed Token")
    except (FileNotFoundError, json.JSONDecodeError):
        print("erro")
        return

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refreshToken,
        'client_id': client_id,
        'client_secret': client_secret
    }
    
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens['access_token']
        refresh_token_new = tokens.get('refresh_token', refreshToken)
        print('Access Token:', access_token)
        print("Refresh_token:", refresh_token_new)
        respons_data = {
            "refresh_token": refresh_token_new,
            "auth_token": access_token,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(respons_data, f, indent=4, ensure_ascii=False)
    else:
        print('Fehler beim Token-Refresh:', response.status_code, response.text)

refresh_access_token()
