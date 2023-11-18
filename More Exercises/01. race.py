import re

list_of_participants = input().split(",")
pattern_name = r"[A-Za-z]+"
pattern_distance = r"\d"
distance = {}
new_score = 0
commands = input()
while commands != "end of race":
    matches_name = re.findall(pattern_name, commands)
    matches_distance = re.findall(pattern_distance, commands)
    distance = "".join(matches_name)
    scores = "".join(matches_distance)
    for score in scores:
        common_score = score
        new_score += int(common_score)
    distance[0] = new_score
    
    if matches_name not in list_of_participants:
        pass
    else:
        print(matches_distance)