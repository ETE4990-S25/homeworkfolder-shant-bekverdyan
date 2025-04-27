import time
import json
import threading

json_file_path = "log_counts.json"

def monitor_log_activity():
    previous_data = {}
    critical_messages = []

    while True:
        try:
            with open(json_file_path, 'r') as log_file:

                try:
                    current_data = json.load(log_file)

                except json.JSONDecodeError:
                    print("Error: Invalid JSON format in log file. Waiting for valid data...")
                    time.sleep(1)
                    continue

            if current_data != previous_data:
                print("Log Activity Update:")
                print("-" * 20)

                total_messages = 0

                for level, messages in current_data.items():

                    count = sum(messages.values())
                    print(f"{level}: {count} messages")
                    total_messages += count

                print(f"Total Messages: {total_messages}")

                new_critical_messages = []

                if "CRITICAL" in current_data:

                    current_critical_messages = list(current_data["CRITICAL"].keys())

                    new_critical_messages = [
                        msg for msg in current_critical_messages if msg not in critical_messages
                    ]

                    critical_messages.extend(new_critical_messages)

                    if new_critical_messages:

                        print("New Critical Messages:")
                        for msg in new_critical_messages:
                            print(f"  - {msg}")

                previous_data = current_data

        except FileNotFoundError:
            print(f"Error: JSON file not found at {json_file_path}.")
            time.sleep(1)
            continue

        except Exception as e:
            print(f"Error monitoring log activity: {e}")
            time.sleep(1)

        time.sleep(1)


def main():

    print("Starting Log Activity Monitor...")
    activity_thread = threading.Thread(target=monitor_log_activity, daemon=True)
    activity_thread.start()

    while True:
        time.sleep(1)

    print("Done")


if __name__ == "__main__":
    main()
