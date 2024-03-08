import requests
import json
import os


def read_log(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading log: {e}"


def log_analyser_request(log_content, name_of_log="", log_type="", cert_path=""):
    api_url = os.environ.get('BBC_AI')
    if not cert_path_:
        raise ValueError("BBC AI|API URL environment variable 'BBC_AI' is not set.")

    data = {
        "inputs": f"Analyze, explain and summarise this {log_type} log, \
         the name of log is  {name_of_log}, in a concise and \
         clear way. Provide a list of potential issues and solutions. Provide a list of potential \
         issues and solutions. Provide a list of potential issues and solutions. \
         Provide a list of potential issues and solutions. Provide a list of potential issues and \
         solutions. Provide a list oflog  for potential issues:\n```{log_content}```",
        "temperature": 0.9,
        "top_p": 0.95,
        "repetition_penalty": 1.2,
        "top_k": 50,
        "truncate": 1024,
        "parameters": {"max_new_tokens": 1024}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, headers=headers, data=json.dumps(data), cert=cert_path)
    return response.json()


# Example usage
cert_path_ = os.environ.get('COSMOS_CERT')
if not cert_path_:
    raise ValueError("Certificate path environment variable 'BBC_CERT_PATH' is not set.")
log_content_ = read_log("/var/log/weekly.out")[0:1024]
response_ = log_analyser_request(
    log_content_, "weekly.out", "Apple macbook systems log weekly", cert_path_)
print(response_["generated_text"])
