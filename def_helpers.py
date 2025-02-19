
def draw_board(spots):
    separator = "+---+---+---+"  
    board_width = 67  
    
    row1 = f"| {spots[1]} | {spots[2]} | {spots[3]} |".center(board_width)
    row2 = f"| {spots[4]} | {spots[5]} | {spots[6]} |".center(board_width)
    row3 = f"| {spots[7]} | {spots[8]} | {spots[9]} |".center(board_width)
    separator_centered = separator.center(board_width)
    
    board = (f"{separator_centered}\n"
             f"{row1}\n"
             f"{separator_centered}\n"
             f"{row2}\n"
             f"{separator_centered}\n"
             f"{row3}\n"
             f"{separator_centered}\n")
    
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return "X"
    else: return "O"

def check_winner(spots):
    win_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # řádky
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # sloupce
        (1, 5, 9), (3, 5, 7)  # diagonály
    ]
    
    for combo in win_combinations:
        a, b, c = combo
        if spots[a] == spots[b] == spots[c] and spots[a] in {"X", "O"}:
            return spots[a]  # Vrátí "X" nebo "O", pokud je vítěz
    return None  # Žádný vítěz

