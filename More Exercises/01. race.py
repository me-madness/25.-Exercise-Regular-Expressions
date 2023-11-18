import re

list_of_participants = input().split(",")
pattern_name = r"[A-Za-z]+"
pattern_distance = r"[0-9]+"
distance = {}
commands = input()
while commands != "end of race":
    matches_name = re.findall(pattern_name, commands)
    matches_distance = re.findall(pattern_distance, commands)
    distance = "".join(matches_name)
    score = ",".join(matches_distance)
    commands = input()
    print(distance)    
    print(score)
    
    if matches_name not in list_of_participants:
        pass
    else:
        print(matches_distance)