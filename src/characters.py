from random import randint


class __Character():
    """A sketch of the all game characters."""

    def __init__(self, name, attack, defense, speed):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.__hp = 0
        self.__prng_spread = 1

    def is_alive(self):
        return self.__hp > 0

    def receive_damage(self, enemy):
        enemy_speed = self.__randomize_attribute(enemy.speed)

        for i in range(enemy_speed):
            defense = self.__randomize_attribute(self.defense)
            enemy_attack = self.__randomize_attribute(enemy.attack)

            if self.__hp >= enemy_attack - defense:
                self.__hp -= enemy_attack - defense

    def __randomize_attribute(self, attribute):
        """Retrun a pseudo-random value of a given attribute.

        Provide a little pseudo-randomness of the game.
        """

        return randint(attribute - self.__prng_spread,
                       attribute + self.__prng_spread)


CHARACTERS = {'Knight: ': __Character(name='Knight', attack=17, defense=6, speed=2),
              'Oathbreaker': __Character(name='Oathbreaker', attack=7, defense=5, speed=4),
              'Wizard': __Character(name='Wizard', attack=8, defense=10, speed=3)}
