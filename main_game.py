from def_helpers import draw_board, check_turn
import os

spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 
         6:"6", 7:"7", 8:"8", 9:"9"}

playing = True
turn = 0
prev_turn = -1

while playing:
    # resetuj obrazovku
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')

    draw_board(spots)

    if prev_turn == turn:
        print("Invalid choice. Please select a free spot from 1 to 9.")
    prev_turn = turn
    current_player = check_turn(turn)
    print(f"Player {current_player} | Please enter your move number or press 'q' to quit")

    # input od uzivatele
    choice = input()
    if choice == "q":
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = check_turn(turn)