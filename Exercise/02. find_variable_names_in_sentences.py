# First task from the lecture

import re

sentence = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(pattern, sentence)
print(" ".join(variables))


# Second task from me

