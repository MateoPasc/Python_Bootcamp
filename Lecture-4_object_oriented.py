import numpy as np

class AstroObj:
    def __init__(self, name, ra, dec):

        self.name = name
        self.ra = ra
        self.dec = dec

    def angDist(self, other):

        ra1 = np.radians(self.ra)
        dec1 = np.radians(self.dec)

        ra2 = np.radians(other.ra)
        dec2 = np.radians(other.dec)

        ang = np.sin(dec1)*np.sin(dec2) + np.cos(dec1)*np.cos(dec2)*np.cos(ra1 - ra2)

        return np.degrees(np.arccos(ang))



venus = AstroObj('Venus', 15.4, -2.3)

print(venus.name)
print(venus.ra)

mars = AstroObj('Mars', 123.8, 6.1)

print(venus.angDist(mars))


class Star(AstroObj):
    def __init__(self, name, ra, dec, spec_type):

        AstroObj.__init__(self, name, ra, dec)

        self.spec_type = spec_type

        # This is calles "Class-inheritance". One class built on top of another.


sirius = Star('Sirius', 101.2875, -16.7161, 'A0')

print(sirius.angDist(venus))


class Galaxy(AstroObj):
    def __init__(self, name, ra, dec, z):

        AstroObj.__init__(self, name, ra, dec)

        self.z = z


g1 = Galaxy("NGC660", 25.7583, 13.645, 0.003)

print(sirius.angDist(g1))