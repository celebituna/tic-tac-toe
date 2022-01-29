from distutils.log import debug
from pyfiglet import figlet_format


class Board:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [str(x+1) for x in range(9)]

    def showBoard(self):
        print("|".join((self.board[:3])))
        print("|".join(self.board[3:6]))
        print("|".join(self.board[6:9]))
        print("\n\n")

    def updateBoard(self, player1, player2):
        players = [player1, player2]
        for player in players:
            count = 0
            for step in player.step:
                if step != '-':
                    self.board[count] = step
                elif self.board[count] != 'O' and self.board[count] != 'X':
                    self.board[count] = '-'
                count += 1


class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name
        self.step = ["-" for x in range(9)]

    def updateStep(self, idx):
        self.step[idx] = self.symbol

    def sumStep(self):
        arrMultiply = [2, 7, 6, 9, 5, 1, 4, 3, 8]
        total = 0
        for x in range(9):
            if self.step[x] != '-':
                total += arrMultiply[x]
        return total

    def isWinner(self):
        return self.sumStep() == 15


class Game:
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.board = None

    def startGame(self):
        print(figlet_format("Welcome Tic-Tac-Toe GAME", font="standard"))
        print("This is the best ever Tic-Tac-Toe game created. Enjoy it...\n\n")
        print("""Tic-Tac-Toe is played on a three-by-three grid by two players, who alternately place
the marks X and O in one of the nine spaces in the grid.
Who first take horizantal, vertical or cross three spaces is the Winner.\n""")
        mark = input("Player1 select your mark. 'X' or 'O': ")
        self.p1 = Player('Player 1', mark)
        if self.p1.symbol == 'X':
            self.p2 = Player('Computer', 'O')
        else:
            self.p2 = Player('Computer', 'X')
        print(
            f"\nPlayer1 select {self.p1.symbol} mark. Computer select {self.p2.symbol}")
        print(f"Player1 firs move is yours. Please select 1 to 9 as shown below\n")
        self.board = Board(self.p1, self.p2)
        self.board.showBoard()

    def isGamefinish(self):
        for x in self.board.board:
            if x == '-':
                return False
        return True

    def play(self):
        turn = self.p1
        self.board.updateBoard(self.p1, self.p2)
        while not self.isGamefinish():
            while True:
                idx = int(
                    input(f"{turn.name} move is yours. Please select 1 to 9 as shown above: "))
                try:
                    if self.board.board[idx-1] == '-':
                        turn.updateStep(idx-1)
                        break
                    else:
                        print('This space is marked. Choose another one')
                        self.board.showBoard()
                except:
                    print("Please select in a range 1 to 9")

            if turn.isWinner():
                print(f"{turn.name} is winner. Game over!")
                self.board.showBoard()
                return
            self.board.updateBoard(self.p1, self.p2)
            self.board.showBoard()
            if turn == self.p1:
                turn = self.p2
            else:
                turn = self.p1
            print(self.isGamefinish())
        print("Game is finish. No Winner!")


g = Game()
g.startGame()
g.play()

# p1 = Player("X")
# p2 = Player("O")
# p2.updateStep(2)
# p1.updateStep(5)
# b = Board(p1, p2)
# b.showBoard()
# b.updateBoard(p1, p2)
# b.showBoard()
