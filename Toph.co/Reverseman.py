apikey="ZGpOQRCTTRBBpEcnplx7gN_9MfEvfddSpzngykmZ"
Accountid="0ddd9358ccb8fd61c7f19b3ded0395ef" 
from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

CLOUDFLARE_ACCOUNT_ID = Accountid
CLOUDFLARE_API_TOKEN = apikey

def run_ai_model(prompt):
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/lykon/dreamshaper-8-lcm"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.content

@app.route('/fetch', methods=['GET'])
async def fetch():
    prompt = "cyberpunk cat"
    image_data = run_ai_model(prompt)
    return Response(image_data, content_type='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
