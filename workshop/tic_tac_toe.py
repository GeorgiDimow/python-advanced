def start():
    player_one_name = input("Player one enter your name: ")
    player_one_name = input("Player two enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'?").upper()
        if player_one_symbol not in "XO":
            print(f"{player_one_name} select a valid option")
        else:
            break



size = 3
playing_field = [[str(i), str(i+1), str(i+2)] for i in range(1, 10, 3)]

players = []
print(playing_field)