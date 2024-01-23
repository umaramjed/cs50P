import sys

def count_code_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        code_lines = 0
        in_multiline_comment = False

        for line in lines:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if line.startswith('"""') or line.startswith("'''") or line.strip() == "":
                in_multiline_comment = not in_multiline_comment

            if not in_multiline_comment:
                code_lines += 1

        return code_lines

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")

    code_lines = count_code_lines(file_path)
    print(code_lines)

if __name__ == "__main__":
    main()
