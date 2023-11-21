# First task it's from me

import re

demon_name = input()
# pattern = r"(([A-Za-z]+)?([\-0-9\.]))"
pattern = r"(([A-Za-z]+)([0-9\.\-]+))"
match = re.search(pattern, demon_name)
name, damage_digits = match.groups()
print(name)
print(damage_digits)

# Second task is from pepko

import re


def get_demon_health(text: str) -> int:
    health = 0
    match_pattern = re.findall(r"[^0-9\*\+\-\/\.]", text)
    for letter in match_pattern:
        health += ord(letter)
    return health


def calculate_damage(text: str) -> float:
    multiply_divide = re.findall(r"[\/\*]", text)
    number_matches = re.findall(r"(\-?[0-9]+[\.0-9]*)", text)
    base_damage = sum([float(i) for i in number_matches])
    for operation in multiply_divide:
        if operation == "*":
            base_damage *= 2
        else:
            base_damage /= 2
    return base_damage


demons = re.sub(" ", "", input()).split(",")
for demon in sorted(demons):
    health = get_demon_health(demon)
    damage = calculate_damage(demon)
    print(f"{demon} - {health} health, {damage:.2f} damage")
    
    
# Third task is from Anelia

import re
 
demons = re.split(", *", input())
demon_book = {}
 
demon_health_pattern = r'[^\d\+\-*\/\.]'
demon_damage_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demon_operators_pattern = r'[*\/]'
 
for demon in demons:
    demon = demon.strip()
    demon_health = re.findall(demon_health_pattern, demon)
    demon_book[demon] = []
    demon_book[demon].append(sum(ord(match) for match in demon_health))
 
    demon_damage = re.finditer(demon_damage_pattern, demon)
    operators = re.findall(demon_operators_pattern, demon)
    current_demon_damage = 0
 
    for value in demon_damage:
        current_demon_damage += float(value.group(0))
 
    for operator in operators:
        if operator == '*':
            current_demon_damage *= 2
        elif operator == '/':
            current_demon_damage /= 2
 
    demon_book[demon].append(current_demon_damage)
 
for demon, qualities in sorted(demon_book.items()):
    print(f'{demon} - {qualities[0]} health, {qualities[1]:.2f} damage')    