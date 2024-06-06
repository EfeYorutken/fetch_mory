import json
from datetime import *

path = "./config.json"

average_life = 74

def read_json(file_path):
    json_to_dict = {}
    with open(path , "r") as f:
        json_to_dict = json.loads("".join(f.readlines()))
    return json_to_dict

#seems iffy
def days_between(start, end):
    return int(int(str(end - start).split(" ")[0]))

def print_death_calander(to_live, lived, width, past, future, motion_over_time=1):
    amount = lived + to_live
    new_line_counter = 0
    for day in range(0,amount,motion_over_time):
        if new_line_counter == width:
            print()
            new_line_counter = 0
        if day > lived:
            print(f"{future} ", end="")
        else:
            print(f"{past} ", end="")
        new_line_counter += 1


json_res = read_json(path)

bday = json_res["birth_date"].split(".")
#not sure why i cant use map on the list but python does not like it
bday = [int(x) for x in bday]
unit_per_line = json_res["displays"]["char_per_line"]
lived_char = json_res["displays"]["char_lived"]
to_live_char = json_res["displays"]["char_to_live"]
motion_over_time = json_res["displays"]["motion_over_time"]
units = json_res["measures"]


(b_day, b_mnt, b_yar) = (bday[0], bday[1], bday[2])

today = datetime.now()
birthday = datetime(b_yar, b_mnt, b_day)
deathday = datetime(b_yar + average_life ,b_mnt, b_day)

days_lived = days_between(birthday, today)
days_to_live = days_between(today, deathday)

print_death_calander(days_to_live, days_lived, unit_per_line, lived_char, to_live_char, motion_over_time)

print()

to_live_units = [(unit, days_to_live/units[unit]) for unit in units]
lived_units = [(unit, days_lived/units[unit]) for unit in units]

print("you have lived")
for i in range(len(lived_units)):
    print(f"\t{lived_units[i][1]} {lived_units[i][0]}")

print("you have")
for i in range(len(lived_units)):
    print(f"\t{to_live_units[i][1]} {to_live_units[i][0]}")
print("to live")


print("  _____   ____  _   _ _______  __          __      _____ _______ ______   _____ _______ ")
print(" |  __ \\ / __ \\| \\ | |__   __| \\ \\        / /\\    / ____|__   __|  ____| |_   _|__   __|")
print(" | |  | | |  | |  \\| |  | |     \\ \\  /\\  / /  \\  | (___    | |  | |__      | |    | |   ")
print(" | |  | | |  | | . ` |  | |      \\ \\/  \\/ / /\\ \\  \\___ \\   | |  |  __|     | |    | |   ")
print(" | |__| | |__| | |\\  |  | |       \\  /\\  / ____ \\ ____) |  | |  | |____   _| |_   | |   ")
print(" |_____/ \\____/|_| \\_|  |_|        \\/  \\/_/    \\_\\_____/   |_|  |______| |_____|  |_|   ")
print("memento mori")
