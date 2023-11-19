import re

data = input()
pattern_title = r"<title>([A-Za-z\ ]+)<\/title>"
pattern_content = r""
match_title = re.findall(pattern_title, data)
match_content = re.findall(pattern_content, data)
print(f"Title: {''.join(match_title)}")