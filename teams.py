import requests
import json

url = "https://publicisgroupe.webhook.office.com/webhookb2/095cb41b-d66f-4bdc-8779-e06f9a941038@d52c9ea1-7c21-47b1-82a3-33a74b1f74b8/IncomingWebhook/7272f18db81b427fbbb5b23c4f7f6fcd/2549b88c-ac2f-47df-9fee-61609d835949"
payload = {
    "text": "Test is a test message, please ignore"
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
print(response.text.encode('utf8'))