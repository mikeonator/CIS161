# Michael Audi - CIS161 Week 10 Main Assignment

class SolarObject:
    def __init__(self, FarthestSunDistance: float, OrbitDays: int):
        '''
        Intialize class SolarObject containing:
        Farthest distance from the sun in au,
        spin,
        and the time to orbit whatever it is orbiting(average) in days.
        '''
        self.FarthestSunDistance: float = FarthestSunDistance
        self.OrbitDays: int = OrbitDays

    def colonization(self):
        '''
        return the colonization potential of the SolarObject.
        600,000,000 / distance from sun

        (i had to do the type ignore thing to get my linter to stop freaking)
        '''
        return round((6000000000 / float(self.FarthestSunDistance)), 2)  # type: ignore

    def spin(self):
        '''
        does nothing lol (gets overidden later)
        '''
        pass


class Planet(SolarObject):
    def __init__(self, FarthestSunDistance: float, OrbitDays: int):
        '''
        init planet w all solarobject attributes
        '''
        super().__init__(FarthestSunDistance, OrbitDays)

    def spin(self):  # type: ignore
        '''
        returns spin
        '''
        return "slightly elliptical"


class Comet(SolarObject):
    def __init__(self, FarthestSunDistance: float, OrbitDays: int):
        '''
        init comet w all solarobject attributes
        '''
        super().__init__(FarthestSunDistance, OrbitDays)

    def spin(self):  # type: ignore
        '''
        returns spin
        '''
        return "like crazy"


def main():

    Earth = Planet(1, 365)
    Mars = Planet(1.524, 687)
    HalleyComet = Comet(35.98, 27740)
    HaleBopp = Comet(362, 900000)

    print(f"Earth:")
    print(f"    Colonization Potential: {Earth.colonization():,.0f} people")
    print(
        f"    Furthest Distance from the Sun: {Earth.FarthestSunDistance} au")
    print(f"    Orbital Period: {Earth.OrbitDays} days")
    print(f"    Spin: {Earth.spin()}")

    print(f"Mars:")
    print(f"    Colonization Potential: {Mars.colonization():,.0f} people")
    print(f"    Furthest Distance from the Sun: {Mars.FarthestSunDistance} au")
    print(f"    Orbital Period: {Mars.OrbitDays} days")
    print(f"    Spin: {Mars.spin()}")

    print(f"Halley's Comet:")
    print(
        f"    Colonization Potential: {HalleyComet.colonization():,.0f} people")
    print(
        f"    Furthest Distance from the Sun: {HalleyComet.FarthestSunDistance} au")
    print(f"    Orbital Period: {HalleyComet.OrbitDays/365.25:,.2f} years")
    print(f"    Spin: {HalleyComet.spin()}")

    print(f"Hale Bopp:")
    print(f"    Colonization Potential: {HaleBopp.colonization():,.0f} people")
    print(
        f"    Furthest Distance from the Sun: {HaleBopp.FarthestSunDistance} au")
    print(f"    Orbital Period: {HaleBopp.OrbitDays/365.25:,.2f} years")
    print(f"    Spin: {HaleBopp.spin()}")

    return


if __name__ == "__main__":
    main()
