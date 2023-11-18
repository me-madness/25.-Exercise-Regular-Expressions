import re

list_of_participants = input().split(",")
commands = input()
pattern = r"(([A-Za-z]+)|([0-9]+))"
distance = {}
while commands != "end of race":
    commands = input()
    matches = re.findall(pattern, commands)
    print(" ".join(list_of_participants))
    print(matches)