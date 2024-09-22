# There are small problems with the winner output, I will fix it a little later

board_ = dict.fromkeys([i for i in range(1, 10)], ' ')
print(board_)


class Board:
    def __init__(self) -> None:
        self.board = board_

    def print_board(self):
        for i in range(3):
            for j in range(3):
                key = 3 * i + j + 1
                value = self.board[key] if self.board[key] != 0 else ' '

                if j != 2:
                    print(f' {value} |', end='')
                else:
                    print(f' {value} ', end='')

            if i != 2:
                print('\n ---------')
        print()


class Game:
    def __init__(self, player='x', win_player=None) -> None:
        self.board = board_
        self.player = player
        self.win_player = win_player

    def plaing(self) -> None:
        cord = input('Введите номер клетки:').lower().strip()
        cord = int(cord)

        if not int(cord):
            print(f'{cord} - не является числом')
            return

        if not 1 <= cord <= 9:
            print(f'Клетки {cord} не существует')
            return

        if self.board[cord] == ' ':
            self.board[cord] = self.player
            self.player = 'o' if self.player == 'x' else 'x'
            self.win_player = 'x' if self.player == 'x' else 'o'
        else:
            print(f'Клетка {cord} - уже занята')

    def check_win(self) -> bool:
        for i in range(3):
            if self.board[3 * i + 1] == self.board[3 * i + 2] == self.board[3 * i + 3] != ' ':
                return True
            elif self.board[i + 1] == self.board[i + 4] == self.board[i + 7] != ' ':
                return True

        if self.board[1] == self.board[5] == self.board[9] != ' ':
            return True

        elif self.board[3] == self.board[5] == self.board[7] != ' ':
            return True
        return False


def main():
    board = Board()
    game = Game('x')

    board.print_board()
    while not game.check_win():
        game.plaing()

        if game.check_win():
            print(f'{game.player} - победитель')
            board.print_board()
            break

        board.print_board()

    else:
        print('Ничья')


if __name__ == '__main__':
    main()
