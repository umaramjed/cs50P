#
# ask user for input for a file name
# output matching the extension to MIME types
#
def main():
    file_name = input("File name: ").lower().strip() #user lower for case incensative and strip to ignore any space
    file_type(file_name)

def file_type(file_name):
    if file_name.endswith('.gif'):
        print("image/gif")
    elif file_name.endswith('.jpg') :
        print("image/jpeg")
    elif file_name.endswith('.jpeg') :
        print("image/jpeg")
    elif file_name.endswith('.png') :
        print("image/png")
    elif file_name.endswith('.pdf') :
        print("application/pdf")
    elif file_name.endswith('.txt') :
        print("text/plain")
    elif file_name.endswith('.zip') :
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == '__main__':
    main()
