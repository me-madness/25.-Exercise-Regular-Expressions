import re

total_sum = 0
# pattern = r"%([A-Za-z]+)%<([A-Za-z]+)>\|(\d)\|(\d+\.\d+)\$"
pattern = r"%([A-Z][a-z]+)%<([A-Za-z]+)>\|(\d)\|(\d+\.\d+)\$"
command = input()
while command != "end of shift":
    match = re.search(pattern, command)
    if match:
        customer_name, product, quantity, prise = match.groups()
        sum = int(quantity) * float(prise)
        total_sum += sum
        print(f"{customer_name}: {product} - {sum:.2f}")
    command = input()
print(f"total income: {total_sum:.2f}")    
    
    