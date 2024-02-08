import copy
from random import randint
from unittest import TestCase

from Nine_mens_morris.Board_Domain import Board_Domain


class Computer_Player:
    def __init__(self , board : Board_Domain):
        self.__board = board


    def move_phase1(self):
        """
        Function to make the computer choose a move depending on the board in the phase 1
        :return: the position to move, and 1 if the computer made a mill and 0 otherwise
        """
        pos_mill = self.make_ai_mill()
        if pos_mill == -1:
            block_mill = self.block_human_mill()
            if block_mill == -1:
                pot_mill = self.make_ai_pot_mill()
                if pot_mill == -1:
                    while True:
                        i = randint(0 , 23)
                        if self.__board.get_pos(i) == -1:
                            self.__board.place_on_board(i , 0)
                            return i , 0
                else:
                    return pot_mill , 0
            else:
                return block_mill , 0
        else:
            return pos_mill , 1

    def move_phase2(self):
        """
        Function to make the computer choose a move depending on the board in the phase 2
        :return: the position from where to move and the position where to move , and 1 if the computer made a mill and 0 otherwise
        """
        initial , last = self.move_to_form_a_mill_phase2()
        if initial != -1 and last != -1:
            self.__board.move_piece(initial , last)
            return initial , last , 1
        else:
            initial , last = self.move_to_block_a_human_mill_phase2()
            if initial != -1 and last != -1:
                self.__board.move_piece(initial, last)
                return initial, last , 0
            else:
                initial, last = self.move_from_ai_mill()
                if initial != -1 and last != -1:
                    self.__board.move_piece(initial, last)
                    return initial, last , 0
                else:
                    initial, last = self.move_from_random_position_phase2()
                    if initial != -1 and last != -1:
                        self.__board.move_piece(initial, last)
                        return initial, last , 0
        return -1 , -1 , 0

    def move_phase3(self):
        """
        Function to make the computer choose a move depending on the board in the phase 3
        :return: the position from where to move and the position where to move , and 1 if the computer made a mill and 0 otherwise
        """

        initial, last = self.move_to_form_a_mill_phase3()
        if initial != -1 and last != -1:
            self.__board.move_piece(initial, last)
            return initial, last, 1
        else:
            initial, last = self.move_to_block_a_human_mill_phase3()
            if initial != -1 and last != -1:
                self.__board.move_piece(initial, last)
                return initial, last, 0
            else:
                initial, last = self.move_from_random_position_phase3()
                if initial != -1 and last != -1:
                    self.__board.move_piece(initial, last)
                    return initial, last, 0
        return -1, -1, 0


    def move_to_form_a_mill_phase3(self):
        """
        Function to give the position for the computer to move in the best position in order to make a mill
        in phase 3 of the game
        :return: the initial position , and the final position
        """
        board2 = copy.deepcopy(self.__board)
        for i in range(0 , 24):
            if board2.get_pos(i) == 0:
                for j in range(0 , 24):
                    if board2.check_pot_mill(j , 0) == 1 and board2.get_pos(j) == -1:
                        board2.move_piece(i , j)
                        if board2.check_mill(j , 0) == 1:
                            return i , j
                        else:
                            board2.move_piece(j , i)
        return -1 , -1

    def move_to_block_a_human_mill_phase3(self):
        """
        Function to give the position for the computer to move in the best position in order to block a human mill
        in phase 3 of the game
        :return: the initial position , and the final position
        """
        nr = 0
        maxim = 1000
        maxi = -1
        maxj = -1
        for i in range(0, 24):
            if self.__board.get_pos(i) == 0:
                for j in range(0 , 24):
                    if self.__board.check_pot_mill(j, 1) == 1 and self.__board.get_pos(j) == -1:
                        nr = 0
                        for k in self.__board.get_adj(j):
                            if self.__board.get_pos(k) == 1:
                                nr = nr + 1
                        if nr > 0 and k / nr < maxim:
                            maxim = k / nr
                            maxi = i
                            maxj = j
        if maxi != -1 and maxj != -1:
            return maxi, maxj

        for i in range(0, 24):
            if self.__board.get_pos(i) == 0:
                for j in range(0 , 24):
                    if self.__board.check_pot_mill(j, 1) == 1 and self.__board.get_pos(j) == -1:
                        return i, j
        return -1, -1

    def move_from_random_position_phase3(self):
        """
        Function to get a random position for the computer to move in the phase 3 of the game
        :return: the initial position and the final position
        """
        for i in range(0, 24):
            if self.__board.get_pos(i) == 0:
                for j in range (0 , 24):
                   if self.__board.get_pos(j) == -1:
                        return i, j
        return -1, -1


    def move_from_random_position_phase2(self):
        """
                Function to get a random position for the computer to move in the phase 2 of the game
                :return: the initial position and the final position
                """
        for i in range(0, 24):
            if self.__board.get_pos(i) == 0:
                for j in self.__board.get_adj(i):
                   if self.__board.get_pos(j) == -1:
                        return i, j
        return -1, -1
    def move_from_ai_mill(self):
        """
        Function to move a piece from an existing mill
        :return: the initial position and the final position
        """
        for i in range(0, 24):
            if self.__board.get_pos(i) == 0 and self.__board.check_mill(i , 0) == 1:
                for j in self.__board.get_adj(i):
                    if self.__board.get_pos(j) == -1:
                        return i, j
        return -1 , -1

    def move_to_block_a_human_mill_phase2(self):
        """
        Function to give the position for the computer to move in the best position in order to block a human mill
        in phase 3 of the game
        :return: the initial position , and the final position
        """
        nr = 0
        maxim = 1000
        maxi = -1
        maxj = -1
        for i in range(0, 24):
            if self.__board.get_pos(i) == 0:
                for j in self.__board.get_adj(i):
                    if self.__board.check_pot_mill(j, 1) == 1 and self.__board.get_pos(j) == -1:
                        nr = 0
                        for k in self.__board.get_adj(j):
                            if self.__board.get_pos(k) == 1:
                                nr = nr + 1
                        if nr > 0 and k / nr < maxim:
                            maxim = k / nr
                            maxi = i
                            maxj = j
        if maxi != -1 and maxj != -1:
            return maxi , maxj


        for i in range(0, 24):
            if self.__board.get_pos(i) == 0:
                for j in self.__board.get_adj(i):
                    if self.__board.check_pot_mill(j, 1) == 1 and self.__board.get_pos(j) == -1:
                        return i, j
        return -1, -1

    def move_to_form_a_mill_phase2(self):
        """
               Function to give the position for the computer to move in the best position in order to make a mill
               in phase 2 of the game
               :return: the initial position , and the final position
               """
        board2 = copy.deepcopy(self.__board)
        for i in range(0 , 24):
            if board2.get_pos(i) == 0:
                for j in board2.get_adj(i):
                    if board2.check_pot_mill(j , 0) == 1 and board2.get_pos(j) == -1:
                        board2.move_piece(i , j)
                        if board2.check_mill(j , 0) == 1:
                            return i , j
                        else:
                            board2.move_piece(j , i)
        return -1 , -1


    def remove_human_piece(self):
        """
                Function for computer to decide which piece is the best to remove
                :return: the position
                """
        for i in range(0 , 24):
            if self.__board.get_pos(i) == 1:
                if self.__board.check_mill(i , 1) == 0:
                    if self.__board.check_pot_mill(i , 1) == 1:
                        self.__board.remove_piece(i)
                        return i
        for i in range(0, 24):
            if self.__board.get_pos(i) == 1:
                if self.__board.check_mill(i, 1) == 0:
                    if self.__board.check_1piece_mill(i , 1) == 1:
                        self.__board.remove_piece(i)
                        return i
        for i in range(0 , 24):
            if self.__board.get_pos(i) == 1:
                self.__board.remove_piece(i)
                return i
        return -1


    def make_ai_mill(self):
        """
        Function to check if the computer can make a mill
        :return: the position where to place
        """
        for i in range(0 , 24):
            if self.__board.get_pos(i) == -1 and self.__board.check_pot_mill(i , 0) == 1:
                self.__board.place_on_board(i , 0)
                return i
        return -1

    def make_ai_pot_mill(self):
        """
                Function to check if the computer can potentialy a mill
                :return: the position where to place
                """
        for i in range(0 , 24):
            if self.__board.get_pos(i) == -1 and self.__board.check_1piece_mill(i , 0) == 1:
                self.__board.place_on_board(i , 0)
                return i
        return -1

    def block_human_mill(self):
        """
        Function to check if the computer can block a human mill
        :return: the position where to place
        """
        for i in range (0 , 24):
            if self.__board.get_pos(i) == -1 and self.__board.check_pot_mill(i , 1) == 1:
                self.__board.place_on_board(i , 0)
                return i
        return -1


