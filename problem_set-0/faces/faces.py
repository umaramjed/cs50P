def main():
    faces = input(" ")
    text = convert(faces)
    print(text)

def convert(faces):
   return faces.replace(":)","🙂").replace(":(","🙁")


main()
