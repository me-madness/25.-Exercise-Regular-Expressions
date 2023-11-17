# First task from the lecture

import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_emails = re.findall(pattern, sentence)
for extracted_email in extracted_emails:
    print(extracted_emails[0])


# Second task from me

