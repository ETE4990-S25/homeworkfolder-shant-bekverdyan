import sys
import os
import json

def process_log(log_file_path, output_file="log_counts.json"):

    level_counts = {}

    try:
        with open(log_file_path, 'r') as f:

            for line in f:
                parts = line.split(" | ")

                if len(parts) >= 4:
                    log_level = parts[2].strip().upper()
                    message = parts[3].strip()

                    if log_level in ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]:
                        if log_level not in level_counts:
                            level_counts[log_level] = {}

                        if message not in level_counts[log_level]:
                            level_counts[log_level][message] = 0

                        level_counts[log_level][message] += 1

    except FileNotFoundError:
        print(f"Error: Log file not found at '{log_file_path}'")
        return
    
    except Exception as e:
        print(f"Error reading log file '{log_file_path}': {e}")
        return

    try:
        with open(output_file, 'w') as outfile:
            json.dump(level_counts, outfile, indent=4)
        print(f"Log level counts have been written to '{output_file}'")

    except Exception as e:
        print(f"Error writing to JSON file '{output_file}': {e}")

def count_log_levels(log_file):

    level_counts = {}

    try:
        with open(log_file, 'r') as opened_file:

            for line in opened_file:
                parts = line.split(" | ")

                if len(parts) >= 4:
                    log_level = parts[2].strip().upper()

                    if log_level in ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]:

                        if log_level not in level_counts:
                            level_counts[log_level] = 0
                        level_counts[log_level] += 1

    except FileNotFoundError:
        print(f"Error: File not found - {log_file}")
        return {}
    
    except Exception as e:
        print(f"An error occurred while reading the log file: {e}")
        return {}
    
    return level_counts

def extract_messages(log_file):

    the_messages = []

    try:
        with open(log_file, 'r') as opened_file:

            for each_line in opened_file:
                parts = each_line.split(" | ")

                if len(parts) >= 4:
                    the_message = parts[3].strip()
                    the_messages.append(the_message)

    except FileNotFoundError:
        print(f"Error: File not found --> {log_file}")
        return []
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    return the_messages

def summarize_logs(log_file):

    print(f"Analyzing log file: {log_file}")

    levels = count_log_levels(log_file)
    messages = extract_messages(log_file)

    if not levels and not messages:
        print("No log data found or error reading file.")
        return

    print("Log Summary:")
    print("-------------")

    if levels:
        print("Log Level Counts:")
        for level_name, count_value in levels.items():
            print(f"{level_name}: {count_value}")

    else:
        print("No log levels found.")

    if messages:

        print("Sample Log Messages:")

        for message_index, the_message in enumerate(messages[:5]):
            print(f"  [{message_index+1}] {the_message}")

        if len(messages) > 5:
            print("  ...")
        print(f"Total Messages: {len(messages)}")

    else:
        print("No log messages found.")

def main():

    """Got help for this part"""

    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <log_file>")
        return

    log_file_name = sys.argv[1]

    if not os.path.exists(log_file_name):
        print(f"Error: The file '{log_file_name}' does not exist.")
        return

    process_log(log_file_name)
    summarize_logs(log_file_name)

if __name__ == "__main__":
    main()
