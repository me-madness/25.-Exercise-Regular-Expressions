import re

demon_name = input()
# pattern = r"(([A-Za-z]+)?([\-0-9\.]))"
pattern = r"([A-Za-z]+)([0-9\.\-]+)"
match = re.match(pattern, demon_name)
name = match.group(1)
damage_digits = match.group(2)
