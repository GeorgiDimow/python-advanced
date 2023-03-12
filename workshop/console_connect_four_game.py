ROW_LEN, COL_LEN = 6, 7
win_connect = 4
playing_field = [[0 for _ in range(COL_LEN)] for _ in range(ROW_LEN)]

last_update_cord = ()
wining_player = None


def update_playing_field(col, player):
    for row in range(ROW_LEN):
        if playing_field[row][col] == 0:
            playing_field[row][col] = player
            return row, col
        else:
            continue


def validate_win(row, col):
    pos_dic = {
        "horizontal": (0, 1, 0, -1),
        "vertical": (1, 0, -1, 0),
        "right_diag": (1, 1, -1, 1),
        "left_diag": (1, -1, -1, -1),
    }
    for pos in pos_dic.keys():
        curr_pos = [playing_field[row][col]]
        x = row
        y = col
        x1 = row
        y1 = col
        for _ in range(win_connect-1):
            x += pos_dic[pos][0]
            y += pos_dic[pos][1]
            if 0 <= x < ROW_LEN and 0 <= y < COL_LEN:
                curr_pos.append(playing_field[x][y])
            x1 += pos_dic[pos][2]
            y1 += pos_dic[pos][3]
            if 0 <= x1 < ROW_LEN and 0 <= y1 < COL_LEN:
                curr_pos.append(playing_field[x][y])

        if len(set(curr_pos)) == 1 and len(curr_pos) == win_connect:
            return curr_pos.pop()


while True:
    for i in range(1, 3, 1):
        print(f"Player {i}, please choose a column")
        # try:
        column = int(input())
        last_update_cord = update_playing_field(column, i)
        wining_player = validate_win(*last_update_cord)
        print(*playing_field[::-1], sep="\n")
        if wining_player:
            break
        # except IndexError:
        #     print("The column must be between 1-7.")
        # except TypeError:
        #     print("The column is full.")
    if wining_player:
        print(f"The winner is {wining_player}")
        break
