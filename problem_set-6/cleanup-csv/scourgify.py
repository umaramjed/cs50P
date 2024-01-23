import sys
import csv

def convert_csv(input_file, output_file):
    try:
        with open(input_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        if not rows:
            sys.exit("Error: The input CSV file is empty.")

        converted_data = []

        for row in rows:
            full_name = row.get("name", "").strip()
            house = row.get("house", "")

            if not full_name:
                sys.exit("Error: Some rows in the input CSV file have missing 'name' field.")

            if ',' not in full_name:
                sys.exit("Error: 'name' field does not contain a comma to separate first and last names.")

            first_name, last_name = full_name.split(',', 1)
            converted_data.append({"first": first_name.strip(), "last": last_name.strip(), "house": house})

        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(converted_data)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_csv(input_file, output_file)
    '''print(f"Conversion completed. Data written to '{output_file}'.")'''

if __name__ == "__main__":
    main()
