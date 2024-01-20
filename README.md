![Loglog App Logo](logo_resized.png)

Loglog, quickly and easily troubleshoot all your logs at the same time.

An innovation 10% time project.

# AIM
There are many problems in software engineering.  

One problem is understanding the logs on an AWS EC2 when troubleshooting.  

An important part of this is reading and understanding logs on an EC2, not just application logs from `/var/log/` 
but also `messages` and `journalctl` and other normal logs.  

A LLM can read interpret and summarise logs to help with troubleshooting.  

Currently engineers use `grep`, `cat`, `tail` and `less` to read and analyse logs when troubleshooting.  

These tools are included in a normal build of linux.  

However, an AI via an AI API endpoint could read, analyse and troubleshoot logs if we had an application that could read
logs and upload them to an AI API endpoint with appropriate prompt and output relevant troubleshooting notes and 
analysis of each log.  

To achieve this we aim to write a simple python script using latest lang chain library to do this.  

We aim to include unit tests.


# TODO
- [x] Create a python script that can read a log file and upload it to an AI API endpoint

## Define Requirements:
- [x] Read logs from various locations (/var/log/, messages, journalctl, etc.) on an AWS EC2 instance.
- [x] Summarize and analyze these logs.
- [x] Communicate with an AI API (like OpenAI's GPT or BBC AI) to process log data.

## Design Approach:
- [x] Develop a Python script to automate log reading.
- [x] Use OpenAI's Python client library to send log excerpts to GPT-4 for analysis. May have to use a different AI API.
- [x] Parse the AI's response for troubleshooting insights.

## Components:
- [x] Log Reader: Module to access and read log files.
- [x] AI Communication: Module to interact with the AI API.
- [x] Log Analyzer: Core logic to handle the summarization and analysis process.
- [x] Unit Tests: To ensure each component works as expected.

## Security & Privacy:
- [x] Ensure sensitive data in logs is handled securely.
- [x] Consider privacy implications of sending data to an external API.  Use a local AI API if possible.

## Error Handling:
- [x] Implement robust error handling for file access, API communication, and data processing.
