from termcolor import colored


class SudokuBoard:
    """
    This class contains the board object, with methods pertaining to the board. This
    class contains methods to check win conditions, the brute force solver, and the main
    command line driver code.
    """

    def __init__(self, difficulty):
        """
        Sets the board based on chosen difficulty level or mode chosen.
        :param difficulty: The difficulty or mode chosen options: Easy, Medium, Hard, Verify, Brute Force
        """
        self.difficulty = difficulty
        self.game_won = False
        if self.difficulty == "Easy":

            self.board_print = [
                [0, colored(8, 'blue'), 0, 0, colored(1, 'blue'), colored(3, 'blue'), colored(4, 'blue'), 0, 0],
                [colored(4, 'blue'), colored(2, "blue"), 0, colored(6, 'blue'), colored(8, "blue"), 0, 0, 0, 0],
                [0, 0, colored(1, "blue"), 0, colored(5, "blue"), colored(4, 'blue'), 0, colored(8, 'blue'),
                 colored(3, "blue")],
                [colored(1, 'blue'), colored(9, 'blue'), 0, 0, 0, colored(8, "blue"), colored(7, "blue"), 0, 0],
                [0, colored(4, 'blue'), colored(7, 'blue'), 0, 0, colored(2, 'blue'), colored(5, 'blue'), 0,
                 colored(8, 'blue')],
                [0, colored(5, "blue"), 0, 0, 0, colored(9, "blue"), 0, colored(3, "blue"), 0],
                [colored(2, "blue"), 0, colored(9, "blue"), colored(3, "blue"), 0, colored(5, "blue"), 0,
                 colored(7, "blue"), 0],
                [colored(5, "blue"), 0, 0, colored(7, "blue"), colored(2, "blue"), 0, 0, 0, colored(9, "blue")],
                [colored(7, "blue"), colored(3, "blue"), 0, 0, 0, 0, colored(2, "blue"), 0, colored(6, "blue")]]

            self.board = [
                [0, 8, 0, 0, 1, 3, 4, 0, 0],
                [4, 2, 0, 6, 8, 0, 0, 0, 0],
                [0, 0, 1, 0, 5, 4, 0, 8, 3],
                [1, 9, 0, 0, 0, 8, 7, 0, 0],
                [0, 4, 7, 0, 0, 2, 5, 0, 8],
                [0, 5, 0, 0, 0, 9, 0, 3, 0],
                [2, 0, 9, 3, 0, 5, 0, 7, 0],
                [5, 0, 0, 7, 2, 0, 0, 0, 9],
                [7, 3, 0, 0, 0, 0, 2, 0, 6]]

            self.banned_moves = [(0, 1), (0, 4), (0, 5), (0, 6),
                                 (1, 0), (1, 1), (1, 3), (1, 4),
                                 (2, 2), (2, 4), (2, 5), (2, 7), (2, 8),
                                 (3, 0), (3, 1), (3, 5), (3, 6),
                                 (4, 1), (4, 2), (4, 5), (4, 6), (4, 8),
                                 (5, 1), (5, 5), (5, 7),
                                 (6, 0), (6, 2), (6, 3), (6, 5), (6, 7),
                                 (7, 0), (7, 3), (7, 4), (7, 8),
                                 (8, 0), (8, 1), (8, 6), (8, 8)]

            self.play_game()

        elif self.difficulty == "Medium":

            self.board = [
                [7, 0, 0, 8, 0, 9, 0, 0, 6],
                [0, 0, 1, 7, 0, 0, 0, 0, 9],
                [2, 0, 0, 0, 5, 0, 0, 0, 1],
                [9, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 5, 0, 0, 0, 0, 4, 2, 0],
                [4, 3, 0, 0, 7, 8, 0, 0, 0],
                [8, 6, 0, 0, 9, 0, 1, 0, 2],
                [3, 0, 4, 0, 0, 6, 0, 0, 0],
                [1, 0, 0, 0, 8, 0, 0, 6, 0]]

            self.board_print = [
                [colored(7, 'blue'), 0, 0, colored(8, "blue"), 0, colored(9, "blue"), 0, 0, colored(6, "blue")],
                [0, 0, colored(1, "blue"), colored(7, "blue"), 0, 0, 0, 0, colored(9, 'blue')],
                [colored(2, "blue"), 0, 0, 0, colored(5, "blue"), 0, 0, 0, colored(1, "blue")],
                [colored(9, "blue"), 0, 0, 0, 0, 0, 0, 0, 0],
                [colored(6, "blue"), colored(5, "blue"), 0, 0, 0, 0, colored(4, "blue"), colored(2, "blue"), 0],
                [colored(4, "blue"), colored(3, "blue"), 0, 0, colored(7, "blue"), colored(8, "blue"), 0, 0, 0],
                [colored(8, "blue"), colored(6, "blue"), 0, 0, colored(9, "blue"), 0, colored(1, "blue"), 0,
                 colored(2, "blue")],
                [colored(3, "blue"), 0, colored(4, "blue"), 0, 0, colored(6, "blue"), 0, 0, 0],
                [colored(1, "blue"), 0, 0, 0, colored(8, "blue"), 0, 0, colored(6, "blue"), 0]]

            self.banned_moves = [
                (0, 0), (0, 5), (0, 8),
                (1, 2), (1, 3), (1, 8),
                (2, 0), (2, 4), (1, 8),
                (3, 0),
                (4, 0), (4, 1), (4, 6), (4, 7),
                (5, 0), (5, 1), (5, 4), (5, 5),
                (6, 0), (6, 1), (6, 4), (6, 6), (6, 8),
                (7, 0), (7, 2), (7, 5),
                (8, 0), (8, 4), (8, 7)]

            self.play_game()

        elif self.difficulty == "Hard":

            self.board = [
                [0, 9, 0, 7, 0, 1, 0, 0, 0],
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 6, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 9, 5, 0, 0, 7],
                [6, 0, 8, 0, 4, 0, 0, 9, 0],
                [8, 0, 0, 3, 0, 0, 7, 0, 0],
                [0, 0, 4, 0, 5, 0, 0, 0, 2],
                [0, 2, 9, 0, 0, 0, 0, 5, 8]]

            self.board_print = [
                [0, colored(9, "blue"), 0, colored(7, "blue"), 0, colored(1, "blue"), 0, 0, 0],
                [0, 0, 0, colored(4, "blue"), 0, 0, 0, 0, 0],
                [colored(7, "blue"), 0, 0, 0, 0, colored(6, "blue"), 0, 0, 0],
                [0, colored(1, "blue"), 0, 0, 0, 0, 0, 0, colored(4, "blue")],
                [0, 0, 0, 0, colored(9, "blue"), colored(5, "blue"), 0, 0, colored(7, "blue")],
                [colored(6, "blue"), 0, colored(8, "blue"), 0, colored(4, "blue"), 0, 0, colored(9, "blue"), 0],
                [colored(8, "blue"), 0, 0, colored(3, "blue"), 0, 0, colored(7, "blue"), 0, 0],
                [0, 0, colored(4, "blue"), 0, colored(5, "blue"), 0, 0, 0, colored(2, "blue")],
                [0, colored(2, "blue"), colored(9, "blue"), 0, 0, 0, 0, colored(5, "blue"), colored(8, "blue")]]

            self.banned_moves = [
                (0, 1), (0, 3), (0, 5),
                (1, 3),
                (2, 0), (2, 5),
                (3, 1), (3, 8),
                (4, 4), (4, 5), (4, 8),
                (5, 0), (5, 2), (5, 4), (5, 7),
                (6, 0), (6, 3), (6, 6),
                (7, 2), (7, 4), (7, 8),
                (8, 1), (8, 2), (8, 7), (8, 8)]

            self.play_game()
        elif self.difficulty == "Brute Force":

            self.board = [
                [0, 8, 0, 0, 1, 3, 4, 0, 0],
                [4, 2, 0, 6, 8, 0, 0, 0, 0],
                [0, 0, 1, 0, 5, 4, 0, 8, 3],
                [1, 9, 0, 0, 0, 8, 7, 0, 0],
                [0, 4, 7, 0, 0, 2, 5, 0, 8],
                [0, 5, 0, 0, 0, 9, 0, 3, 0],
                [2, 0, 9, 3, 0, 5, 0, 7, 0],
                [5, 0, 0, 7, 2, 0, 0, 0, 9],
                [7, 3, 0, 0, 0, 0, 2, 0, 6]]

            self.board_print = self.board

            self.banned_moves = [(0, 1), (0, 4), (0, 5), (0, 6),
                                 (1, 0), (1, 1), (1, 3), (1, 4),
                                 (2, 2), (2, 4), (2, 5), (2, 7), (2, 8),
                                 (3, 0), (3, 1), (3, 5), (3, 6),
                                 (4, 1), (4, 2), (4, 5), (4, 6), (4, 8),
                                 (5, 1), (5, 5), (5, 7),
                                 (6, 0), (6, 2), (6, 3), (6, 5), (6, 7),
                                 (7, 0), (7, 3), (7, 4), (7, 8),
                                 (8, 0), (8, 1), (8, 6), (8, 8)]

            game_obj = SudokuGame(self)
            self.brute_force_method(game_obj)
            self.print_board()

        elif self.difficulty == "Verify":
            n = 81

            # citation: https://pynative.com/python-accept-list-input-from-user/#h-input-a-list-using-input-and-range-function
            num_list = list(int(num) for num in input("Enter a Sudoku Board ").strip().split())[:n]

            if len(num_list) < 81:
                print("No, this is not a valid solution.")
            else:
                # citation: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
                self.board = [num_list[x:x + 9] for x in range(0, len(num_list), 9)]
                self.board_print = self.board
                self.print_board()

                print(self.check_win())

    def play_game(self):
        """
        Main driver code for the command line game. The function contains all of the
        commands that are asked of the player until the game is won.
        :return:
        """
        self.game_won = False
        temp = self
        print("Ok, here's your board.")
        temp.print_board()
        print("Fill in the blanks to win the game")
        print("Pass an argument by entering row, column, and value")

        game_obj = SudokuGame(self.board)

        while self.game_won is False:
            while True:
                try:
                    row = int(input("What row? "))
                    col = int(input("what column? "))
                    value = int(input("What value? "))
                    game_obj.add_value(row, col, value, self)
                    print(self.puzzle_complete())
                    print(self.check_win())
                    temp.print_board()
                except:
                    print("Those were not valid inputs")
                else:
                    break

    def get_squares(self, row, col):
        """
        Returns the subgrid a passed cell belongs to. Used to check whether the intended
        value is already present in the subgrid.
        :param row: Row of the cell to be changed
        :param col: Column of the cell to be changed
        :return: Tuple
        """
        if row <= 2:
            if col <= 2:
                return (0, 2), (0, 2)
            elif col <= 5:
                return (0, 2), (3, 5)
            else:
                return (0, 2), (6, 8)
        elif row <= 5:
            if col <= 2:
                return (3, 5), (0, 2)
            elif col <= 5:
                return (3, 5), (3, 5)
            else:
                return (3, 5), (6, 8)
        else:
            if col <= 2:
                return (6, 8), (0, 2)
            elif col <= 5:
                return (6, 8), (3, 5)
            else:
                return (6, 8), (6, 8)

    def is_move_legal(self, game_obj, row, col, value):
        """
        Calls several functions to determine whether a potential move is legal
        :param game_obj: SudokuGame object
        :param row: row to be altered
        :param col: column to be altered
        :param value: value to insert in [row][column]
        :return: True False
        """
        if game_obj.check_row(row, value, self) is True:
            if game_obj.check_col(col, value, self) is True:
                square = self.get_squares(row, col)
                if game_obj.check_square(square, value, self) is True:
                    return True
        return False

    def empties(self):
        """
        Helper Function for Brute_Force_Method. When the board has been filled this function signals the end of
        the recursive calls.
        :return: List of tuples
        """
        empties = []
        for i in range(9):
            for x in range(9):
                if self.board[i][x] == 0:
                    empties.append((i, x))
        return empties

    def brute_force_method(self, game_obj):
        """
        This function builds a solution to the sudoku board using backtracking method.
        :param game_obj: SudokuGame object
        :return: None
        """
        for i in range(9):
            for x in range(9):
                if self.board[i][x] == 0:
                    for num in range(1, 10):
                        if self.is_move_legal(game_obj, i, x, num) is True:
                            self.board[i][x] = num
                            result = self.brute_force_method(game_obj)
                            empties = self.empties()
                            if len(empties) == 0:
                                break
                            else:
                                self.board[i][x] = 0
                    return False
        return True

    def print_board(self):
        """
        This function prints the board through the game. Formatting citation provided below.
        :return: printed board representation.
        """
        # citation: https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
        iter = 0
        print("|" + "---+" * 8 + "---|")
        for i in self.board_print:
            print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in i]))
            if iter == 8:
                print("|" + "---+" * 8 + "---|")
            elif iter % 3 == 2:
                print("|" + "---+" * 8 + "---|")
            else:
                print("|" + "   +" * 8 + "   |")
            iter += 1

    def update_board(self, row, col, val):
        """
        When the SudokuGame class determines that a potential move is legal this function updated
        the game board and the human-readable printed board.
        :param row: The row to be upated
        :param col: Column to be updated
        :param val: The value to be inserted at the [row][column] position
        :return: None
        """

        self.board[row][col] = val
        self.board_print[row][col] = val

    def get_board_value(self, row, col):
        """
        Returns the value at a given [row][column] location.
        :param row: The row to be checked.
        :param col: The column to be checked.
        :return: Value at [row][column] location.
        """
        return self.board[row][col]

    def puzzle_complete(self):
        """
        This function determines whether the sudoku grid has been filled and if so runs
        a check for win conditions.
        :return: String or calls check_win()
        """
        check_val = 0
        for i in self.board:
            if check_val in i:
                return "Ready for next guess"

        return self.check_win()

    def check_win(self):
        """
        Checks whether a filled board represents a valid solution.
        :return: String
        """
        # check that the board is completely filled
        for i in self.board:
            row = i
            for x in row:
                if x == 0:
                    return

        # check if no values are repeated in any row
        for i in self.board:
            used_nums = []
            row = i
            for num in row:
                if num not in used_nums:
                    used_nums.append(num)
                elif num in used_nums:
                    return "This is not a valid solution"

            # check for no repeated nums in cols
        cols = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for col in cols:
            used_nums = []
            for x in range(9):
                temp_val = self.board[col][x]
                if temp_val not in used_nums:
                    used_nums.append(temp_val)
                elif temp_val in used_nums:
                    return "This is not a valid solution"

        # check for repeated nums in sub-grid

        sub1 = self.board[0:3]
        temp = []
        for i in sub1:
            i = i[0:3]
            temp.append(i)
        sub1 = temp

        sub2 = self.board[0:3]
        temp = []
        for i in sub2:
            i = i[3:6]
            temp.append(i)
        sub2 = temp

        sub3 = self.board[0:3]
        temp = []
        for i in sub3:
            i = i[6:9]
            temp.append(i)
        sub3 = temp

        sub4 = self.board[3:6]
        temp = []
        for i in sub4:
            i = i[0:3]
            temp.append(i)
        sub4 = temp

        sub5 = self.board[3:6]
        temp = []
        for i in sub5:
            i = i[3:6]
            temp.append(i)
        sub5 = temp

        sub6 = self.board[3:6]
        temp = []
        for i in sub6:
            i = i[6:9]
            temp.append(i)
        sub6 = temp

        sub7 = self.board[6:9]
        temp = []
        for i in sub7:
            i = i[0:3]
            temp.append(i)
        sub7 = temp

        sub8 = self.board[6:9]
        temp = []
        for i in sub8:
            i = i[3:6]
            temp.append(i)
        sub8 = temp

        sub9 = self.board[6:9]
        temp = []
        for i in sub9:
            i = i[6:9]
            temp.append(i)
        sub9 = temp

        sub_grids = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9]

        for grid in sub_grids:
            used_nums = []
            for num in grid:
                if num not in used_nums:
                    used_nums.append(num)
                elif num in used_nums:
                    return "This is not a valid Solution"

        self.game_won = True
        print("You've won the game!")




