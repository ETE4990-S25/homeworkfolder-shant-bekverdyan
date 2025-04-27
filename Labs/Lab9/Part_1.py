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
                    level_count["WARNING"] += 1

                elif "ERROR:" in top_line:
                    if "ERROR" not in level_count:
                        level_count["ERROR"] = 0
                    level_count["ERROR"] += 1

                elif "CRITICAL:" in top_line:
                    if "CRITICAL" not in level_count:
                        level_count["CRITICAL"] = 0
                    level_count["CRITICAL"] += 1

                elif "DEBUG:" in top_line:
                    if "DEBUG" not in level_count:
                        level_count["DEBUG"] = 0
                    level_count["DEBUG"] += 1

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
                if "INFO:" in each_line or "WARNING:" in each_line or "ERROR:" in each_line or "CRITICAL:" in each_line or "DEBUG:" in each_line:
                    
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

    print("\nLog Summary:")
    print("-------------")
    if levels:
        print("\nLog Level Counts:")
        for level_name, count_value in levels.items():
            print(f"{level_name}: {count_value}")
    else:
        print("\nNo log levels found.")

    if messages:
        print("\nSample Log Messages:")
        print("---------------")

        for message_index, the_message in enumerate(messages[:5]):
            print(f"  [{message_index+1}] {the_message}")

        if len(messages) > 5:
            print("  ...")
        print(f"\nTotal Messages: {len(messages)}")

    else:
        print("\nNo log messages found.")

def main():

    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <log_file>")
        return

    log_file_name = sys.argv[1]

    if not os.path.exists(log_file_name):
        print(f"Error: The file '{log_file_name}' does not exist.")
        return

    summarize_logs(log_file_name)

if __name__ == "__main__":
    main()
