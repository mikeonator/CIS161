# Michael Audi - CIS161 Week 10 Main Assignment

class SolarObject:
    def __init__(self, FarthestSunDistance, Spin, OrbitDays):
        '''
        Intialize class SolarObject containing:
        Farthest distance from the sun in au
        spin
        and the time to orbit whatever it is orbiting(average) in days.
        '''
        self.FarthestSunDistance = FarthestSunDistance
        self.Spin = Spin
        self.OrbitDays = OrbitDays
