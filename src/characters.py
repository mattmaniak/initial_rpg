import random


class __Character():
    """A sketch of the all game characters."""

    def __init__(self, name, hp, attack, armor, speed):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.hp = hp
        self.__prng_spread = 1

    def is_alive(self):
        return self.hp > 0

    def receive_damage(self, enemy):
        enemy_speed = self.__randomize_attribute(enemy.speed)

        for i in range(enemy_speed):
            armor = self.__randomize_attribute(self.armor)
            enemy_attack = self.__randomize_attribute(enemy.attack)
            lost_hp = enemy_attack - armor
            death_damage = self.hp - lost_hp

            if death_damage < 0:
                enemy_attack += death_damage
                self.hp = 0
            else:
                self.hp -= lost_hp

            print(self.name
                  + f' (current hp: {self.hp}, lost {enemy_attack - armor} hp'
                  + f' ({enemy_attack} damage - {armor} armor) by'
                  + f' {enemy.name}.')

            return self.is_alive()

    def __randomize_attribute(self, attribute):
        """Retrun a pseudo-random value with padding of a given attribute.

        Provide a little pseudo-randomness of the game.
        """

        return random.randint(attribute - self.__prng_spread,
                              attribute + self.__prng_spread)


all = {'Knight': __Character(name='Knight', hp=90, attack=17, armor=7,
                             speed=2),
       'Oathbreaker': __Character(name='Oathbreaker', hp=60, attack=14,
                                  armor=2, speed=4),
       'Wizard': __Character(name='Wizard', hp=120, attack=10, armor=11,
                             speed=3)}
