import requests
import random
import json
import time
import os
fileURL = "https://verumignis.com/spam.json"
while True:
    try:
        url = input("Enter the webhook URL: ")
        print("Checking webhook...")
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if all(key in data for key in ("type", "id", "name", "avatar", "channel_id", "guild_id", "application_id", "token")):
                print("Valid webhook")
                break
            else:
                print("Invalid webhook")
        else:
            print("Invalid webhook")
    except:
        print("Invalid webhook")
print(f"Downloading spam message file from {fileURL}")
try:
    response = requests.get(fileURL)
    messages = response.json()
    print("Downloaded successfully")
except:
    print("Could not get message file")
    raise BaseException(f"Unable to GET {fileURL}")

print("Spam starting...")
previousMessage = None
x = 0
while True:
    message = previousMessage
    while message == previousMessage:
        message = random.choice(messages)
    previousMessage = message
    image = message['image']
    username = message['username']
    avatar = message['avatar']
    title = message['title']
    text = message['text']
    outJSON = {
        "content": "@everyone",
        "embeds": [{
            "title": title,
            "image": {
                "url": f"{image}"
            },
            "description": text,
            "footer": {
                "text": "Oopsies, shouldn't have spread that malware!"
            }
        }],
        "username": username,
        "avatar_url": avatar
    }
    response = requests.post(url, json=outJSON, headers={"Content-Type": "application/json"})
    if response.status_code == 204:
        x = x+1
        print(f"Spammed successfully {x} time(s)")
    else:
        print("Failed to spam webhook, maybe it got deleted?")
    time.sleep(5)
