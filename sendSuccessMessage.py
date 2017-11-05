import requests

url = "https://slack.com/api/chat.postMessage"

payload = "{\n\t\"channel\":\"#pipelinesuccess\",\n\t\"text\":\"Successfully built your pipeline\",\n\t\"as_user\":\"abhaybh\"\n}"
headers = {
    'content-type': "application/json;  charset=utf-8",
    'authorization': "Bearer xoxp-209182456768-210663224342-267231979220-f6d1016c831b42f80f253309f3db0ad4"
		}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
