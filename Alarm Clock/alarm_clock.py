import time
import os


def set_alarm(alarm_time):
    while True:
        current_time = time.strftime('%H:%M:%S')
        if current_time == alarm_time:
            print("Alarm! Wake Up!!")
            os.system("afplay /System/Library/Sounds/Glass.aiff")
            break
        time.sleep(1)


def main():
    alarm_time = input("Enter the alarm time (in HH:MM:SS format): ")
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()


    
