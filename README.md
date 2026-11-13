# Python Log Analyzer & Error Monitoring Tool

A Python-based log analysis tool that reads application log files, identifies different log levels, tracks errors, detects repeated issues, and generates an analysis report.

## Project Overview

This project analyzes text-based application logs using core Python concepts. It helps monitor application activity, identify errors, and summarize important information in a readable report.

## Features

- Reads and processes log files using file handling.
- Counts INFO, WARNING, and ERROR entries.
- Detects empty and malformed log entries.
- Identifies unknown log levels.
- Collects error messages and counts repeated errors.
- Finds the most frequently occurring error.
- Calculates the error percentage.
- Searches logs using case-insensitive keyword matching.
- Counts matching search results.
- Generates a text-based analysis report.
- Handles empty log files without division errors.

## Technologies Used

- Python 3
- File Handling
- Lists and Dictionaries
- Loops and Conditional Statements
- String Methods
- Exception and Input Validation Concepts

## Project Structure

```text
python-log-analyzer/
│
├── main.py
├── sample_logs.txt
├── analysis_report.txt
└── README.md
```

## How to Run

1. Clone or download this repository.
2. Make sure Python 3 is installed.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python main.py
```

5. Enter a keyword when prompted to search the logs.
6. View the generated `analysis_report.txt` file.

## Sample Analysis Results

| Metric | Result |
|---|---:|
| Total Logs | 10 |
| INFO | 4 |
| WARNING | 2 |
| ERROR | 4 |
| Invalid Logs | 0 |
| Error Percentage | 40.00% |
| Database Matches | 3 |

**Most Frequent Error:** Database connection failed

## Learning Outcomes

Through this project, I practiced:

- Reading and processing structured text files.
- Working with lists and dictionaries.
- Counting and grouping repeated data.
- Validating input records.
- Searching and analyzing text.
- Generating reports using Python file handling.

## Future Improvements

- Add date-based log filtering.
- Organize the program into reusable functions.
- Add support for larger log files.
- Improve error handling for missing files.

---

**Author:** Saba Noor

**Project:** Python Learning Journey – Project 3
