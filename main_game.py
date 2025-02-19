"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Romana Bělohoubková
email: romanabelohoubkova@gmail.com
discord: Romana.B
"""

from def_helpers import draw_board, check_turn, check_winner
import os

spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 
         6:"6", 7:"7", 8:"8", 9:"9"}

separator_simple = "-" * 67
separator_double = "=" * 67
m_welcome = "Welcome to Tic Tac Toe".center(len(separator_double))
m_lets_start = "Let's start the game!".center(len(separator_double))

playing = True
turn = 0
prev_turn = -1


while playing:
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')

    message = (
        f"{m_welcome}\n"
        f"{separator_double}\n"
        "GAME RULES:\n"
        "Each player can place one mark (or stone) per turn on the 3x3 grid.\n"
        "The WINNER is who succeeds in placing three of their marks in a:\n"
        "  * horizontal,\n"
        "  * vertical, or\n"
        "  * diagonal row\n"
        f"{separator_double}\n"
        f"{m_lets_start}\n"
        f"{separator_simple}\n"
    )
    print(message)

    draw_board(spots)

    if prev_turn == turn:
        print("Invalid choice. Please select a free spot from 1 to 9.")

    prev_turn = turn
    current_player = check_turn(turn)

    m_who_plays = f"Player {current_player} | Please enter your move number or press 'q' to quit".center(len(separator_simple))
    
    print(f"{separator_simple}\n"
          f"{m_who_plays}\n"
          f"{separator_simple}\n")

    choice = input()
    if choice.lower() == "q":
        playing = False
        break

    elif choice.isdigit() and (spot := int(choice)) in spots:
        if spots[spot] not in ("X", "O"):
            spots[int(choice)] = current_player

            winner = check_winner(spots)

            if winner:
                draw_board(spots)
                print(
                    f"{separator_double}\n"
                    f"Congratulation! The player {winner} WON!\n"
                    f"{separator_double}"
                    )
                playing = False 
                break

            elif turn == 8:
                draw_board(spots)
                print(
                    f"{separator_double}\n"
                    "It's a draw! No one wins.\n"
                    f"{separator_double}"
                    )
                playing = False
                break

            turn += 1

            
