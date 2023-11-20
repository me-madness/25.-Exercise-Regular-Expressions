import re

demon_name = input()
pattern = r"(([A-Za-z]+)|([\-0-9\.]))"
match = re.findall(pattern, demon_name)
print(match)
