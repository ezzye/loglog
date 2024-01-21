from text_generation import Client
import os


def read_log(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading log: {e}"


def call_bbc_api(log_content, name_of_log="", log_type=""):
    # Get the certificate path from an environment variable
    cert_path = os.environ.get('COSMOS_CERT')
    if not cert_path:
        raise ValueError("Certificate path environment variable 'BBC_CERT_PATH' is not set.")

    # Create a client instance
    client = Client(
        "https://llama-2-13b-chat.automation.bbctest01.uk/",
        cert=cert_path
    )

    # Generate text using the BBC API
    prompt = f"Analyze, explain and summarise this {log_type} log, \
         the name of log is  {name_of_log}, in a concise and \
         clear way. Provide a list of potential issues and solutions. Provide a list of potential \
         issues and solutions. Provide a list of potential issues and solutions. \
         Provide a list of potential issues and solutions. Provide a list of potential issues and \
         solutions. Provide a list oflog  for potential issues:\n{log_content}"
    response = client.generate(prompt, max_new_tokens=170)
    return response.generated_text


# Example usage
try:
    log_content_ = read_log("/var/log/weekly.out")
    generated_text = call_bbc_api(log_content_, "weekly.out", "Apple macbook systems log weekly")
    print(generated_text)
except Exception as e:
    print(f"An error occurred: {e}")
