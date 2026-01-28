import requests
import json
import time
import threading
import sys
import urllib.parse
from dotenv import load_dotenv
import os

sys.path.append(r"E:\Jarvis\tools")
from get_token import refresh_access_token

load_dotenv()  # Lädt die .env-Datei automatisch

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = os.getenv("SCOPE")
user_id = os.getenv("USER_ID")
path = os.getenv("TOKEN_PATH")

base_url = "https://api.spotify.com/v1"

def load_token():
    with open(r"E:\Spotify-wrapper\json\token.json", "r", encoding="utf-8") as f:
        data_out = json.load(f)
        return data_out.get("auth_token")

def refresh_token_loop():
    while True:
        refresh_access_token()
        time.sleep(3500)


def skip(base_url, headers):
    url = base_url+"/me/player/next"
    response = requests.post(url=url, headers=headers,)
    print(f"Status: {response.status_code};   {response.text}")

def skip_back(base_url, headers):
    url = base_url+"/me/player/previous"
    response = requests.post(url=url, headers=headers)
    print(f"Status: {response.status_code};   {response.text}")

def pause(base_url, headers):
    url = base_url+"/me/player/pause"
    response = requests.put(url=url, headers=headers)
    print(f"Status: {response.status_code};   {response.text}")

def unpause(base_url, headers):
    url = base_url+"/me/player/play"
    response = requests.put(url=url, headers=headers)
    print(f"Status: {response.status_code};   {response.text}")

def play_playlist(base_url, headers, playlist_uri):
    url = base_url+"/me/player/play"
    data = {
    "context_uri": f"spotify:playlist:{playlist_uri}",
    }
    response = requests.put(url=url, headers=headers, data=data)
    print(f"Status: {response.status_code};   {response.text}")

def get_devices(base_url, headers):
    url= f"{base_url}/me/player/devices"
    respons = requests.get(url, headers)
    

def get_devices(base_url, headers):
    url  = f"{base_url}/me"

# Muss noch gemacht werden ist um playlists ab zu rufen
# def name_to_uri(name):
#     print()

# def get_playlist_list():
#     url = base_url+"/me/playlists?limit=50"
#     response = requests.get(url, headers)
#     data = response.json()

#     # Nach deiner Vorlage transformieren
#     filtered = {
#         "posts": [
#             {"nummer": item["id"], "überschrift": item["title"]}
#             for item in data
#         ]
#     }

#     # In Datei speichern
#     with open("output.json", "w", encoding="utf-8") as f:
#         json.dump(filtered, f, indent=4, ensure_ascii=False)

        # mögliche felders


def search(type=str, ):
    
    query = " ".join(parts)
    query 
    spotifiy_query = urllib.parse.quote(query)   
    if __name__ == "__main__":
        raw, enc = spotifiy_query
        URL = f"https: //api.spotify.com/v1/search/{enc}"


def command_loop():
    while True:
        auth_token = load_token()
        headers = { "Authorization": f"Bearer {auth_token}" }
        command = input("Aufgabe: ")
        if command == "skip":
            skip(base_url, headers)
        if command == "skip back":
            skip_back(base_url, headers)
        if command == "pause":
            pause(base_url, headers)
        if command == "unpause":
            unpause(base_url, headers)

threading.Thread(target=refresh_token_loop, daemon=True).start()
command_loop()


