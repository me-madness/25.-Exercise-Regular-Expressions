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
    name = "".join(matches_name)
    scores = "".join(matches_distance)
    if name in list_of_participants:
        for score in scores:
            common_score = score
            new_score += int(common_score)
        distance[name] = new_score    
    print(distance)
    commands = input()
    
