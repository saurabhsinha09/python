temps = [221, 235, 345,-9999, 198]

temp_for = []

for temp in temps:
    if temp > 0:
        temp_for.append(temp/10)
    else:
        temp_for.append(0)

print(temp_for)

temp_list = [temp/10 if temp > 0 else 0 for temp in temps]

print(temp_list)