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
- [x] Log Analyzer: Core logic to handle the summarisation and analysis process.
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


# Development Plan

To create a CLI (Command-Line Interface) tool for analyzing and summarizing actionable issues in large Linux application logs using Microsoft Autogen 2 for automation and the Meta LLaMA 2 LLM for analysis, you're facing two primary challenges: handling the small context window of LLaMA 2 and prompting the AI effectively to analyze and spot issues while minimizing false positives. Here's a plan to address these challenges:

### 1. **Preprocessing Large Logs**

Given the small context window of LLaMA 2, preprocessing the log files to break them down into manageable chunks is crucial. This can involve:

- **Chunking:** Divide the logs into segments that fit within the AI's context window. Focus on splitting by logical sections such as timestamps or events.
- **Filtering:** Pre-filter log entries to remove routine information or data not relevant to error detection. This reduces the volume of text the AI needs to analyze.
- **Summarisation:** Apply a preliminary summarisation step to condense logs while retaining critical information, especially if the logs are verbose.

### 2. **Efficient Analysis with a Small Context Window**

To effectively use LLaMA 2 for analysis within its context window limitations, consider:

- **Sequential Processing:** Analyze the preprocessed chunks sequentially. Use the AI to assess each chunk for potential issues, summarizing findings before moving to the next.
- **Context Sharing:** If possible, maintain a running context or summary of previous analyses to inform the AI as it processes subsequent chunks. This helps in understanding ongoing issues without exceeding the context window.

### 3. **AI Prompting Strategy**

Creating effective prompts for the AI to identify and summarize actionable issues is critical. Here's how to refine this:

- **Specific Error Identification:** Develop prompts that guide the AI to look for explicit error patterns and known failure modes relevant to your application and infrastructure.
- **Exclusion Criteria:** Incorporate logic to identify and exclude known false positives, such as benign timing errors, by including examples or patterns that the AI should ignore.
- **Severity Assessment:** Include prompt elements that help the AI assess the severity of identified issues, prioritizing those that require immediate attention.

### 4. **Handling False Positives**

To minimize false positives:

- **Heuristics:** Use simple heuristic rules to filter out common but inconsequential errors before feeding log data to the AI.
- **Feedback Loop:** Incorporate a mechanism for users or administrators to provide feedback on the AI's assessments, using this feedback to refine future analyses.

### 5. **Implementation Steps**

1. **Log Preprocessing Module:** Implement Python code for log chunking, filtering, and summarisation.
2. **AI Interaction Module:** Develop the interface for sending processed log chunks to LLaMA 2, including dynamic prompt construction to guide analysis.
3. **Result Synthesis Module:** Combine AI analyses from individual chunks into a comprehensive report, highlighting key issues and recommended actions.
4. **Feedback and Refinement:** Implement a feedback system to refine AI performance over time.


Addressing queries and making suggestions, let's outline the approach and provide Python code snippets that integrate these concepts, focusing on chunking with overlapping, AI-based filtering and summarisation, sequential processing with context sharing, and other aspects like error identification, exclusion criteria, severity assessment, heuristics, and establishing a feedback loop.

### 1. **Chunking with Overlapping**

Overlapping chunks can indeed be beneficial, especially for ensuring that no critical context is lost between chunks. This approach allows potential error patterns that span multiple chunks to be captured fully.

#### Code for Chunking with Overlapping

```python
def chunk_logs_with_overlap(log_path, chunk_size=1000, overlap=100):
    """Chunk logs with specified overlap."""
    with open(log_path, 'r') as file:
        logs = file.readlines()
    
    chunks = []
    start = 0
    end = chunk_size
    while start < len(logs):
        chunks.append(''.join(logs[start:end]))
        start += (chunk_size - overlap)
        end = start + chunk_size
    return chunks
```

### 2. **Filtering and Summarisation by AI**

The AI's role includes filtering irrelevant chunks and summarizing both the filtered-out chunks and those that might need further investigation. Summarisation should highlight sections with potential issues and provide brief summaries for sections deemed uneventful.

### 3. **Sequential Processing and Context Sharing**

Sequential processing can be done in two passes:
- **First Pass:** Identify and highlight critical issues or sections that require attention.
- **Second Pass:** Summarize the context built up from the first pass, focusing on drawing conclusions or identifying patterns across the entire log file.

Context sharing involves keeping track of summaries and any relevant metadata (e.g., timestamps) that help maintain continuity and relevance across chunks.

### 4. **Error Identification and Severity Assessment**

Error identification can be part of the AI prompt, guiding the model to look for specific error patterns or anomalies.

