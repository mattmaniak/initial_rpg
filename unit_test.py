import unittest

from src.app import App
import src.characters as characters

app = App()


class AppCase(unittest.TestCase):
    def test_init(self):
        self.assertNotIn(app.player, characters.all.values())
        self.assertIn(app.enemy, characters.all.values())


class CharacterCase(unittest.TestCase):
    def test_is_alive(self):
        self.assertTrue(app.player.is_alive, app.player.hp > 0)
        self.assertTrue(app.enemy.is_alive, app.enemy.hp > 0)


if __name__ == '__main__':
    unittest.main()

else:
    from sys import stderr
    stderr.write('Do not import the main file.\n')
    exit()
