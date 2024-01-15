import re

data = "HOST-10-140-60-[35,2],HOST-10-140-66-2"

pattern_60 = re.compile(r'HOST-10-140-60-(\[(?:\d+(?:,\d+)*)?\]|\d+)')
pattern_66 = re.compile(r'HOST-10-140-66-(\[(?:\d+(?:,\d+)*)?\]|\d+)')

matches_60 = pattern_60.findall(data)[0]
matches_66 = pattern_66.findall(data)[0]
print(matches_60)
print(matches_66)

node_list_60 = eval(matches_60) if '[' in matches_60 else int(matches_60)
node_list_66 = eval(matches_66) if '[' in matches_66 else int(matches_66)

print(node_list_60, type(node_list_60), type(node_list_60[0]))
print(node_list_66)


# for match in matches_60:
#     values_str = match.group(1)
#     values = [int(val) for val in re.findall(r'\d+', values_str)]
#     print(f"Group 60: {values}")

# for match in matches_66:
#     values_str = match.group(1)
#     values = [int(val) for val in re.findall(r'\d+', values_str)]
#     print(f"Group 66: {values}")