class SudokuGame:
    """
    This class contains all the logic to actually play the sudoku game.
    """

    def __init__(self, board):
        """
        Takes as argument a SudodkuBoard object.
        :param board:
        """
        self.board = board

    def input_validations(self, row, col, value, board_obj):
        """
        This function validates that the passed row, col, and value are valid
        :param row: The row to be checked
        :param col: The column to be checked
        :param value: The value to be checked
        :param board_obj: The SudokuBoard object.
        :return: True or False
        """

        if value <= 9 and row <= 9 and col <= 9:
            temp_tup = (row, col)
            if temp_tup not in board_obj.banned_moves:
                return True
            else:
                return False
        else:
            return False

    def add_value(self, row, col, value, board_obj):
        """
        This function updates the Sudokuboard with the valid move.
        :param row: The row to be updated
        :param col: The col to be updated
        :param value: The value to be inserted at [row][col] position.
        :param board_obj: SudokuBoard object.
        :return: True or String
        """
        square = board_obj.get_squares(row,col)

        if self.input_validations(row, col, value, board_obj) is True:
            if board_obj.is_move_legal(self,row,col,value) is True:
                board_obj.update_board(row, col, value)
                return True
            else:
                print("Try another value")
        else:
            print("Try another value between 0-9")

    def check_row(self,row, val, board_obj):
        """
        Checks whether the proposed value already occurs in the row
        :param row: The row to be checked
        :param val: The value to be checked
        :param board_obj: SudokuBoard object
        :return: True or False
        """
        used_nums = []

        for i in range(9):
            temp_val = board_obj.get_board_value(row, i)
            if temp_val == 0:
                pass
            else:
                if temp_val not in used_nums:
                    used_nums.append(temp_val)
        if val in used_nums:
            return False
        else:
            return True

    def check_col(self, col, val, board_obj):
        """
        :Checks whether the proposed value already occurs in the column
        :param col: The col to be checked
        :param val: The value to be checked
        :param board_obj: SudokuBoard object
        :return: True or False
        """
        used_nums = []

        for i in range(9):
            temp_val = board_obj.get_board_value(i, col)
            if temp_val == 0:
                pass
            else:
                if temp_val not in used_nums:
                    used_nums.append(temp_val)

        if val in used_nums:
            return False
        else:
            return True

    def check_square(self, square, val, board_obj):
        """
        Checks whether the proposed value already occurs in the subgrid
        :param square: The tuple representation the subgrid
        :param val: The value to be checked
        :param board_obj: SudokuBoard object
        :return: True or False
        """

        used_nums = []
        rows = square[0]
        cols = square[1]

        for i in range(rows[0], rows[1] + 1):
            for y in range(cols[0], cols[1] + 1):
                temp_val = board_obj.get_board_value(i, y)
                if temp_val == 0:
                    pass
                elif temp_val not in used_nums:
                    used_nums.append(temp_val)
        if val in used_nums:
            return False
        else:
            return True


def diff_level_function():
    """
    Runs automatically when the program is run. Prompt's the user for a valid difficulty and
    calls the SudokuGame and SudokuBoard classes so that the game cab be played
    :return: None
    """
    diff_level = input("Easy, Medium, Hard, Brute Force, or Verify? ")

    if diff_level == "Easy" or diff_level == "easy":
        game = SudokuBoard("Easy")
    elif diff_level == "Medium" or diff_level == "medium":
        game = SudokuBoard("Medium")
    elif diff_level == "Hard" or diff_level == "hard":
        game = SudokuBoard("Hard")
    elif diff_level == "Brute Force" or diff_level == "brute force":
        game = SudokuBoard("Brute Force")
    elif diff_level == "Verify" or diff_level == "Verify":
        game = SudokuBoard("Verify")
    else:
        print("You'll need to enter a difficulty level")
        diff_level_function()


diff_level_function()
