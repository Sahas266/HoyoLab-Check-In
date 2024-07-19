##########################################################################
########## Modify Profiles and Discord Information as Necessary ##########
##########################################################################

# Use directions in README to find ltoken_v2 and ltuid_v2 values
profiles = [
    {
        "token": "ltoken_v2=gBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxCY; ltuid_v2=26XXXXX20;",
        "genshin": False,
        "honkai_star_rail": False,
        "honkai_3": False,
        "tears_of_themis": False,
        "zenless_zone_zero": False,
        "accountName": ""
    }
]

# Use directions in README to find Discord ID and create a webhook
myDiscordID = ""
discordWebhook = ""


##########################################################################################################################
################################################## BELOW IS SCRIPT CODE ##################################################
##################################################    DO NOT MODIFY     ##################################################
##########################################################################################################################

import requests
import json
import time
import asyncio

urlDict = {
    "Genshin": "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id=e202102251931481",
    "Star_Rail": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202303301540311",
    "Honkai_3": "https://sg-public-api.hoyolab.com/event/mani/sign?lang=en-us&act_id=e202110291205111",
    "Tears_of_Themis": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202308141137581",
    "Zenless_Zone_Zero": "https://sg-act-nap-api.hoyolab.com/event/luna/zzz/os/sign?lang=en-us&act_id=e202406031448091"
}

def post_webhook(data):
    
    payload = {
        "username": "HoyoLab Check-In",
        "avatar_url": "https://1000logos.net/wp-content/uploads/2023/02/HoYoverse-Emblem.png",
        "content": (f"<@{myDiscordID}> " if myDiscordID else "") + "\n" + data
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(discordWebhook, headers=headers, data=json.dumps(payload))
    
    if (response.status_code != 200) and (response.status_code != 204):
        print(f"Failed to post webhook: {response.status_code}")
        print(response.text)

def auto_sign_function(profile):
    
    response = f"Check-in response for {profile["accountName"]}: \n"

    urls = []

    if profile.get("genshin"):
        urls.append(urlDict["Genshin"])
    if profile.get("honkai_star_rail"):
        urls.append(urlDict["Star_Rail"])
    if profile.get("honkai_3"):
        urls.append(urlDict["Honkai_3"])
    if profile.get("tears_of_themis"):
        urls.append(urlDict["Tears_of_Themis"])
    if profile.get("zenless_zone_zero"):
        urls.append(urlDict["Zenless_Zone_Zero"])

    headers = {
        "Cookie": profile["token"],
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "x-rpc-app_version": "2.34.1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-rpc-client_type": "4",
        "Referer": "https://act.hoyolab.com/",
        "Origin": "https://act.hoyolab.com"
    }

    sleep_time = 0

    http_responses = []
    for url in urls:
        time.sleep(sleep_time / 1000)
        http_response = requests.post(url, headers=headers)
        http_responses.append(http_response)
        sleep_time = 1000

    for i, hoyolab_response in enumerate(http_responses):
        response_json = hoyolab_response.json()
        response += (response_json.get("message") + "\n")

    return response

async def main():

    for profile in profiles:
         post_webhook(auto_sign_function(profile))
    post_webhook("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")


asyncio.run(main())