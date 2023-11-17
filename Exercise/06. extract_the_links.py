# First task from the lecture

import re

text = input()
pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"

while text:
    match = re.search(pattern, text)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    text = input()


# Second task from me

