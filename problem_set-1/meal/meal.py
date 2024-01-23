#
#breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
#prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time


def main():


    def output(time):
        time = input("What time is it? ") #user lower for case incensative and strip to ignore any space
        time = convert(time)
        try:
            if 7 <= time <= 8:
                print("breakfast time")
            elif 12 <= time <= 13:
                print("lunch time")
            elif 18 <= time <= 19:
                print("dinner time")
        except:
            exit()

def convert(time):
    if time.endswith(" a.m."):
        time = time.split(' a.m.')
        time = time[0].split(':')
        return round(int(time[0]) + int(time[1])/60, 2)
    elif time.endswith(" p.m."):
        time = time.split(' p.m.')
        time = time[0].split(':')
        return round(12 + int(time[0]) + int(time[1])/60, 2)
    else:
        time = time.split(":")
        return round(int(time[0]) + int(time[1])/60, 2)

if __name__ == "__main__":
    main()
