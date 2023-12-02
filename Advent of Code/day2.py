import re

impossible_set = set()
impossible_list = []

# Add impossible games (red>12, green>13, blue>14) to set of impossible games
with open ("day2.txt", 'r') as file:
    for line in file:
        match_red = re.findall(r'(\d+)\sred', line)
        match_green = re.findall(r'(\d+)\sgreen', line)
        match_blue = re.findall(r'(\d+)\sblue', line)
        for red in match_red:
            if int(red) > 12:
                impossible_set.add(line)
        for green in match_green:
            if int(green) > 13:
                impossible_set.add(line)
        for blue in match_blue:
            if int(blue) > 14:
                impossible_set.add(line)

# Extract game ID for each game in impossible set
for ID in impossible_set:
    match = re.search(r'Game\s(\d+)', ID)
    imp_ID = match.group(1)
    impossible_list.append(imp_ID)

# Sum of game IDs of all impossible games
impossible = (sum(map(int, impossible_list)))
# Sum of game IDs of all possible games [all integers from 1 to 100 (simple workaround as I've misinterpreted the question)]
possible = 100*(100+1)//2
print(possible - impossible)
