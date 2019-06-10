def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        i=0
        while i<len(board):
            print(board[i],"",board[i+1],"",board[i+2])
            i=i+3

    def player1():
        n = choose_number()
        if board[n] == "+" or board[n] == "-":
            print("\nYou can't go there. Try again")
            player1()
        else:
            board[n] = "+"

    def player2():
        n = choose_number()
        if board[n] == "+" or board[n] == "-":
            print("\nYou can't go there. Try again")
            player2()
        else:
            board[n] = "-"

    def choose_number():
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check_board_state():
        count = 0
        for a in winning_combinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "+":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "-":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "+" or board[a] == "-":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True
        return False

    while not end:
        draw()
        end = check_board_state()
        if end == True:
            break
        print("Player 1 choose where to place a plus")
        player1()
        print()
        draw()
        end = check_board_state()
        if end == True:
            break
        print("Player 2 choose where to place a minus")
        player2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()
