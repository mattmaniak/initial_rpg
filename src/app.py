from random import choice

import src.characters as characters


class App:
    """Gameplay."""

    enemy = None
    player = None
    player_starts = choice((False, True))

    def __init__(self):
        player_id = ''

        print('Welcome to the mattmaniak\'s Initial RPG game.\n')
        for ch in characters.all.values():
            print(ch.name
                  + f' ({ch.hp} hp, {ch.attack} attack, {ch.armor} armor,'
                  + f' {ch.speed} speed)'
                  + f' - type \'{ch.name[0].lower()}\'.')

        while self.player is None:
            player_id = input('Choose your character: ')
            for character_name in characters.all:
                if player_id == character_name[0].lower():
                    self.player = characters.all[character_name]

        characters.all.pop(self.player.name)
        self.enemy = choice(list(characters.all.values()))

    def round(self):
        """Main loop."""

        print('\n' + self.player.name
              + ' is your chosen character. Your enemy will be the '
              + self.enemy.name + '.')

        input('Press \'Enter\' to start the round.\n')

        while self.player.is_alive() and self.enemy.is_alive():
            if self.player_starts:
                self.enemy.receive_damage(self.player)
                self.player.receive_damage(self.enemy)
            else:
                self.player.receive_damage(self.enemy)
                self.enemy.receive_damage(self.player)
