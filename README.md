# <p align="center">webhookSpammer</p>

---

webhookSpammer allows you to easily nuke webhooks used by script kiddies or malware developers. Heres how to use it:

---

## Installation

### To install webhookSpammer you will need:

1. Python: https://www.python.org/downloads/
2. Requests: With python installed run the command `pip install requests` in command prompt.
3. webhookSpammer.py: Download from this repo.

## Usage

To use webhookSpammer you will need a target URL. This will be found in the malware you are trying to nuke. If the malware is a .jar file and it is not obfuscated you can use JD-GUI to decompile the .jar and retreive the webhook URL.
Once you have the target URL you can run webhookSpammer.py by following these steps:

1. Navigate to the folder webhookSpammer.py is located in.
2. Right click some empty space in file explorer and select `open in terminal`
3. In the terminal type `python webhookSpammer.py`
4. When it prompts you for a webhook URL paste in the URL you retrieved from the malware. It will then download the message list and start spamming.
5. Sit back and enjoy as the webhook URL gets spammed with random messages from a list (if you have any funny messages you want me to add DM me on verumIgnis#1564)
