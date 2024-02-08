import copy
from unittest import TestCase


class Board_Domain:
    def __init__(self):
        self.__board = [-1] * 24
        self.__adj = {0: (1, 9), 1: (0, 2, 4), 2: (1, 14), 3: (4, 10), 4: (1, 3, 5, 7), 5: (4, 13), 6: (7, 11),
                       7: (4, 6, 8), 8: (7, 12), 9: (0, 21, 10), 10: (3, 9, 11, 18), 11: (6, 10, 15), 12: (8, 13, 17),
                       13: (5, 12, 14, 20), 14: (2, 13, 23), 15: (11, 16), 16: (15, 17, 19), 17: (12, 16),
                       18: (10, 19), 19: (16, 18, 20, 22), 20: (13, 19), 21: (9, 22), 22: (19, 21, 23), 23: (14, 22)}
        self.__posible_mills = [[0 , 1 , 2] , [3 , 4 , 5] , [6 , 7 , 8]  , [9 , 10 , 11] , [12 , 13 , 14] , [15 , 16 , 17] ,
                                [18 , 19 , 20] , [21 , 22 , 23] , [0 , 9 , 21] , [3 , 10 , 18] , [6 , 11 , 15] , [8 , 12 , 17] ,
                                [5 , 13 , 20] , [2 , 14 , 23] , [1 , 4 , 7] , [16 , 19 , 22]]

    def place_on_board(self , pos , c_or_p):
        """
        Places a piece on the board on a certain position
        :param pos: the position
        :param c_or_p: computer means 0 , player means 1
        :return:
        """
        self.__board[pos] = c_or_p

    def __str__(self):
        """
        Function to display the board nicely
        :return:
        """
        board = copy.deepcopy(self.__board)
        for i in range(0, len(board)):
            if board[i] == -1:
                board[i] = "None"
            elif board[i] == 1:
                board[i] = "You "
            elif board[i] == 0:
                board[i] = "AI  "



        return (
            '                    [0]{}---------------------------------------[1]{}-----------------------------------------[2]{}\n'
            '                     |                                             |                                                |\n'
            '                     |                                             |                                                |\n'
            '                     |            [3]{}-------------------------[4]{}-------------------------[5]{}           |\n'
            '                     |             |                               |                               |                |\n'
            '                     |             |                               |                               |                |\n'
            '                     |             |              [6]{}---------[7]{}---------[8]{}          |                |\n'
            '                     |             |                |                              |               |                |\n'
            '                     |             |                |                              |               |                |\n'
            '                    [9]{}-------[10]{}-------[11]{}                         [12]{}--------[13]{}------[14]{}\n'
            '                     |             |                |                              |               |                |\n'
            '                     |             |                |                              |               |                |\n'
            '                     |             |             [15]{}--------[16]{}--------[17]{}          |                |\n'
            '                     |             |                               |                               |                |\n'
            '                     |             |                               |                               |                |\n'
            '                     |            [18]{}-----------------------[19]{}------------------------[20]{}           |\n'
            '                     |                                             |                                                |\n'
            '                     |                                             |                                                |\n'
            '                    [21]{}-------------------------------------[22]{}-----------------------------------------[23]{}\n'.format(board[0], board[1],
                                                                                              board[2], board[3],
                                                                                              board[4], board[5],
                                                                                              board[6], board[7],
                                                                                              board[8], board[9],
                                                                                              board[10], board[11],
                                                                                              board[12],
                                                                                              board[13], board[14],
                                                                                              board[15], board[16],
                                                                                              board[17], board[18],
                                                                                              board[19]
                                                                                              , board[20], board[21],
                                                                                              board[22], board[23]))

    def update(self , pos , i):
        """
        Function to update a certain position from the board
        :param pos: the position
        :param i: the new value
        :return:
        """
        self.__board[pos] = i

    def get_pos(self , pos):
        """
        Function to get the value from a certain position
        :param pos: the position to get the value from
        :return: the value
        """
        return self.__board[pos]

    def get_board(self):
        """
        Function to return the entire board
        :return: the board
        """
        return self.__board

    def check_mill(self , pos , turn):
        """
        Function to check if we have a mill on a horizontal or vertical line
        :param pos: the position for which we want to check
        :param turn: to see if we have a human/ai mill
        :return: 1 if we have a mill / 0 otherwise
        """
        for i in self.__posible_mills:
            if pos in i:
                if self.__board[i[0]] == self.__board[i[1]] == self.__board[i[2]] == turn:
                    return 1
        return 0


    def check_pot_mill(self , pos , turn):
        """
        Function to check if we have two pieces of the same nature and an empty square on
        a horizontal or vertical line, so we can make in future a mill
        :param pos: the position for which we want to check
        :param turn: to see if we have a human/ai mill
        :return: 1 if we have a mill / 0 otherwise
        """
        for i in self.__posible_mills:
            if pos in i:
                if (self.__board[i[0]] == self.__board[i[1]] == turn and self.__board[i[2]] == -1) or\
                    (self.__board[i[0]] == self.__board[i[2]] == turn and self.__board[i[1]] == -1) or\
                     (self.__board[i[1]] == self.__board[i[2]] == turn and self.__board[i[0]] == -1):
                    return 1
        return 0

    def check_1piece_mill(self, pos, turn):
        """
           Function to check if we have one piece and two empty squares on
            a horizontal or vertical line, so we can make in future a mill
            :param pos: the position for which we want to check
            :param turn: to see if we have a human/ai mill
           :return: 1 if we have a mill / 0 otherwise
                """
        for i in self.__posible_mills:
            if pos in i:
                if (self.__board[i[0]] == turn and self.__board[i[2]]  == self.__board[i[1]] == -1) or \
                        (self.__board[i[2]] == turn and self.__board[i[1]] == self.__board[i[0]] ==  -1) or \
                        (self.__board[i[1]]  == turn and self.__board[i[0]] == self.__board[i[2]] == -1):
                    return 1
        return 0

    def remove_piece(self , pos):
        """
        Function to remove a piece from the board
        :param pos: The position from where to remove
        :return:
        """
        self.__board[pos] = -1

    def two_adj(self , pos1 , pos2):
        """
        Function to check if two positions are adiacent
        :param pos1: first position
        :param pos2: second position
        :return: 1 if they are adiacent, 0 otherwise
        """
        if pos2 in self.__adj[pos1]:
            return True
        return False

    def move_piece(self , pos1 , pos2):
        """
        Function to move a piece from a position to another position
        :param pos1: Initial position
        :param pos2: Final position
        :return:
        """
        self.__board[pos2] = self.__board[pos1]
        self.__board[pos1] = -1

    def can_be_moved(self , pos):
        """
        Function to see if a piece can be moved
        :param pos: the position of the piece
        :return: 1 if the piece can be moved, 0 otherwise
        """
        for i in self.__adj[pos]:
            if self.__board[i] == -1:
                return True
        return False

    def is_board_won(self):
        """
        Function to check if the board is won
        :return: 1 if the board is won, 0 otherwise
        """
        ai_pieces = 0
        you_pieces = 0
        for i in range(0 , 24):
            if self.__board[i] == 1:
                you_pieces = you_pieces + 1
            if self.__board[i] == 0:
                ai_pieces = ai_pieces + 1
        if ai_pieces < 3 or you_pieces < 3:
            return 1


        return 0

    def only_3_pieces(self , val):
        """
        Function to check if we have only 3 pieces f
        :param val:
        :return:
        """
        nr = 0
        for i in range(0 , 24):
            if self.__board[i] == val:
                nr = nr + 1
        if nr == 3:
            return 1
        return 0

    def get_adj(self , pos):
        """
        Function to get all the adiacent positions
        :param pos: the position for which to get the adiacent positions
        :return: all the adiacent position
        """
        return self.__adj[pos]


