import re
import math

move_regex = re.compile(r"^([LR])(\d+)")

# Read in the input file and create a list of moves
def create_list(file_handle):
    move_list = []
    for line in file_handle:
        match = re.match(move_regex, line.strip("\r\n"))
        if match:
            for item in match.groups():
                if item == None:
                    print("This row seems invalid")
                else:
                    continue
            direction = match.group(1)
            move = int(match.group(2))
            move_list.append([direction, move])
    return move_list

def resolve_moves(start, move_list):
    curr_pos = start
    naughty = 0
    for move in move_list:
        match move:
            case ('L', s):
                s_pos = curr_pos
                cross = abs(math.floor((curr_pos - s)/100))
                curr_pos = (curr_pos - s) % 100
                print(f"Start: {s_pos}, Rotate left by {s}, End: {curr_pos}")
                if cross > 0:
                    naughty = naughty + cross
                    print(f"Dial crossed zero {cross} times in this rotation")
            case ('R', s):
                s_pos = curr_pos
                cross = abs(math.floor((curr_pos + s)/100))
                curr_pos = (curr_pos + s) % 100
                print(f"Start: {s_pos}, Rotate right by {s}, End: {curr_pos}")
                if cross > 0:
                    naughty = naughty + cross
                    print(f"Dial crossed zero {cross} times in this rotation")
            case _:
                print("This move seems invalid somehow!")
    return curr_pos, naughty

def main():
    print("Opening file")
    file = open("input1.txt", 'r')
    move_list = create_list(file)
    start = int(50)
    end, naughty = resolve_moves(start, move_list)
    print(f"Current position: {end}, crossed zero: {naughty} times")

if __name__ == "__main__":
    main()
