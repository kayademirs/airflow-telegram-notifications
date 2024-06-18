import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
title = os.getenv("TITLE")

def get_chat_id(token, title):
    # Construct the URL for the getUpdates method
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    # Define the parameters for the request
    params = {"offset": "-1", "limit": "1", "allowed_updates": ["channel_post"]}
    # Send a GET request to the Telegram API
    response = requests.get(url, params=params)
    # Parse the JSON response
    data = response.json()
    # Check if the response contains a "result" key and it's not empty
    if "result" in data and len(data["result"]) > 0:
        # Loop through each result in the response
        for result in data["result"]:
            # Check if the result contains a "channel_post" key
            # and if the "title" of the chat matches the specified title
            if "channel_post" in result and result["channel_post"]["chat"]["title"] == title:
                # Return the chat ID if a match is found
                return result["channel_post"]["chat"]["id"]
    # Return None if no matching chat is found
    return None


# Get the chat ID for the specified title
chat_id = get_chat_id(token, title)
# Print the chat ID
print(f"The ID of the chat with the title '{title}' is:", chat_id)
