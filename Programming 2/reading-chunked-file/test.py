import unittest
from io import StringIO


from chunkIO import ChunkIO
from broken_reader import BrokenReader
from corrupted_chess_file_error import CorruptedChessFileError
from piece import Piece


class Test(unittest.TestCase):

    def test_given_example(self):
        """
        IMPORTANT!

        The test method is allowed here to throw the CorruptedChessFileError.

        The reasons for this are
        1) we expect the code to work
        2) if the code throws this exception the test will self.fail

        This is therefore desired behavior for this test. It also removes the problem
        of untestable code in the catch section.
        """
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURIKd3Rf1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        #self.input_file = open('game.txt', 'r')
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
        except CorruptedChessFileError:
            self.fail("Loading a correctly structured file caused an exception")

        self.input_file.close()


        self.assertNotEqual(None, game.get_black(), "Loading data self.failed. Player missing.")
        self.assertEqual("Marko" ,game.get_black().get_name(),  "Loading data self.failed. Wrong player name.")


        # Add your own tests, check that the players are ok and that the pieces were correctly placed.

    def test_broken_example_un_chunk(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLY17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURILd3Df1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_1(self):
        test_data = u"SHACKA1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURILd3Df1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_given_example_2(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURILd3Df1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
        except CorruptedChessFileError:
            self.fail("Loading a correctly structured file caused an exception")

        self.input_file.close()

    def test_broken_example_up(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c9" + u"PLR13V5LAURIKd3Rf7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_3(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURIKd3Ri1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_colours(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17G5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKd3Rf7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_min_layer(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_letter_space(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKd3Rf7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_blow(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c-9" + u"PLR13V5LAURIKd3Rf7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_early_end(self):
        test_data = u"END00SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURILd3Df1" + u"PLR13V5KALLELf3Dd1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_end(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKd3Rf7" + u""

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_exp_layer(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURILd3Df1" + u"PLR13V5KALLELf3Dd1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_size(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3k7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_end_big(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKd3Rf7" + u"END1234556"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_ex_chunk(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKd3Rf7" + u"PLR13V5KIVIAKd3Rf7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_value(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKa4Ta6b3k7" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()

    def test_broken_example_order(self):
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"END00" + u"PLR17M5MarkoKa4Ta6b3k7" + u"PLR13V5LAURIKd3Rf7"
        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
            self.fail("Loading a correctly structured file caused an exception")
        except CorruptedChessFileError:
            pass

        self.input_file.close()


    def testOSError(self):
        """
        This test was designed to test the catch code in method load_game.
        """
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + "PLR13V5LAURIKd3Rf1" + "END00"

        #original_file = open('game.txt', 'r')

        # Adding a brokenreader allows raising simulated exceptions
        self.input_file = BrokenReader(test_data, 26)

        check_this = None
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check_this = e

        # Note that initially your code does not read past the file header
        # so this test will fail.

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")

        try:
            self.input_file.close()
            self.fail("Closing a file did not cause an exception.")
        except OSError:
            """All ok"""

        self.input_file.close_really()


    def close_silently(self, r):
        try:
            r.close()
        except OSError:
            """ignore"""


if __name__ == "__main__":
    unittest.main()
