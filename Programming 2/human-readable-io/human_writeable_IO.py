from game import Game
from corrupted_chess_file_error import *
from player import Player
from piece import Piece
from board import Board


class HumanWriteableIO(object):

    def load_game(self, input):
        """
        This is the game object this method will fill with data. The object
        is returned when the file ends and everything is ok.
        """

        self.game = Game()
        board = Board()

        self.game.set_board(board)

        info_read = False
        white_read = False
        black_read = False


        #Use this variable for reading all the section headers.
        current_line = ''

        try:

            # Read the file header and the save date

            line = input.readline()
            header_parts = line.split(" ")

            self.board = Board()
            self.players = []

            self.game.set_board(self.board)

            # Process the data we just read.
            # NOTE: To test the line below you must test the class once with a
            # broken header

            if header_parts[0] != "SHAKKI":
                raise CorruptedChessFileError("Unknown file type")

            if header_parts[2].strip().lower() != 'tallennustiedosto':
                raise CorruptedChessFileError("Unknown file type")
            info_read = True

            # The version information and the date are not used in this
            # exercise

            # *************************************************************
            #
            # EXERCISE
            #
            # ADD CODE HERE FOR READING THE
            # DATA FOLLOWING THE MAIN HEADERS
            #
            #
            # *************************************************************

            self.piece_types = {'Kuningas':Piece.KING, 'Kuningatar':Piece.QUEEN, 'Torni':Piece.ROOK, 'Lahetti':Piece.BISHOP, 'Ratsu':Piece.KNIGHT, 'Sotilas':Piece.PAWN}

            self.piece_types_list = ['kuningas', 'kuningatar', 'torni', 'lahetti', 'ratsu', 'sotilas']

            read = False
            line = input.readline()

            while True:
                if line == "\n":
                    line = input.readline()
                elif len(line) == 0:
                    raise CorruptedChessFileError("Error! x1")
                else:
                    break

            while not read:
                if line.replace('#', '').lower().rstrip() == "pelin tiedot":
                    line = input.readline()
                    while line[0] != "#":
                        if line.split(":")[0].lower().rstrip() == "musta":
                            self.black_name = line.split(":")[1].lower().rstrip()
                            line = input.readline()
                        elif line.split(":")[0].lower().rstrip() == "valkoinen":
                            self.white_name = line.split(":")[1].lower().rstrip()
                            line = input.readline()
                        elif line.split(":")[0].lower().rstrip() == "tallennettu":
                            self.date = line.split(":")[1].lower().rstrip()
                            line = input.readline()
                        elif line == "\n":
                            line = input.readline()
                    print(line)

                elif line.replace('#', '').lower().rstrip() == "valkoinen":
                    self.white_pieces = []
                    line = input.readline()
                    while line[0] != "#":
                        if line.split(":")[0].lower().rstrip() in self.piece_types_list:
                            piece = [line.split(":")[0].rstrip(), line.split(":")[1].rstrip()]
                            self.white_pieces.append(piece)
                            line = input.readline()
                        else:
                            line = input.readline()
                        if len(line) == 0:
                            white_read = True
                            break

                elif line.replace('#', '').lower().rstrip() == "musta":
                    self.black_pieces = []
                    line = input.readline()
                    while line[0] != "#":
                        if line.split(":")[0].lower().rstrip() in self.piece_types_list:
                            piece = [line.split(":")[0].rstrip(), line.split(":")[1].rstrip()]
                            self.black_pieces.append(piece)
                            line = input.readline()
                        else:
                            line = input.readline()
                        if len(line) == 0:
                            black_read = True
                            break

                elif len(line) == "\n":
                    print("Empty line")
                    line = input.readline

                elif len(line) == 0:
                    read = True

                else:
                    line = input.readline()

            self.white_name = str.title(self.white_name).strip()
            self.black_name = str.title(self.black_name).strip()

            player_black = Player(self.black_name, 1)
            self.players.append(player_black)
            self.game.add_player(player_black)

            player_white = Player(self.white_name, 0)
            self.players.append(player_white)
            self.game.add_player(player_white)

            self.import_player(self.white_pieces, player_white)
            self.import_player(self.black_pieces, player_black)

            # If we reach this point the Game-object should now have the proper
            # players and
            # a fully set up chess board. Therefore we might as well return it.

            return self.game

        except OSError:
            # To test this part the stream would have to cause an
            # OSError. That's a bit complicated to test. Therefore we have
            # given you a "secret tool", class BrokenReader, which will throw
            # an OSError at a requested position in the stream.
            # Throw the exception inside any chunk, but not in the chunk
            # header.
            raise CorruptedChessFileError("Reading the chess data failed.")

    def import_player(self, player_inst, player):
        remaining = len(player_inst)
        i = 0
        while i < remaining:
            first_alphabet = player_inst[i][1][0]
            input = player_inst[i][1].strip()
            if player_inst[i][0] == "Kuningas":
                piece = Piece(player, 0)
                self.place_piece(input, piece)
                i += 1
            elif player_inst[i][0] == "Kuningatar":
                piece = Piece(player, 1)
                self.place_piece(input, piece)
                i += 1
            elif player_inst[i][0] == "Lahetti":
                piece = Piece(player, 2)
                self.place_piece(input, piece)
                i += 1
            elif player_inst[i][0] == "Ratsu":
                piece = Piece(player, 3)
                self.place_piece(input, piece)
                i += 1
            elif player_inst[i][0] == "Torni":
                piece = Piece(player, 4)
                self.place_piece(input, piece)
                i += 1
            elif player_inst[i][0] == "Sotilas":
                piece = Piece(player, 5)
                self.place_piece(input, piece)
                i += 1
            else:
                raise CorruptedChessFileError("Error! x4")

    def place_piece(self, input, piece):
        try:
            column = Board.column_char_to_integer("".join(input[0]))
            row = Board.row_char_to_integer("".join(input[1]))
            if 0 > column or column > 7 or 0 > row or row > 7:
                raise CorruptedChessFileError("Error! x3")
            self.board.set_piece(piece, column, row)
        except ValueError:
            raise CorruptedChessFileError("Error! x4")
