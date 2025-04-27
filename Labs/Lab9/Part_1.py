import sys
import os

def log_level_count(log_file):

    """Counts occurences"""

    level_count = {}

    try:
        with open(log_file, 'r') as opened_file:

            for line in opened_file:
                top_line = line.upper()
                
                if "INFO:" in top_line:
                    if "INFO" not in level_count:
                        level_count["INFO"] = 0
                    level_count["INFO"] += 1

                elif "WARNING:" in top_line:
                    if "WARNING" not in level_count:
                        level_count["WARNING"] = 0
                    level_count["WARNING", 0] += 1

                elif "ERROR:" in top_line:
                    if "ERROR" not in level_count:
                        level_count["ERROR"] = 0
                    level_count["ERROR", 0] += 1

                elif "CRITICAL:" in top_line:
                    if "CRITICAL" not in level_count:
                        level_count["CRITICAL"] = 0
                    level_count["CRITICAL", 0] += 1

    except FileNotFoundError:
        print(f"File not found: {log_file}")
        return {}
    
    except Exception as e:
        print(f"An error occurred when trying to the read the log files: {e}")
        return {}
    
    return level_count

def extract_messages(log_file):

    """Extracts messages"""

    messages = []

    try:
        with open(log_file, 'r') as opened_file:
            for each_line in opened_file:

                log_levels = ["INFO:", "WARNING:", "ERROR:", "CRITICAL:"]

                if "INFO:" in each_line or "WARNING:" in each_line or "ERROR:" in each_line or "CRITICAL:" in each_line:
                    
                    colon_position = each_line.find(":")

                    if colon_position != -1:
                        message = each_line[colon_position + 1:].strip()
                        messages.append(message)

    except FileNotFoundError:
        print(f"File not found: {log_file}")
        return []

    except Exception as e:
        print(f"An error occurred when trying to the read the log files: {e}")
        return []
    
    return messages

def summarize_logs(log_file):

    """Got help for the messages output format"""

    levels = log_level_count(log_file)
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
        print("---------------")

        for message_index, the_message in enumerate(messages[:5]):
            print(f"  [{message_index+1}] {the_message}")

        if len(messages) > 5:
            print("  ...")
        print(f"Total Messages: {len(messages)}")

    else:
        print("No log messages found.")

def main():

    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_directory = os.path.join(script_directory, "Logs")

    if not os.path.exists(log_directory) or not os.path.isdir(log_directory):
        print(f"Error: Directory '{log_directory}' not found.")
        return

    log_files_to_analyze = [
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\my_app_utils_db.log",
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\my_app_utils.log",
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\my_app.log",
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\RSVP_Agent_processing.log",
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\systemd_core_performance.log",
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\systemd_core.log",
        r"C:\Users\Shanto\Documents\GitHub\homeworkfolder-shant-bekverdyan\Labs\Lab9\Logs\systemd.log",
    ]

    for log_file_name in log_files_to_analyze:

        log_file_path = os.path.join(log_directory, log_file_name)
        print(f"Debugging: Trying to access file at path: '{log_file_path}'")

        if os.path.exists(log_file_path):
            summarize_logs(log_file_path)

        else:
            print(f"Error: Log file '{log_file_path}' not found.")

if __name__ == "__main__":
    main()
