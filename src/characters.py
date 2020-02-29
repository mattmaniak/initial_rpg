from random import randint


class __Character():
    """A sketch of the all game characters."""

    def __init__(self, name, hp, attack, armor, speed):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.__hp = hp
        self.__prng_spread = 1

    def is_alive(self):
        return self.__hp > 0

    def receive_damage(self, enemy):
        enemy_speed = self.__randomize_attribute(enemy.speed)

        for i in range(enemy_speed):
            armor = self.__randomize_attribute(self.armor)
            enemy_attack = self.__randomize_attribute(enemy.attack)
            self.__hp -= enemy_attack - armor

            print(self.name + ' (current hp: ' + str(self.__hp) + ') lost '
                  + str(enemy_attack - armor) + ' hp (' + str(enemy_attack)
                  + ' damage - ' + str(armor) + ' armor) by '
                  + str(enemy.name) + '.')

    def __randomize_attribute(self, attribute):
        """Retrun a pseudo-random value of a given attribute.

        Provide a little pseudo-randomness of the game.
        """

        return randint(attribute - self.__prng_spread,
                       attribute + self.__prng_spread)


all = {'Knight': __Character(name='Knight', hp=100, attack=17, armor=6,
                             speed=2),
       'Oathbreaker': __Character(name='Oathbreaker', hp=60, attack=7, armor=5,
                                  speed=4),
       'Wizard': __Character(name='Wizard', hp=120, attack=8, armor=10,
                             speed=3)}
