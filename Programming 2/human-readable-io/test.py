import unittest
from io import StringIO

from human_writeable_IO import HumanWriteableIO
from broken_reader import BrokenReader
from corrupted_chess_file_error import CorruptedChessFileError
from piece import Piece

from robotworld import RobotWorld
from robot import Robot

from spinbot import Spinbot
from drunkbot import Drunkbot
from nosebot import Nosebot

from coordinates import Coordinates
from direction import Direction



class Test(unittest.TestCase):

    def setUp(self):
        self.human_IO = HumanWriteableIO()

        self.test_world = RobotWorld(5, 5)
        wall_coordinates = Coordinates(2, 4)
        self.test_world.add_wall(wall_coordinates)

        first_location = Coordinates(4, 3)
        first_body = Robot('Bart')
        first_brain = Spinbot(first_body)
        first_body.set_brain(first_brain)
        self.test_world.add_robot(first_body, first_location, Direction.EAST)


    """
    IMPORTANT!

    The  test method is allowed here to throw the CorruptedChessFileError.

    The reasons for this are
    1) we expect the code to work
    2) if the code throws this exception the test will fail

    This is therefore desired behavior for this test. It also removes the problem
    of untestable code in the catch section.
    """

    def test_given_example(self):
        self.input_file = StringIO()
        self.input_file.write('SHAKKI 1.222 Tallennustiedosto\n\n')
        self.input_file.write('#Pelin tiedot\n\nTallennettu : 5.7.2001\n')
        self.input_file.write('Musta     : Marko\nValkoinen : Lauri\n\n#Kommentit\n')
        self.input_file.write('\nLaurin revanssipeli, joskin huonosti on menossa...\n')
        self.input_file.write('\n#Musta\n\nKuningas   : a4\nTorni      : a6\n')
        self.input_file.write('Sotilas    : b3\nKuningatar : c8\n\n#Valkoinen\n')
        self.input_file.write('\nKuningas   : d3\nRatsu      : f1')

        self.input_file.seek(0, 0)

        game = None

        game = self.human_IO.load_game(self.input_file)

        self.input_file.close()

        self.assertNotEqual(None, game.get_black(), "Loading data failed. Player missing.")
        self.assertEqual("Marko" ,game.get_black().get_name(),  "Loading data failed. Wrong player name.")

        # Add your own tests, check that the players are ok and that the pieces were correctly placed.

    def test_nosebot(self):
        """
        Tests the nosebot movements.
        """
        location5 = Coordinates(4, 4)
        body5 = Robot('ABC')
        brain5 = Nosebot(body5)
        body5.set_brain(brain5)
        self.test_world.add_robot(body5, location5, Direction.WEST)

        self.test_world.next_full_turn()
        self.test_world.next_full_turn()

        self.assertEqual('(3, 3)', str(self.test_world.get_robots()[1].get_location()),
                         "Error! Nosebot should be in (3, 3).")

    def test_drunkbot(self):
        """
        Tests the drunkbot movements.
        """
        location5 = Coordinates(4, 4)
        body5 = Robot('ABC')
        brain5 = Nosebot(body5)
        body5.set_brain(brain5)
        self.test_world.add_robot(body5, location5, Direction.WEST)

        location2 = Coordinates(2, 2)
        body2 = Robot('XYZ')
        brain2 = Drunkbot(body2, 4522)
        body2.set_brain(brain2)
        self.test_world.add_robot(body2, location2, Direction.SOUTH)

        self.test_world.next_full_turn()
        self.test_world.next_full_turn()

        self.assertEqual('(3, 3)', str(self.test_world.get_robots()[1].get_location()),
                         "Error! Nosebot should be at (3, 3).")

        self.assertEqual('(2, 3)', str(self.test_world.get_robots()[2].get_location()),
                         "Error! Drunkbot should be at (2, 3).")

        self.assertTrue(self.test_world.get_robot(1).is_broken(),
                        "Error! Drunkbot crashed into Nosebot. Nosebot should be broken.")

    def testOSError(self):
        """
        This test was designed to test the catch code in method load_game.
        """
        original_file = StringIO()
        original_file.write('SHAKKI 1.2 Tallennustiedosto\n')
        original_file.write('\n')
        original_file.write('#Pelin tiedot\n')
        original_file.write('\n')
        original_file.write('Tallennettu : 5.7.2001\n')
        original_file.write('Musta     : Marko\n')
        original_file.write('Valkoinen : Lauri\n')
        original_file.write('\n')
        original_file.write('#Kommentit\n')
        original_file.write('\n')
        original_file.write('Laurin revanssipeli, joskin huonosti on menossa...\n')
        original_file.write('\n')
        original_file.write('#Musta\n')
        original_file.write('\n')
        original_file.write('Kuningas   : a4\n')
        original_file.write('Torni      : a6\n')
        original_file.write('Sotilas    : b3\n')
        original_file.write('Kuningatar : c8\n')
        original_file.write('\n')
        original_file.write('#Valkoinen\n')
        original_file.write('\n')
        original_file.write('Kuningas   : d3\n')
        original_file.write('Ratsu      : f1')

        data = original_file.getvalue()
        # Adding a brokenreader allows throwing simulated exceptions
        self.input_file = BrokenReader(data, 50)

        original_file.close()

        check_this = None
        try:
            self.human_IO.load_game(self.input_file)
        except CorruptedChessFileError as e:
            check_this = e

        self.input_file.close_really()

        # Note that initially your code does not read past the file header
        # so this test will fail.

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not thrown.")


    def close_silently(self, r):
        try:
            r.close()
        except OSError:
            """ignore"""


if __name__ == "__main__":
    unittest.main()
