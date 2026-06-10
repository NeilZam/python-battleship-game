import random
import time

area = [[]]
area_size = 10
how_many_ships = 8
how_many_shots = 50
end_game = False
ships_sunk = 0
where_are_ships = [[]]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_place_ship(start_row, end_row, start_col, end_col):
    global area
    global where_are_ships

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if area[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        where_are_ships.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                area[r][c] = "O"
    return all_valid


def place_ship_grid(row, col, direction, length):
    global area_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= area_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= area_size:
            return False
        end_row = row + length

    return validate_place_ship(start_row, end_row, start_col, end_col)


def make_area():
    global area
    global area_size
    global how_many_ships
    global where_are_ships

    random.seed(time.time())

    rows, cols = (area_size, area_size)

    area = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        area.append(row)

    ships_placed = 0

    where_are_ships = []

    while ships_placed != how_many_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if place_ship_grid(random_row, random_col, direction, ship_size):
            ships_placed += 1


def put_area_on_game():
    global area
    global letters

    debug_mode = True

    letters = letters[0: len(area) + 1]

    for row in range(len(area)):
        print(letters[row], end=") ")
        for col in range(len(area[row])):
            if area[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(area[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(area[0])):
        print(str(i), end=" ")
    print("")


def valid_bullet():
    
    global letters
    global area

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = letters.find(row)
        if not (-1 < row < area_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < area_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if area[row][col] == "#" or area[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if area[row][col] == "." or area[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_sunk(row, col):
    global where_are_ships
    global area

    for position in where_are_ships:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if area[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    global area
    global ships_sunk
    global how_many_shots

    row, col = valid_bullet()
    print("")
    print("----------------------------")

    if area[row][col] == ".":
        print("You missed, no ship was shot")
        area[row][col] = "#"
    elif area[row][col] == "O":
        print("You hit!", end=" ")
        area[row][col] = "X"
        if check_sunk(row, col):
            print("A ship was completely sunk!")
            ships_sunk += 1
        else:
            print("A ship was shot")

    how_many_shots -= 1


def is_game_over():
    global ships_sunk
    global how_many_ships
    global how_many_shots
    global end_game

    if how_many_ships == ships_sunk:
        print("you won!")
        end_game = True
    elif how_many_shots <= 0:
        print("you lost!")
        end_game = True


def main():
    global end_game

    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    make_area()

    while end_game is False:
        put_area_on_game()
        print("Number of ships remaining: " + str(how_many_ships - ships_sunk))
        print("Number of bullets left: " + str(how_many_shots))
        shoot_bullet()
        print("----------------------------")
        print("")
        is_game_over()

if __name__ == '__main__':
    main()
