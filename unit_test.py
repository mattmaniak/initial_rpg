import unittest

from src.app import App
import src.characters as characters


class AppCase(unittest.TestCase):
    app = App()

    def test_characters(self):
        self.assertNotIn(self.app.player, characters.all.values())
        self.assertIn(self.app.enemy, characters.all.values())

        print('Player ' + self.app.player.name + ' is in '
              + str(characters.all) + '. Enemy ' + self.app.enemy.name
              + ' is not.')


if __name__ == '__main__':
    unittest.main()

else:
    from sys import stderr
    stderr.write('Do not import the main file.\n')
    exit()