class Test_Board_Domain_Functions(TestCase):

    def test_place_on_board(self):
        board = Board_Domain()
        board.place_on_board(1 , 0)
        assert board.get_pos(1) == 0
        self.assertEqual(board.get_pos(1) , 0)

    def test_update(self):
        board = Board_Domain()
        board.update(1 , 1)
        assert board.get_pos(1) == 1

    def test_get_pos(self):
        board = Board_Domain()
        assert board.get_pos(1) == -1

    def test_get_board(self):
        board = Board_Domain()
        board2 = [-1] * 24
        assert board2 == board.get_board()

    def test_check_mill(self):
        board = Board_Domain()
        board.place_on_board(0 , 1)
        board.place_on_board(1, 1)
        board.place_on_board(2, 1)

        assert board.check_mill(0 , 1) == 1
        assert board.check_mill(1, 1) == 1
        assert board.check_mill(2, 1) == 1

    def test_check_pot_mill(self):
        board = Board_Domain()
        board.place_on_board(0 , 1)
        board.place_on_board(1, 1)

        assert board.check_pot_mill(0 , 1) == 1
        assert board.check_pot_mill(1, 1) == 1
        assert board.check_pot_mill(2, 1) == 1

    def test_check_1piece_mill(self):
        board = Board_Domain()
        board.place_on_board(0, 1)

        assert board.check_1piece_mill(0, 1) == 1
        assert board.check_1piece_mill(1, 1) == 1
        assert board.check_1piece_mill(2, 1) == 1
        assert board.check_1piece_mill(9, 1) == 1
        assert board.check_1piece_mill(21, 1) == 1

    def test_remove_piece(self):
        board = Board_Domain()
        board.place_on_board(0, 1)
        board.remove_piece(0)

        assert board.get_pos(0) == -1
    def test_remove_piece(self):
        board = Board_Domain()
        board.place_on_board(0, 1)
        board.remove_piece(0)

        assert board.get_pos(0) == -1
    def test_two_adj(self):
        board = Board_Domain()

        assert board.two_adj(0, 5) == 0
        assert board.two_adj(0, 9) == 1

    def test_move_piece(self):
        board = Board_Domain()

        board.place_on_board(1 , 1)
        board.move_piece(1 , 2)

        assert board.get_pos(1) == -1
        assert board.get_pos(2) == 1

    def test_can_be_moved(self):
        board = Board_Domain()

        assert board.can_be_moved(1) == 1

    def test_is_board_won(self):
        board = Board_Domain()

        assert board.is_board_won() == 1

        board.place_on_board(1 , 0)
        board.place_on_board(2, 0)
        board.place_on_board(3, 0)

        board.place_on_board(10, 1)
        board.place_on_board(22, 1)
        board.place_on_board(13, 1)

        assert board.is_board_won() == 0

    def test_only3_pieces(self):
        board = Board_Domain()

        board.place_on_board(1, 0)
        board.place_on_board(2, 0)
        board.place_on_board(3, 0)

        assert board.only_3_pieces(0) == 1
        assert board.only_3_pieces(1) == 0

    def test_get_adj(self):
        board = Board_Domain()

        assert board.get_adj(0) == (1 , 9)

