import copy
import time

from Nine_mens_morris.Board_Domain import Board_Domain
from Nine_mens_morris.Computer_Player import Computer_Player


class ValidationException(Exception):
    pass

class UI:
    def __init__(self , board : Board_Domain , computer : Computer_Player):
        self.__board = board
        self.__computer= computer

    def print_menu(self):
        print("*----------------------------------*\n"
              "   *Welcome to Nine Men's Morris*\n"
              "*----------------------------------*\n\n"
              "Nine men's morris is a strategy board game for two players dating "
              "at least to the Roman Empire.\nThe game is also known as nine-man morris, "
              "mill, mills, the mill game, merels, merrills, merelles,\nmarelles, morelles, "
              "and ninepenny marl in English. In North America, the game has also been "
              "called cowboy checkers,\nand its board is sometimes printed on the back of checkerboards.\n\n\n"
              "Available Commands: 'start' , 'rules' , 'exit'\n")

    def print_rules(self):
        print("The board consists of a grid with twenty-four intersections, or points.\n"
              "Each player has nine pieces, or men, usually coloured black and white.\n"
              "Players try to form 'mills'—three of their own men lined horizontally or vertically—allowing a player to remove an opponent's man from the game.\n"
              "A player wins by reducing the opponent to two men (whereupon they can no longer form mills and thus are unable to win) or by leaving them without a legal move.\n"         
               "The game proceeds in three phases:\n"           
               "   1.Placing men on vacant points\n"
               "   2.Moving men to adjacent points\n"
               "   3.(optional phase) Moving men to any vacant point when the player has been reduced to three men\n\n"
              "---------Phase 1: Placing pieces---------\nNine men's morris starts on an empty board.The game begins with an empty board.\n"
              "The players determine who plays first and then take turns. During the first phase, a player's turn consists of placing a man from their hand onto an empty point.\n"
              "If a player is able to place three of their pieces on contiguous points in a straight line, vertically or horizontally,\n"
              "they have formed a mill, which allows them to remove one of their opponent's pieces from the board.\n"
              "A piece in an opponent's mill, however, can be removed only if no other pieces are available.\n"
              "After all men have been placed, phase two begins.\n\n"
              "---------Phase 2: Moving pieces---------\nPlayers continue to alternate moves, this time moving one of their men to an adjacent point each turn.\n"
              "A piece may not 'jump' another piece. Players continue to try to form mills and remove their opponent's pieces as in phase one.\n"
              "If all a player's pieces get blocked in (where they are unable to move to an adjacent, empty space) that player loses.\n"
              "A player can 'break' a mill by moving one of his pieces out of an existing mill, then moving it back to form the same mill a second time\n"
              "(or any number of times), each time removing one of his opponent's men.\n"
              "The act of removing an opponent's man is sometimes called 'pounding' the opponent.\n"
              "When one player has been reduced to three men, phase three begins.\n\n"
              "---------Phase 3: Flying ---------\nWhen a player is reduced to three pieces, there is no longer a limitation on that player of moving\n"
              "to only adjacent points: The player's men may 'fly' from any point to any vacant point.\n"
              "Flying was introduced to compensate when the weaker side is one man away from losing the game\n\n\n")


    def computer_phase1(self):
        c_pos , mill = self.__computer.move_phase1()
        if mill == 0:
            print("Computer moved on position " + str(c_pos))
        else:
            c_pos2 = self.__computer.remove_human_piece()
            print("Computer moved on position " + str(c_pos) + " and made a mill. He removed your piece from position " + str(c_pos2))



    def player_phase1(self):
            p_move = input("--------Your turn!---------\nWhere do you want to place a piece?\n")
            if p_move.isdigit() == 0:
                raise ValidationException("Please enter a valid position")
            p_move = int(p_move)
            if p_move not in range(0 , 24):
                raise ValidationException("Please enter a valid position!")
            if self.__board.get_pos(p_move) == -1:
                self.__board.update(p_move , 1)
                print("Piece moved on position " + str(p_move))
                return p_move
            else:
                raise ValidationException("Position occupied")

    def player_phase2(self):
        while True:
            try:
                print("From where do you want to move a piece? ")
                from_opt = input("> ")
                if from_opt.isdigit() == False:
                    raise ValidationException("Please enter a valid position")
                from_opt = int(from_opt)
                if self.__board.get_pos(from_opt) != 1:
                    raise ValidationException("You don't have a piece on that position!")
                if self.__board.can_be_moved(from_opt) == 0:
                    raise ValidationException("This piece cannot be moved anywhere!")
                break
            except ValidationException as ve:
                print(str(ve))

        while True:
            try:
                print("Where do you want to move the piece?")
                to_opt = input("> ")
                if to_opt.isdigit() == False:
                    raise ValidationException("Please enter a valid position")
                to_opt = int(to_opt)
                if self.__board.get_pos(to_opt) != -1:
                    raise ValidationException("That position is occupied!")
                if self.__board.two_adj(from_opt, to_opt) == False:
                    raise ValidationException("Please move to an adiacent position!")
                self.__board.move_piece(from_opt, to_opt)
                print("Piece succesfully moved from position " + str(from_opt) + " to position " + str(to_opt))
                return to_opt
            except ValidationException as ve:
                print(str(ve))
    def player_formed_mill(self):
        print(
            "Congratulations! You formed a mill! Now choose one of the positions available to remove one oponent piece")
        available_pos = []
        for i in range(0, 24):
            if self.__board.get_pos(i) == 0 and self.__board.check_mill(i , 0) == 0:
                available_pos.append(i)
        if len(available_pos) == 0:
            for i in range(0, 24):
                if self.__board.get_pos(i) == 0:
                    available_pos.append(i)
        while True:
            try:
                print("Choose one of the available positions: ", ', '.join(map(str, available_pos)))
                option = input("> ")
                if option.isdigit() == False:
                    raise ValidationException("Please choose a valid position!")
                option = int(option)
                if option not in available_pos:
                    raise ValidationException("There is no piece on that position!")
                self.__board.remove_piece(option)
                print("You succesfully removed the piece from position " + str(option))
                print(self.__board)
                break
            except ValidationException as ve:
                print(str(ve))

    def computer_phase2(self):
        initial , final , mill = self.__computer.move_phase2()

        if mill == 0:
            print("Computer moved from position " + str(initial) + " to position " + str(final))
        else:
            c_pos2 = self.__computer.remove_human_piece()
            print("Computer moved from position " + str(initial) + " to position " + str(final) + " and made a mill. He removed your piece from position " + str(c_pos2))

    def player_phase3(self):
        while True:
            try:
                print("From where do you want to move a piece? ")
                from_opt = input("> ")
                if from_opt.isdigit() == False:
                    raise ValidationException("Please enter a valid position")
                from_opt = int(from_opt)
                if self.__board.get_pos(from_opt) != 1:
                    raise ValidationException("You don't have a piece on that position!")
                break
            except ValidationException as ve:
                print(str(ve))

        while True:
            try:
                print("Where do you want to move the piece?")
                to_opt = input("> ")
                if to_opt.isdigit() == False:
                    raise ValidationException("Please enter a valid position")
                to_opt = int(to_opt)
                if self.__board.get_pos(to_opt) != -1:
                    raise ValidationException("That position is occupied!")
                self.__board.move_piece(from_opt, to_opt)
                print("Piece succesfully moved from position " + str(from_opt) + " to position " + str(to_opt))
                return to_opt
            except ValidationException as ve:
                print(str(ve))

    def computer_phase3(self):
        initial , final , mill = self.__computer.move_phase3()

        if mill == 0:
            print("Computer moved from position " + str(initial) + " to position " + str(final))
        else:
            c_pos2 = self.__computer.remove_human_piece()
            print("Computer moved from position " + str(initial) + " to position " + str(final) + " and made a mill. He removed your piece from position " + str(c_pos2))


    def start_phase2(self , move):
        print("*-----------------------------------*\n"
              "     *Phase 2 of game started*\n"
              "*-----------------------------------*\n\n")
        phase3_you = 0
        phase3_ai = 0
        while True:
            try:
                if move == 1:
                    print(self.__board)


                    if phase3_you == 0:
                        move = 0
                        last_move = self.player_phase2()
                        if self.__board.check_mill(last_move , 1) == 1:
                            self.player_formed_mill()
                        if self.__board.is_board_won() == 1:
                            print("*-----------------------------------*\n"
                                  "    *Congratulations! You won!*\n"
                                  "*-----------------------------------*\n\n")
                            break
                        elif self.__board.only_3_pieces(0) == 1:
                            print("*-----------------------------------*\n"
                                  "     *Phase 3 of game started*\n"
                                  "*-----------------------------------*\n\n")
                            print("The computer has only 3 pieces left. Now he can move in any place on the board! \n")
                            phase3_ai = 1

                    elif phase3_you == 1:
                        last_move = self.player_phase3()
                        if self.__board.check_mill(last_move, 0) == 1:
                            self.player_formed_mill()
                        if self.__board.is_board_won() == 1:
                            print("*-----------------------------------*\n"
                                  "    *Congratulations! You won!*\n"
                                  "*-----------------------------------*\n\n")
                            break
                        move = 0





                elif move == 0:
                    if phase3_ai == 0:
                        self.computer_phase2()
                        if self.__board.is_board_won() == 1:
                            print("*-----------------------------------*\n"
                                  "     *Game over! You lost :(\n"
                                  "*-----------------------------------*\n\n")
                            break

                        elif self.__board.only_3_pieces(1) == 1:
                            print("*-----------------------------------*\n"
                                  "     *Phase 3 of game started*\n"
                                  "*-----------------------------------*\n\n")
                            print("You have left only 3 pieces. Now you can move a piece wherever you want! \n")
                            phase3_you = 1
                        move = 1

                    elif phase3_ai == 1:
                        self.computer_phase3()
                        if self.__board.is_board_won() == 1:
                            print("*-----------------------------------*\n"
                                  "     *Game over! You lost :(\n"
                                  "*-----------------------------------*\n\n")
                            break
                        move = 1




            except ValidationException as ve:
                print(str(ve))


    def start_phase1(self , move):
        total_pieces = 0
        while True:
            try:
                if move == 1:
                    print(self.__board)
                    last_move = self.player_phase1()
                    if self.__board.check_mill(last_move , 1) == 1:
                        self.player_formed_mill()
                    move = 0
                    total_pieces = total_pieces + 1
                elif move == 0:
                    self.computer_phase1()
                    move = 1
                    total_pieces = total_pieces + 1
                if total_pieces == 18:
                    self.start_phase2(move)
                    break


            except ValidationException as ve:
                print(str(ve))



    def ui_start(self):
        self.print_menu()
        while True:
            try:
                option = input(">> ")
                option = option.strip()
                option = option.lower()
                if option not in ["start" , "rules" , "exit"]:
                    raise ValidationException("Please enter valid command!")
                elif option == "rules":
                    self.print_rules()
                elif option == "start":
                    who_starts = input("Do you want to move first (yes/no)\n >> ")
                    who_starts = who_starts.strip()
                    who_starts = who_starts.lower()
                    if who_starts not in ["yes" , "no"]:
                            raise ValidationException("Please enter valid command!")
                    elif who_starts == "yes":
                        self.start_phase1(1)
                    elif who_starts == "no":
                        self.start_phase1(0)
                elif option == "exit":
                    break
                else: raise ValidationException("Invalid command!")
                        
            except ValidationException as ve:
                print(ve)

