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
- [x] Test with BBC endpoint, see https://llama-2-13b-chat.automation.bbctest01.uk/
- Use a local AI API if possible 
```shell
pip install git+https://github.com/bbc/text-generation-inference.git@add-cert-to-client#subdirectory=clients/python
```
- [x] Ensure sensitive data in logs is handled securely.
- [x] Consider privacy implications of sending data to an external API.  Use a local AI API if possible.

## Error Handling:
- [x] Implement robust error handling for file access, API communication, and data processing.


# Initial Examples
## OPENAI for Apple macbook logs, no Workplace information
```
% python log_analyser_openai.py
This provided log, named `weekly.out`, appears to be a system log for an Apple MacBook that records timestamped entries over a span of time from February 25, 2023, to January 19, 2024. The log presumably indicates the times when certain events occurred, perhaps automated system checks, maintenance tasks, or backups.

Key Observations from the Log Data:

1. **Routine Schedule**: Initially, the timestamps do not follow a strict weekly pattern, but eventually, they seem to stabilize on Tuesdays and Fridays.
   
2. **Time Zone and Daylight Saving Time**:
   - The timestamps shift from GMT (Greenwich Mean Time) to BST (British Summer Time) between March 29 and October 30, indicating daylight saving time adjustments.
   - This is reversed at the end of October when the timestamps revert to GMT.

3. **Variation in Execution Time**:
   - The times of log entries vary, but typically they are in the morning hours. There are a few notable exceptions where the system log captures events in the afternoon or evening.
   - This could suggest either different schedule times for different tasks or delayed execution due to system activity or issues.

Potential Issues Based on Observations:

1. **Inconsistent Schedule**: The inconsistencies in the early part of the log entries could indicate issues with the scheduling system or manual interventions.
   
2. **Time Zone Changes**: Automated tasks may run at unexpected local times due to the shifts between GMT and BST without proper adjustment for daylight saving changes.
   
3. **Delayed Tasks**: Entries that are significantly later than the usual times may signify system overloads, performance issues, or conflicts with other processes.

Potential Solutions for the Issues:

1. **Consistency in Scheduling**:
   - Review the scheduling system for automated tasks to ensure consistency.
   - If manual intervention is causing inconsistencies, reassess whether the task should be automated or assign clear protocols for manual runs.

2. **Time Zone Management**:
   - Implement daylight saving aware scheduling, ensuring that any system tasks that should run at specific local times adjust automatically.
   - Verify that time zone settings are correctly configured on the system.

3. **System Performance**:
   - Investigate any delayed tasks to find out why they did not run at their expected time.
   - Monitor system resources to ensure that the hardware can handle the scheduled tasks without significant delays. Consider upgrading system resources if they are found to be lacking.
   - Identify if other simultaneous processes are causing resource contention and adjust schedules or system priorities accordingly.

4. **Maintenance and Updates**:
   - Keep the operating system and all relevant software up to date to prevent bugs that could affect scheduling.
   - Perform regular system health checks and maintenance to avoid performance degradation over time.

As this analysis is based solely on the timestamps from the `weekly.out` log, for a comprehensive diagnostics report, the actual event messages and error logs (if any) would need to be reviewed to pinpoint the causes behind the given observations and implement the specific solutions accordingly.
```