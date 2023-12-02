import re

power_list = []

with open('day2.txt', 'r') as file:
    for line in file:
        match_red = re.findall(r'(\d+)\sred', line)
        match_green = re.findall(r'(\d+)\sgreen', line)
        match_blue = re.findall(r'(\d+)\sblue', line)
        #Obtain the highest value for each colour in each line
        highest_red = max(map(int,match_red))
        highest_green = max(map(int,match_green))
        highest_blue = max(map(int,match_blue))
        #Adds the power (multiplication of the highest values for each colour) to list
        power_list.append(highest_red*highest_blue*highest_green)

#Calculates the sum of all obtained powers 
answer = sum(power_list)
print(answer)