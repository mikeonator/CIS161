# Michael Audi - CIS161 Week 10 Main Assignment

class SolarObject:
    def __init__(self, FarthestSunDistance: float, Spin: str, OrbitDays: int):
        '''
        Intialize class SolarObject containing:
        Farthest distance from the sun in au
        spin
        and the time to orbit whatever it is orbiting(average) in days.
        '''
        self.FarthestSunDistance: float = FarthestSunDistance
        self.Spin: str = Spin
        self.OrbitDays: int = OrbitDays

    def colonization(self):
        '''
        return the colonization potential of the SolarObject.
        (i had to do the type ignore thing to get my linter to stop freaking)
        '''
        return round((6000000000 / float(self.FarthestSunDistance)), 2)  # type: ignore


def main():
    return


if __name__ == "__main__":
    main()
