from Nine_mens_morris.Board_Domain import  Board_Domain
from Nine_mens_morris.Computer_Player import Computer_Player
from Nine_mens_morris.ui import UI

if __name__ == "__main__":

    board = Board_Domain()
    computer = Computer_Player(board)
    ui = UI(board , computer)
    ui.ui_start()

