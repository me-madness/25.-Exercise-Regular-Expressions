import re

demon_name = input()
# pattern = r"(([A-Za-z]+)?([\-0-9\.]))"
pattern = r"([A-Za-z]+)([0-9\.\-]+)"
match = re.search(pattern, demon_name)
name, damage_digits = match.groups()
print(name)
print(damage_digits)