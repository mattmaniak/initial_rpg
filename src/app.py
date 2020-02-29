from random import choice

from src.characters import CHARACTERS


class App:
    def __init__(self):
        self.__characters = CHARACTERS
        self.__enemies = CHARACTERS
        self.__enemy = None
        self.__player = None
        self.__player_id = ''

        print('Welcome to the Initial RPG.\n')
        for ch in self.__characters:
            print(ch + ' - type \'' + ch[0].lower() + '\'.')

        while self.__player is None:
            try:
                self.__player_id = input('Choose your character: ')
            except KeyboardInterrupt:
                pass

            for ch in self.__characters:
                if self.__player_id == ch[0].lower():
                    self.__player = self.__characters[ch]

        self.__enemies.pop(self.__player.name)
        __, self.__enemy = choice(list(self.__enemies.items()))

    def run(self):
        print('\nChosen player: ' + self.__player.name + ' and your enemy: '
              + self.__enemy.name + '.')
