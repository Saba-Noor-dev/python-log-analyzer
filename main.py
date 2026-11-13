with open("sample_logs.txt" , "r") as file:
    logs = file.readlines()
    info_count = 0
    warning_count = 0
    error_count = 0
    error_messages = []
    error_counts = {}
    invalid_count = 0
    for line in logs:
        line = line.strip()
        if not line:
            print(f"Empty log entry: {line}")
            invalid_count += 1
            continue
        parts = line.split(" | ")
        if len(parts) != 3:
            print(f"Malformed log entry: {line}")
            invalid_count += 1
            continue
        level = parts[1].strip()
        if level == "INFO":
            info_count += 1
        elif level == "WARNING":
            warning_count += 1
        elif level == "ERROR":
            error_count += 1
            error_messages.append(parts[2].strip())
            if parts[2].strip() in error_counts:
                error_counts[parts[2].strip()] += 1
            else:
                error_counts[parts[2].strip()] = 1
        else:
           print(f"Unknown Log Level: {level}") 
           invalid_count += 1

total_logs = info_count + warning_count + error_count 
if total_logs > 0:
    error_percentage = (error_count / total_logs) * 100
else:
    error_percentage = 0
if error_counts:
    most_frequent_error = max(error_counts, key=error_counts.get)
else:
    print("No Errors Found")

search_term = input("Search for specific logs: ")
found = False
search_count = 0
for line in logs:
    if search_term.lower() in line.lower():
        print(line)
        found = True
        search_count += 1
if not found:
    print("No logs found containing the search term.")

with open("analysis_report.txt", "w") as result_file:
    result_file.write(f"INFO: {info_count}\n")
    result_file.write(f"WARNING: {warning_count}\n")
    result_file.write(f"ERROR: {error_count}\n")
    result_file.write(f"Total Logs: {total_logs}\n")
    result_file.write(f"Invalid Logs: {invalid_count}\n")
    result_file.write(f"Error Percentage: {error_percentage:.2f}%\n")
    result_file.write(f"Search Term: {search_term} - Found {search_count} occurrences\n")
    result_file.write("Error Messages:\n")
    for msg in error_messages:
        result_file.write(f"  - {msg}\n")
    result_file.write("Error Counts:\n")
    for msg, count in error_counts.items():
        result_file.write(f"  - {msg}: {count}\n")
    if error_counts:
        result_file.write(f"Most Frequent Error: {most_frequent_error}\n")
    else:
        result_file.write("No Errors Found\n")