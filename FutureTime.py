#FutureTime.py
#Name: Pierce Limbo
#Date: 9/4/2025
#Assignment: Lab2

import datetime

def main():
    now = datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute

    Hours = int(input("Enter number of hours to add: "))
    Minutes = int(input("Enter number of minutes to ad1d: "))

    totalMinutes = currentHour * 60 + currentMinute + Hours * 60 + Minutes

    futureHour = (totalMinutes // 60) % 24
    futureMinute = totalMinutes % 60

    print("Future time: {:02d}:{:02d}".format(futureHour, futureMinute))

if __name__ == '__main__':
    main()
