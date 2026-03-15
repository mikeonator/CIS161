# Michael Audi - CIS161 Week 10 Main Assignment

class SolarObject:
    def __init__(self, FarthestSunDistance: float, OrbitDays: int):
        '''
        Intialize class SolarObject containing:
        Farthest distance from the sun in au
        spin
        and the time to orbit whatever it is orbiting(average) in days.
        '''
        self.FarthestSunDistance: float = FarthestSunDistance
        self.OrbitDays: int = OrbitDays

    def colonization(self):
        '''
        return the colonization potential of the SolarObject.
        (i had to do the type ignore thing to get my linter to stop freaking)
        '''
        return round((6000000000 / float(self.FarthestSunDistance)), 2)  # type: ignore

    def spin(self):
        pass


class Planet(SolarObject):
    def __init__(self, FarthestSunDistance: float, OrbitDays: int):
        super().__init__(FarthestSunDistance, OrbitDays)

    def spin(self):  # type: ignore
        return "slightly elliptical"


class Comet(SolarObject):
    def __init__(self, FarthestSunDistance: float, OrbitDays: int):
        super().__init__(FarthestSunDistance, OrbitDays)

    def spin(self):  # type: ignore
        return "like crazy"


def main():

    Earth = Planet(1, 365)
    Mars = Planet(1.524, 687)

    return


if __name__ == "__main__":
    main()
