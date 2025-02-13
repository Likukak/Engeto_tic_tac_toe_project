
def draw_board(spots):
    separator = "+---+---+---+"
    board = (f"{separator}\n"
             f"| {spots[1]} | {spots[2]} | {spots[3]} |\n"
             f"{separator}\n"
             f"| {spots[4]} | {spots[5]} | {spots[6]} | \n"
             f"{separator}\n"
             f"| {spots[7]} | {spots[8]} | {spots[9]} | \n"
             f"{separator}\n")
    
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return "O"
    else: return "X"