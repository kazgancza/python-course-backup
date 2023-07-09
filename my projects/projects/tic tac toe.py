import random


CHARS = {
    "a1": " ",
    "a2": " ",
    "a3": " ",
    
    "b1": " ",
    "b2": " ",
    "b3": " ",

    "c1": " ",
    "c2": " ",
    "c3": " ",
}

CHARS_NUMBERS = {
    "1": "a1",
    "2": "a2",
    "3": "a3",

    "4": "b1",
    "5": "b2",
    "6": "b3",

    "7": "c1",
    "8": "c2",
    "9": "c3",

}

unused_chars = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]


def show_table():
    print(f"{CHARS['a1']}|{CHARS['a2']}|{CHARS['a3']}\n\
{CHARS['b1']}|{CHARS['b2']}|{CHARS['b3']}\n\
{CHARS['c1']}|{CHARS['c2']}|{CHARS['c3']}")

def generate_X():
    char_name = random.choice(unused_chars)
    CHARS[char_name] = "X"
    unused_chars.remove(char_name)

def check_winner_X():
    if CHARS["a1"] == "X" and CHARS["a2"] == "X" and CHARS["a3"] == "X":
        return True
    if CHARS["b1"] == "X" and CHARS["b2"] == "X" and CHARS["b3"] == "X":
        return True
    if CHARS["c1"] == "X" and CHARS["c2"] == "X" and CHARS["c3"] == "X":
        return True
    
    if CHARS["a1"] == "X" and CHARS["b1"] == "X" and CHARS["c1"] == "X":
        return True
    if CHARS["a2"] == "X" and CHARS["b2"] == "X" and CHARS["c2"] == "X":
        return True
    if CHARS["a3"] == "X" and CHARS["b3"] == "X" and CHARS["c3"] == "X":
        return True

    if CHARS["a1"] == "X" and CHARS["b2"] == "X" and CHARS["c3"] == "X":
        return True
    if CHARS["a3"] == "X" and CHARS["b2"] == "X" and CHARS["c1"] == "X":
        return True

    return False

def check_winner_O():
    if CHARS["a1"] == "O" and CHARS["a2"] == "O" and CHARS["a3"] == "O":
        return True
    if CHARS["b1"] == "O" and CHARS["b2"] == "O" and CHARS["b3"] == "O":
        return True
    if CHARS["c1"] == "O" and CHARS["c2"] == "O" and CHARS["c3"] == "O":
        return True
    
    if CHARS["a1"] == "O" and CHARS["b1"] == "O" and CHARS["c1"] == "O":
        return True
    if CHARS["a2"] == "O" and CHARS["b2"] == "O" and CHARS["c2"] == "O":
        return True
    if CHARS["a3"] == "O" and CHARS["b3"] == "O" and CHARS["c3"] == "O":
        return True

    if CHARS["a1"] == "O" and CHARS["b2"] == "O" and CHARS["c3"] == "O":
        return True
    if CHARS["a3"] == "O" and CHARS["b2"] == "O" and CHARS["c1"] == "O":
        return True

    return False

def generate_O():
    while True:
        players_input = int(input("Które pole chcesz zaznaczyć? (Wpisz cyfrę od 1-9): "))
        
        if 1 <= players_input <= 9:
            players_input_char = CHARS_NUMBERS[str(players_input)]
            if players_input_char in unused_chars:
                CHARS[players_input_char] = "O"
                unused_chars.remove(players_input_char)
                return
            else:
                print("To pole jest już zajęte")
                continue
        else:
            print("Zła wartość")
            continue


def game():
    while True:
        generate_X()
        if check_winner_O() is True:
            print("Gratulację. Wygrałeś!")
            break
        elif check_winner_X is True:
            print("Niestety, tym razem przegrałeś.")
            break
        show_table()
        if unused_chars is not False:
            print(unused_chars)
            generate_O()
            show_table()
            print(CHARS)
            if check_winner_O() is True:
                print("Gratulację. Wygrałeś!")
                break
            elif check_winner_X is True:
                print("Niestety, tym razem przegrałeś.")
                break
        
            else:
                continue

        else:
            print("Remis. Brak możliwych ruchów")
            break


game()