class Test_Computer_Player_Functions(TestCase):
    def test_move_phase1(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        computer.move_phase1()
        nr = 0
        for i in range (0 , 24):
            if board.get_pos(i) == 0:
                nr += 1
        assert nr == 1

    def test_move_phase2(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        computer.move_phase1()
        computer.move_phase1()

        nr = 0
        for i in range (0 , 24):
            if board.get_pos(i) == 0:
                assert board.check_pot_mill(i , 0) == 1

    def test_move_phase3(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        computer.move_phase1()
        computer.move_phase3()

        nr = 0
        for i in range (0 , 24):
            if board.get_pos(i) == 0:
                assert board.check_1piece_mill(i , 0) == 1

    def test_move_to_form_a_mill_phase3(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0 , 0)
        board.place_on_board(2, 0)
        board.place_on_board(21, 0)

        assert computer.move_to_form_a_mill_phase3() == (2 , 9)

    def test_move_to_form_a_mill_phase2(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0 , 0)
        board.place_on_board(2, 0)
        board.place_on_board(4, 0)

        assert computer.move_to_form_a_mill_phase3() == (4 , 1)

    def test_move_to_block_a_human_mill_phase3(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 1)
        board.place_on_board(2, 1)
        board.place_on_board(4, 1)
        board.place_on_board(9, 1)
        board.place_on_board(10, 1)

        board.place_on_board(19, 0)

        assert computer.move_to_block_a_human_mill_phase3() == (19, 1)

    def test_move_to_block_a_human_mill_phase2(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 1)
        board.place_on_board(2, 1)
        board.place_on_board(4, 0)


        assert computer.move_to_block_a_human_mill_phase3() == (4, 1)

    def test_move_from_random_position_phase3(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(19, 0)

        assert computer.move_from_random_position_phase3() == (19, 0)

    def test_move_from_random_position_phase2(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 0)

        assert computer.move_from_random_position_phase3() == (0, 1)

    def test_move_from_ai_mill(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 0)
        board.place_on_board(1, 0)
        board.place_on_board(2, 0)

        assert computer.move_from_ai_mill() == (0 , 9)

    def test_remove_human_piece(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 1)
        board.place_on_board(2, 1)

        assert computer.remove_human_piece() == 0

    def test_make_ai_mill(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 0)
        board.place_on_board(2, 0)
        assert computer.make_ai_mill() == 1

    def test_make_ai_pot_mill(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 0)
        assert computer.make_ai_pot_mill() == 1

    def test_make_ai_mill(self):
        board = Board_Domain()
        computer = Computer_Player(board)

        board.place_on_board(0, 1)
        board.place_on_board(2, 1)

        assert computer.block_human_mill() == 1
