# Michael Audi CIS161 Final Test Code Answer

class Character():
    def __init__(self, name, health=10):
        '''initializes character name and health '''
        self.name = name
        self.health = health

    def health_report(self):
        ''' prints object name and health value '''
        print(f"{self.name} has {self.health} health.")

    def spell(self):
        ''' passthrough '''
        pass


class Witch(Character):
    def __init__(self, name, health=10):
        ''' inherits properties from parent '''
        super().__init__(name, health)

    def spell(self):
        ''' prints "Swoosh!" and subtracts 1 from health '''
        print(f"{self.name} uses Swoosh!")
        self.health -= 1


class Warlock(Character):
    def __init__(self, name, health=10):
        ''' inherits properties from parent '''
        super().__init__(name, health)

    def spell(self):
        ''' prints "Kaboom!" and subtracts 2 from health '''
        print(f"{self.name} uses Kaboom!")
        self.health -= 2


def main():
    # I loved the show Merlin as a Kid and this whole time my brain
    # is just hearing John Hurt go "Young Warlock!" so you'll have
    # to forgive my renaming
    Merlin = Warlock("Merlin")

    Glenda = Witch("Glenda", 15)

    # Witch Spellcasting sequence
    Glenda.spell()
    Glenda.health_report()
    Glenda.spell()
    Glenda.health_report()
    Glenda.spell()
    Glenda.health_report()

    # Warlock Spellcasting sequence
    Merlin.spell()
    Merlin.health_report()
    Merlin.spell()
    Merlin.health_report()
    Merlin.spell()
    Merlin.health_report()
    return


if __name__ == "__main__":
    main()
