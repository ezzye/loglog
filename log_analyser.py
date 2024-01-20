import requests
import json
import os


def log_analyser(input_text, cert_path):
    api_url = os.environ.get('BBC_AI')
    if not cert_path_:
        raise ValueError("BBC AI|API URL environment variable 'BBC_AI' is not set.")

    data = {
        "inputs": input_text,
        "parameters": {"max_new_tokens": 170}
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(api_url, headers=headers, data=json.dumps(data), cert=cert_path)
    return response.json()


# Example usage
cert_path_ = os.environ.get('COSMOS_CERT')
if not cert_path_:
    raise ValueError("Certificate path environment variable 'BBC_CERT_PATH' is not set.")

response_ = log_analyser("How is the BBC funded?", cert_path_)
print(response_)
