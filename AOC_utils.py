import os
import requests
import json
import time

if not os.path.exists("days"):
    os.mkdir("days")
    # create blank cookie file
    with open("days/cookies.json","w") as f:
        json.dump({"session":""},f)
    print("Created days folder and blank cookie file. Please add your session cookie to days/cookies.json")
    time.sleep(5)
    exit()

cookies = json.load(open("days/cookies.json","r"))

def get_day(day, year=2024):
    # check if the file already exists
    if os.path.exists(f"days/day{day}input.txt"):
        print(f"Day {day} input already downloaded")
    else:
        r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies)
        with open(f"days/day{day}input.txt","w") as f:
            f.write(r.text)
        print(f"Downloaded day {day} input")

    
    with open(f'days/day{day}input.txt') as f:
        input_data = f.readlines()
    input_data = [line[:-1] if line[-1] == '\n' else line for line in input_data]

    return input_data