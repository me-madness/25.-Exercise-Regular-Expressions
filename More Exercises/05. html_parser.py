import re

data = input()
pattern_title = r"<title>([A-Za-z\ ]+)<\/title>"
pattern_content = r""
match_title = re.findal(pattern_title, data)
match_content = re.findal(pattern_content, data)
print(f"{''.join(match_title)}")