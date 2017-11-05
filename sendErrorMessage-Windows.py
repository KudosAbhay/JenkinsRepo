import requests

url = "https://slack.com/api/chat.postMessage"

payload = "{\n\t\"channel\":\"#pipelineerror\",\n\t\"text\":\"Error while building pipeline\",\n\t\"as_user\":\"abhaybh\"\n}"
headers = {
    'content-type': "application/json;  charset=utf-8",
    'authorization': "Bearer xoxp-209182456768-210663224342-267245180100-8a39ac3ee6d1c417293e575417f45259"
		}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
