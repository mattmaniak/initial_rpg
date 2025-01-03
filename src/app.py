import random
import time

import src.characters


class App:
    """Gameplay."""

    enemy = None
    player = None
    player_starts = random.choice((False, True))

    def __init__(self):
        player_id = ''

        print('Welcome to the mattmaniak\'s Initial RPG game.\n')
        for ch in src.characters.all.values():
            print(ch.name
                  + f' ({ch.hp} hp, {ch.attack} attack, {ch.armor} armor,'
                  + f' {ch.speed} speed)'
                  + f' - type \'{ch.name[0].lower()}\'.')

        while self.player is None:
            player_id = input('Choose your character: ')
            for character_name in src.characters.all:
                if player_id == character_name[0].lower():
                    self.player = src.characters.all[character_name]

        src.characters.all.pop(self.player.name)
        self.enemy = random.choice(list(src.characters.all.values()))

    def round(self):
        """Main loop."""

        print('\n' + self.player.name
              + ' is your chosen character. Your enemy will be the '
              + self.enemy.name + '.')

        input('Press \'Enter\' to start the round.\n')

        while self.player.is_alive() and self.enemy.is_alive():
            if self.player_starts:
                if not self.enemy.receive_damage(self.player) \
                        or not self.player.receive_damage(self.enemy):
                    break
            else:
                if not self.player.receive_damage(self.enemy) \
                        or not self.enemy.receive_damage(self.player):
                    break

            time.sleep(1)
            print('')
