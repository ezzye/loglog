import openai
from pathlib import Path


class LogAnalyser:
    def __init__(self, api_key):
        self.api_key = api_key

    def read_log(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            return f"Error reading log: {e}"

    def analyze_log(self, log_content):
        try:
            openai.api_key = self.api_key
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Analyze and summarize this log for potential issues:\n{log_content}",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error analyzing log: {e}"


# Example usage
api_key = "your-api-key"
analyzer = LogAnalyser(api_key)
log_content_ = analyzer.read_log("/var/log/example.log")
analysis = analyzer.analyze_log(log_content_)
print(analysis)
