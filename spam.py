import requests
import random
import json
import time

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

print("Spam starting...")

previous_message = None
x = 0

while True:
    message = previous_message
    while message == previous_message:
        message = random.choice(messages)
    previous_message = message

    image = message['image']
    username = message['username']
    avatar = message['avatar']
    title = message['title']
    text = message['text']

    payload = {
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

    # Send the POST request to the webhook
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
    if response.status_code == 204:
        x = x+1
        print(f"Spammed successfully {x} time(s)")
    else:
        print("Failed to spam webhook, maybe it got deleted?")

    # Sleep for 1 second to avoid hitting Discord's rate limits
    time.sleep(5)
