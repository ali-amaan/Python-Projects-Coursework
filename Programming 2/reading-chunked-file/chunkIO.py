from game import Game
from corrupted_chess_file_error import *
from player import Player
from piece import Piece
from board import Board


class ChunkIO(object):

    def load_game(self, input):
        """
        @note:This is the game object this method will fill with data. The object
               is returned when the END chunk is reached.
        """
        self.game = Game()

        try:

            # Read the file header and the save date

            header = self.read_fully(8, input)
            date = self.read_fully(8, input)

            # Process the data we just read.
            # NOTE: To test the line below you must test the class once with a broken header

            header = ''.join(header)
            date = ''.join(date)
            if not str(header).startswith("SHAKKI"):
                raise CorruptedChessFileError("Unknown file type")

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

            self.board = Board()
            self.game.set_board(self.board)

            flag = False

            self.players = []

            while not flag:
                header = self.read_fully(5, input)
                name = self.extract_chunk_name(header)
                size = self.extract_chunk_size(header)

                if name == "PLR":
                    self.player_read(size, input)
                elif name == "CMT":
                    self.comment_read(size, input)
                elif name == "END":
                    if len(self.players) != 2:
                        raise CorruptedChessFileError("Error! Player count is incorrect.")
                    else:
                        flag = self.end_read(size)
                else:
                    self.other_read(size, input)

            # If we reach this point the Game-object should now have the proper players and
            # a fully set up chess board. Therefore we might as well return it.

            return self.game

        except OSError:
            # To test this part the stream would have to cause an
            # OSError. That's a bit complicated to test. Therefore we have
            # given you a "secret tool", class BrokenReader, which will throw
            # an OSError at a requested position in the stream.
            # Throw the exception inside any chunk, but not in the chunk header.
            raise CorruptedChessFileError("Error! Reading chess data failed.")


    # HELPER METHODS -------------------------------------------------------


    def player_read(self, chunk_size, input):
        if len(self.players) >= 2:
            raise CorruptedChessFileError("Error! Player count is incorrect.")
        colour = "".join(self.read_fully(1, input))

        if colour == "M":
            temp = 1
        elif colour == "V":
            temp = 0
        else:
            raise CorruptedChessFileError("Error: Colour codes incorrect.")

        length_of_name = self.read_fully(1, input)
        length_of_name = int("".join(length_of_name))
        n = "".join(self.read_fully(length_of_name, input))
        player = Player(n, temp)
        self.players.append(player)
        self.game.add_player(player)
        rem = chunk_size - length_of_name - 2

        i = 0
        while i < rem:
            letter1 = "".join(self.read_fully(1, input))

            if letter1 == "K":
                p = Piece(player, 0)
                self.place_piece(input, p)
                i += 3

            elif letter1 == "D":
                p = Piece(player, 1)
                self.place_piece(input, p)
                i += 3

            elif letter1 == "L":
                p = Piece(player, 2)
                self.place_piece(input, p)
                i += 3

            elif letter1 == "R":
                p = Piece(player, 3)
                self.place_piece(input, p)
                i += 3

            elif letter1 == "T":
                p = Piece(player, 4)
                self.place_piece(input, p)
                i += 3

            else:
                p = Piece(player, 5)
                c = Board.column_char_to_integer(letter1)
                r = Board.row_char_to_integer("".join(self.read_fully(1, input)))
                if (r < 0) or (r > 7) or (c < 0) or (c > 7):
                    raise CorruptedChessFileError("Error! Board dimensions incorrect.")
                self.board.set_piece(p, c, r)
                i += 2


    def place_piece(self, input, p):
        try:
            c = Board.column_char_to_integer("".join(self.read_fully(1, input)))
            r = Board.row_char_to_integer("".join(self.read_fully(1, input)))

            if (r < 0) or (r > 7) or (c < 0) or (c > 7):
                raise CorruptedChessFileError("Error! Board dimensions incorrect.")

            self.board.set_piece(p, c, r)

        except ValueError:
            raise CorruptedChessFileError("Error! Value error.")


    def end_read(self, chunk_size):
        if chunk_size != 00:
            raise CorruptedChessFileError("Error! Non-empty end file.")
        else:
            return True


    def comment_read(self, chunk_size, input):
        if chunk_size != 00:
            self.read_fully(chunk_size, input)


    def other_read(self, chunk_size, input):
        if chunk_size != 00:
            self.read_fully(chunk_size, input)


    def extract_chunk_size(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the size of this
        chunks data.

        @param chunk_header:
                   a chunk header to process (str)
        @return: the size (int) of this chunks data
        """


        # subtracting the ascii value of the character 0 from
        # a character containing a number will return the
        # number itself

        return int( ''.join( chunk_header[3:5] ) )


    def extract_chunk_name(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the name of this
        chunk as a 3-letter String.

        @param chunk_header:
                   a chunk header to process
        @return: the name of this chunk
        """
        return ''.join( chunk_header[0:3] )


    def read_fully(self, count, input):
        """
        The read-method of the Reader class will occasionally read only part of
        the characters that were requested. This method will repeatedly call read
        to completely fill the given buffer. The size of the buffer tells the
        algorithm how many bytes should be read.

        @param count:
                   How many characters are read
        @param input:
                   The character stream to read from
        @raises: OSError
        @raises: CorruptedChessFileError
        """
        read_chars = input.read( count )

        # If the file end is reached before the buffer is filled
        # an exception is thrown.
        if len(read_chars) != count:
                raise CorruptedChessFileError("Unexpected end of file.")

        return list(read_chars)
