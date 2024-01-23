import sys
import os
import csv
from tabulate import tabulate

def load_csv_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        return data
    except FileNotFoundError:
        sys.exit("Error: The specified CSV file does not exist.")
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    data = load_csv_file(file_path)

    headers = data[0]
    table_data = data[1:]

    table = tabulate(table_data, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
