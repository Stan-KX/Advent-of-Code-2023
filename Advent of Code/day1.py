import re

#Convert word to number:
def word_to_num():
    replace_words = {
        'one' : 'o1e',
        'two' : 't2o',
        'three' : 't3e',
        'four' : 'f4r',
        'five' : 'f5e',
        'six' : 's6x',
        'seven' : 's7n',
        'eight' : 'e8t',
        'nine' : 'n9e'
    }
    with open('puzzles.txt', 'r') as file:
        data = file.read()
        for word, num in replace_words.items():
            data = data.replace(word,num)
    with open('puzzles2.txt', 'w') as file:
        file.write(data)

word_to_num()


# Find first and last digit in string
def find_digits(s):
    match = re.search(r"(\d)", s)
    first = match.group(1) if match else None
    reversed_s = s[::-1]
    match = re.search(r"(\d)", reversed_s)
    last = match.group(1) if match else None
    return first + last


# Finds first and last digit in each row and appends to list
def main():
    word_to_num()
    with open("puzzles2.txt", "r") as file:
        numbers_list = []
        for s in file:
            digits = find_digits(s)
            if digits is not None:
                numbers_list.append(digits)
            else:
                continue
    int_list = list(map(int, numbers_list))
    print(sum(int_list))

if __name__ == '__main__':
    main()