from random import choice

from src.characters import CHARACTERS


class App:
    """Gameplay."""

    __enemy = None
    __player = None
    __player_starts = choice((False, True))

    def __init__(self):
        enemies = CHARACTERS
        player_id = ''

        print('Welcome to the Initial RPG game.\n')
        for character_name in CHARACTERS:
            print(f'character_name - type \'{character_name[0].lower()}\'.')

        while self.__player is None:
            player_id = input('Choose your character: ')
            for character_name in CHARACTERS:
                if player_id == character_name[0].lower():
                    self.__player = CHARACTERS[character_name]

        enemies.pop(self.__player.name)
        __, self.__enemy = choice(list(enemies.items()))

    def round(self):
        """Main loop."""

        print('\n' + self.__player.name
              + ' is your chosen character. Your enemy will be the '
              + self.__enemy.name + '.')

        input('Press \'Enter\' to start the round.\n')

        while self.__player.is_alive() and self.__enemy.is_alive():
            if self.__player_starts:
                self.__enemy.receive_damage(self.__player)
                self.__player.receive_damage(self.__enemy)
            else:
                self.__player.receive_damage(self.__enemy)
                self.__enemy.receive_damage(self.__player)
