from src.characters import CHARACTERS


class App:
    def __init__(self):
        self.__characters = CHARACTERS
        self.__player_id = ''
        self.__player = None

        for ch in self.__characters:
            print(ch + ' - type \'' + ch[0].lower() + '\'.')

        while self.__player == None:
            try:
                self.__player_id = input('\nPick a player: ')
            except KeyboardInterrupt:
                pass

            for ch in self.__characters:
                if self.__player_id == ch[0].lower():
                    self.__player = self.__characters[ch]
        print('Chosen player: ' + self.__player.name)

    def run(self):
        print(self.__player.name)
