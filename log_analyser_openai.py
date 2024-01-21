from openai import OpenAI
from openai import AsyncOpenAI
from pathlib import Path
import os

client = OpenAI(
    api_key=os.environ['OPENAIKEY'],
)


class LogAnalyser:

    def read_log(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            return f"Error reading log: {e}"

    def analyze_log(self, log_content, name_of_log="", log_type=""):

        try:
            completion = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {
                        "role": "user",
                        "content": f"Analyze, explain and summarise this {log_type} log, \
                         the name of log is  {name_of_log}, in a concise and \
                         clear way. Provide a list of potential issues and solutions. Provide a list of potential \
                         issues and solutions. Provide a list of potential issues and solutions. \
                         Provide a list of potential issues and solutions. Provide a list of potential issues and \
                         solutions. Provide a list oflog  for potential issues:\n{log_content}",
                    },
                ],
            )
            response = completion.choices[0].message.content
            return response
        except Exception as e:
            return f"Error analyzing log: {e}"


# Example usage (using non BBC data on non BBC systems)
analyzes = LogAnalyser()
log_content_ = analyzes.read_log("/var/log/weekly.out")
analysis = analyzes.analyze_log(log_content_, "weekly.out", "Apple macbook systems log weekly")
print(analysis)