Severity assessment can also be directed by AI prompts, asking the model to classify issues based on their potential impact.

### 5. **Heuristics and Feedback Loop**

Heuristics might involve predefined rules for ignoring certain types of common but inconsequential errors.

A feedback loop can be established by allowing users to review the AI's conclusions and provide corrections or feedback, which can then be used to refine future analyses.

### Example Implementation

Combining the above concepts, here's an outline of a Python script incorporating these features:

```python
def analyze_chunks(chunks, ai_model):
    """Process each chunk with the AI model."""
    # Placeholder for AI model interaction
    summaries = []
    for chunk in chunks:
        analysis = ai_model.analyze(chunk)  # This would involve actual interaction with the AI
        summaries.append(analysis)
    return summaries

def summarize_and_filter(summaries):
    """Further process summaries to filter and highlight."""
    # Implement logic based on summaries to filter, highlight, or flag for review
    return filtered_summaries

def main(log_file_path):
    chunks = chunk_logs_with_overlap(log_file_path)
    summaries = analyze_chunks(chunks, ai_model_placeholder)
    final_report = summarize_and_filter(summaries)
    print(final_report)

# Placeholder for AI model interaction
ai_model_placeholder = None

if __name__ == "__main__":
    main("path/to/journalctl_log.log")
```

### Conclusion

This implementation provides a foundational structure for your CLI tool, focusing on handling large log files with AI. It includes chunking with overlaps to maintain context, AI-based filtering and summarisation for efficient analysis, and strategies for error identification and severity assessment. Adjustments and expansions can be made based on specific requirements and the capabilities of the AI model you integrate with.




### Example Outline for Python Implementation

```python
def preprocess_logs(log_path):
    """Chunk and filter logs for AI processing."""
    # Example: Split logs, filter, and summarize
    return preprocessed_chunks

def analyze_chunk_with_ai(chunk, ai_prompt):
    """Analyze a log chunk with LLaMA 2 using a custom prompt."""
    # Example: Send chunk to LLaMA 2, receive analysis
    return analysis_results

def compile_analysis_results(results):
    """Compile AI analyses into a comprehensive summary."""
    # Example: Aggregate results, identify key issues
    return compiled_report

def main(log_file_path):
    # Preprocess the logs
    chunks = preprocess_logs(log_file_path)
    
    # Analyze each chunk
    analyses = [analyze_chunk_with_ai(chunk, "Your custom prompt here") for chunk in chunks]
    
    # Compile and display the analysis results
    report = compile_analysis_results(analyses)
    print(report)

if __name__ == "__main__":
    main("path/to/your/log/file.log")
```

### Unit Testing

For each component, write unit tests to validate functionality. For example, tests for `preprocess_logs` could check if logs are correctly chunked and filtered. Ensure tests cover various log formats and error conditions.

### Conclusion

This plan outlines a strategy to effectively utilize a small-context-window LLM for analyzing large Linux application logs by focusing on preprocessing, efficient AI prompting, and minimizing false positives. Implementing a feedback loop for continuous refinement will enhance the accuracy and usefulness of your CLI tool over time.



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

## BBC Llama 2 for Apple macbook logs, no Workplace information
```
Based on the provided weekly log files for an Apple MacBook, the following are potential issues and solutions:

1. System software updates:
        * Potential issue: Outdated system software.
        * Solution: Check for and install any available software updates.
2. System performance:
        * Potential issue: Slow system performance.
        * Solution: Run disk cleanup and maintenance tasks to optimize system performance.
3. Network connectivity:
        * Potential issue: Poor network connectivity.
        * Solution: Check network settings and connections, and ensure that the MacBook is connected to a stable network.
4. Battery health:
        * Potential issue: Degraded battery health.
        * Solution: Run the built-in battery diagnostic test to check for any issues, and consider replacing the battery if necessary.
5. Storage issues:
        * Potential issue: Low storage space.
        * Solution: Delete unnecessary files and applications to free up storage space.
6. Security:
        * Potential issue: Malware or viruses.
        * Solution: Run a virus scan using built-in security software or a third-party antivirus program.
7. Hardware issues:
        * Potential issue: Hardware failures or malfunctions.
        * Solution: Check for any hardware issues using built-in diagnostic tools or third-party software, and consider repairing or replacing any faulty hardware.

Based on the log files provided, there are no specific issues or errors that stand out. However, it is still important to regularly check for software updates, optimize system performance, and ensure proper network connectivity to maintain the health and security of the MacBook. Additionally, it is a good idea to periodically run disk cleanup and maintenance tasks to keep the system running smoothly.

```