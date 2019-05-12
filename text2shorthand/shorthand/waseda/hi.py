import math
from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    tensioncurve,
    controlcurve,
    curve)

class CharHi(WasedaChar):
    def __init__(self, name='hi', kana='ひ',
                 model='SEL8CL1', head_type='SEL',
                 tail_type='SELCL1'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_pos_kyou(self):
        return super().get_pos_kyou() + P(0, 1)

    @classmethod
    def path_SELCL(cls, ta=None, **kwargs):
        #M 47.3414,58.6772 C 47.3414,69.3019 50.1663,75.08 59.7018,75.08 60.8169,75.08 61.1959,74.4327 61.0897,73.8304 60.994,73.2263 60.4401,72.6888 59.7299,72.9473 58.6772,73.3514 57.729253,74.157718 56.865553,74.882518

        z0 = P(0, -0)
        c0 = P(0, -3.73416)
        c1 = P(0.992839, -5.76493)
        z1 = P(4.34418, -5.76493)
        c2 = P(4.7361, -5.76493)
        c3 = P(4.8693, -5.53743)
        z2 = P(4.83198, -5.32574)
        c4 = P(4.79834, -5.11342)
        c5 = P(4.60367, -4.92452)
        z3 = P(4.35406, -5.01537)
        c6 = P(3.98408, -5.15739)
        c7 = P(3.65091, -5.44078)
        z4 = P(3.34736, -5.69552)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.73416)
        #z1 = z0 + P(4.34418, -5.76493)
        #c1 = z1 + P(-3.35135, 0)
        #c2 = z1 + P(0.391913, 0)
        #z2 = z1 + P(0.487791, 0.439184)
        #c3 = z2 + P(0.037325, -0.211684)
        #c4 = z2 + P(-0.0336347, 0.212317)
        #z3 = z2 + P(-0.477915, 0.310374)
        #c5 = z3 + P(0.249607, 0.0908524)
        #c6 = z3 + P(-0.369982, -0.142025)
        #z4 = z3 + P(-1.0067, -0.680151)
        #c7 = z4 + P(0.303556, 0.254738)

        #z0 = P(0, -0)
        #c0 = z0 + PP(3.73416, -90)
        #z1 = z0 + PP(7.21847, -52)
        #c1 = z1 + PP(3.35135, 180)
        #c2 = z1 + PP(0.391913, 0)
        #z2 = z1 + PP(0.656371, 41)
        #c3 = z2 + PP(0.21495, -80)
        #c4 = z2 + PP(0.214965, 99)
        #z3 = z2 + PP(0.569855, 146)
        ##z3 = z4 - PP(1.21493, ta + -5)
        #c5 = z3 + PP(0.265627, 20)
        #c6 = z3 + PP(0.396305, -158)
        ##z4 = z3 + PP(1.21493, -145)
        #c7 = z4 + PP(0.39628, 40)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

    @classmethod
    def path_SELCLe(cls, ta=None, **kwargs):
        #M 58.68,540.152 C 58.68,550.697 61.7659,556.215 71.2302,556.215 72.3371,556.215 72.466741,555.59513 72.6292,554.999 72.802592,554.36275 72.593155,553.41323 72.000984,553.12304 71.101644,552.68233 69.121523,553.11413 69.1648,554.11471 69.216301,555.30543 71.1894,554.999 72.6292,554.999

        #z0 = P(0, -0)
        #c0 = P(0, -3.72004)
        #c1 = P(1.08864, -5.66667)
        #z1 = P(4.42743, -5.66667)
        #c2 = P(4.81792, -5.66667)
        #c3 = P(4.86366, -5.44799)
        #z2 = P(4.92097, -5.23769)
        #c4 = P(4.98214, -5.01324)
        #c5 = P(4.90825, -4.67827)
        #z3 = P(4.69935, -4.57589)
        #c6 = P(4.38208, -4.42042)
        #c7 = P(3.68354, -4.57275)
        #z4 = P(3.6988, -4.92573)
        #c8 = P(3.71697, -5.34579)
        #c9 = P(4.41304, -5.23769)
        z5 = P(4.92097, -5.23769)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.72004)
        #z1 = z0 + P(4.42743, -5.66667)
        #c1 = z1 + P(-3.33879, 0)
        #c2 = z1 + P(0.39049, 0)
        #z2 = z1 + P(0.493536, 0.428978)
        #c3 = z2 + P(-0.0573119, -0.210301)
        #c4 = z2 + P(0.0611688, 0.224455)
        #z3 = z2 + P(-0.221621, 0.661797)
        #c5 = z3 + P(0.208905, -0.102373)
        #c6 = z3 + P(-0.317267, 0.155473)
        #z4 = z3 + P(-1.00054, -0.349839)
        #c7 = z4 + P(-0.0152672, 0.352982)
        #c8 = z4 + P(0.0181684, -0.42006)
        #z5 = z4 + P(1.22216, -0.311958)
        #c9 = z5 + P(-0.507929, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(3.72004, -90)
        z1 = z0 + PP(7.1912, -51)
        c1 = z1 + PP(3.33879, 180)
        c2 = z1 + PP(0.39049, 0)
        z2 = z1 + PP(0.653911, 40)
        c3 = z2 + PP(0.217971, -105)
        c4 = z2 + PP(0.232641, 74)
        z3 = z2 + PP(0.697919, 108)
        c5 = z3 + PP(0.23264, -26)
        c6 = z3 + PP(0.353313, 153)
        #z4 = z3 + PP(1.05994, -160)
        z4 = z5 - PP(1.26135, ta + -14)
        c7 = z4 + PP(0.353312, 92)
        #c8 = z4 + PP(0.420452, -87)
        #z5 = z4 + PP(1.26135, -14)
        #c9 = z5 + PP(0.507929, 180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_SELCLer(cls, ta=None, **kwargs):
        #M 157.033,131.515 C 157.033,142.1 159.847,147.856 169.347,147.856 170.458,147.856 170.74627,147.22106 170.73,146.611 170.67771,144.65054 167.44443,145.25043 167.44015,146.62098 167.43435,148.47762 169.2055,146.90413 170.59824,146.00674

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989008, -5.74321)
        #z1 = P(4.32788, -5.74321)
        #c2 = P(4.71835, -5.74321)
        #c3 = P(4.81966, -5.52005)
        #z2 = P(4.81395, -5.30564)
        #c4 = P(4.79557, -4.61662)
        #c5 = P(3.6592, -4.82745)
        #z3 = P(3.6577, -5.30915)
        #c6 = P(3.65566, -5.96168)
        #c7 = P(4.27815, -5.40866)
        z4 = P(4.76764, -5.09327)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32788, -5.74321)
        #c1 = z1 + P(-3.33887, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.486069, 0.437568)
        #c3 = z2 + P(0.00571825, -0.214412)
        #c4 = z2 + P(-0.0183778, 0.689023)
        #z3 = z2 + P(-1.15625, -0.00350757)
        #c5 = z3 + P(0.00150425, 0.481693)
        #c6 = z3 + P(-0.00203847, -0.652534)
        #z4 = z3 + P(1.10994, 0.215881)
        #c7 = z4 + P(-0.489492, -0.315397)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19131, -52)
        c1 = z1 + PP(3.33887, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.65401, 41)
        c3 = z2 + PP(0.214488, -88)
        c4 = z2 + PP(0.689268, 91)
        #z3 = z2 + PP(1.15626, -179)
        z3 = z4 - PP(1.13074, ta + 338)
        c5 = z3 + PP(0.481696, 89)
        #c6 = z3 + PP(0.652538, -90)
        #z4 = z3 + PP(1.13074, 11)
        #c7 = z4 + PP(0.582304, -147)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLel(cls, ta=None, **kwargs):
        #M 107.856,131.515 C 107.856,142.1 110.671,147.856 120.171,147.856 121.282,147.856 121.83225,146.87222 121.83225,146.26194 121.83225,145.14326 120.16584,144.33832 119.14127,144.90561 117.97696,145.55027 120.32094,146.76817 121.36854,147.34231

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.98936, -5.74321)
        #z1 = P(4.32823, -5.74321)
        #c2 = P(4.7187, -5.74321)
        #c3 = P(4.91209, -5.39745)
        #z2 = P(4.91209, -5.18296)
        #c4 = P(4.91209, -4.78979)
        #c5 = P(4.32641, -4.50688)
        #z3 = P(3.96632, -4.70626)
        #c6 = P(3.55711, -4.93283)
        #c7 = P(4.38093, -5.36088)
        z4 = P(4.74912, -5.56266)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32823, -5.74321)
        #c1 = z1 + P(-3.33887, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.583863, 0.560248)
        #c3 = z2 + P(0, -0.214489)
        #c4 = z2 + P(0, 0.393171)
        #z3 = z2 + P(-0.945771, 0.476696)
        #c5 = z3 + P(0.360095, 0.19938)
        #c6 = z3 + P(-0.409208, -0.226572)
        #z4 = z3 + P(0.782796, -0.856402)
        #c7 = z4 + P(-0.368189, 0.201787)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19152, -52)
        c1 = z1 + PP(3.33887, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.809181, 43)
        c3 = z2 + PP(0.214489, -90)
        c4 = z2 + PP(0.393171, 90)
        #z3 = z2 + PP(1.05911, 153)
        z3 = z4 - PP(1.16026, ta + -18)
        c5 = z3 + PP(0.411608, 28)
        #c6 = z3 + PP(0.467746, -151)
        #z4 = z3 + PP(1.16026, -47)
        #c7 = z4 + PP(0.419859, 151)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLne(cls, ta=None, **kwargs):
        #M 47.3414,204.353 C 47.3414,214.938 50.1558,220.694 59.6556,220.694 60.7666,220.694 61.0384,220.05826 61.0384,219.449 61.0384,217.84696 58.046374,219.47673 56.83,220.497

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989149, -5.74321)
        #z1 = P(4.32795, -5.74321)
        #c2 = P(4.71842, -5.74321)
        #c3 = P(4.81395, -5.51977)
        #z2 = P(4.81395, -5.30564)
        #c4 = P(4.81395, -4.74259)
        #c5 = P(3.76237, -5.31538)
        z3 = P(3.33486, -5.67397)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32795, -5.74321)
        #c1 = z1 + P(-3.3388, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.485999, 0.437568)
        #c3 = z2 + P(0, -0.21413)
        #c4 = z2 + P(0, 0.563053)
        #z3 = z2 + P(-1.47908, -0.36833)
        #c5 = z3 + P(0.427507, 0.358584)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19135, -52)
        c1 = z1 + PP(3.3388, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.653957, 41)
        #z2 = z3 - PP(1.52426, ta + -25)
        c3 = z2 + PP(0.21413, -90)
        #c4 = z2 + PP(0.563053, 90)
        #z3 = z2 + PP(1.52426, -166)
        #c5 = z3 + PP(0.557982, 39)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta+180)])

    @classmethod
    def path_SELCLner(cls, ta=None, **kwargs):
        #M140.863 204.353C140.863 214.938 143.677 220.694 153.177 220.694C154.288 220.694 154.665 220.049 154.559 219.449C154.464 218.847 153.912 218.312 153.205 218.569C152.156 218.972 151.212 219.775 150.351 220.497

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989008, -5.74321)
        #z1 = P(4.32788, -5.74321)
        #c2 = P(4.71835, -5.74321)
        #c3 = P(4.85085, -5.51651)
        #z2 = P(4.81359, -5.30564)
        #c4 = P(4.78021, -5.09406)
        #c5 = P(4.5862, -4.90603)
        #z3 = P(4.33772, -4.99635)
        #c6 = P(3.96904, -5.13799)
        #c7 = P(3.63726, -5.42021)
        z4 = P(3.33465, -5.67397)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32788, -5.74321)
        #c1 = z1 + P(-3.33887, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.485718, 0.437568)
        #c3 = z2 + P(0.0372547, -0.210876)
        #c4 = z2 + P(-0.0333887, 0.211579)
        #z3 = z2 + P(-0.475877, 0.309285)
        #c5 = z3 + P(0.248482, 0.0903252)
        #c6 = z3 + P(-0.368681, -0.141638)
        #z4 = z3 + P(-1.00307, -0.677615)
        #c7 = z4 + P(0.302607, 0.253754)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19131, -52)
        c1 = z1 + PP(3.33887, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.653748, 42)
        c3 = z2 + PP(0.214141, -79)
        c4 = z2 + PP(0.214197, 98)
        z3 = z2 + PP(0.567552, 146)
        #z3 = z4 - PP(1.2105, ta + -4)
        c5 = z3 + PP(0.26439, 19)
        c6 = z3 + PP(0.394952, -158)
        #z4 = z3 + PP(1.2105, -145)
        c7 = z4 + PP(0.39492, 39)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

    @classmethod
    def path_SELCLnel(cls, ta=None, **kwargs):
        #M 94.4673,204.353 C 94.4673,214.938 97.2817,220.694 106.782,220.694 107.892,220.694 108.15506,220.05823 108.164,219.449 108.17302,218.8345 107.53756,217.95101 106.86465,217.89487 106.17168,217.83706 105.06126,218.59137 105.27987,219.25149 105.58282,220.16626 107.31676,219.63395 108.164,219.449

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989149, -5.74321)
        #z1 = P(4.32812, -5.74321)
        #c2 = P(4.71824, -5.74321)
        #c3 = P(4.8107, -5.51976)
        #z2 = P(4.81384, -5.30564)
        #c4 = P(4.81701, -5.08967)
        #c5 = P(4.59367, -4.77915)
        #z3 = P(4.35717, -4.75942)
        #c6 = P(4.11362, -4.73911)
        #c7 = P(3.72335, -5.00422)
        #z4 = P(3.80018, -5.23622)
        #c8 = P(3.90666, -5.55773)
        #c9 = P(4.51607, -5.37064)
        z5 = P(4.81384, -5.30564)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32812, -5.74321)
        #c1 = z1 + P(-3.33897, 0)
        #c2 = z1 + P(0.39012, 0)
        #z2 = z1 + P(0.485718, 0.437568)
        #c3 = z2 + P(-0.00314205, -0.21412)
        #c4 = z2 + P(0.00317017, 0.215972)
        #z3 = z2 + P(-0.456669, 0.546214)
        #c5 = z3 + P(0.236501, -0.019731)
        #c6 = z3 + P(-0.243551, 0.0203179)
        #z4 = z3 + P(-0.556987, -0.476797)
        #c7 = z4 + P(-0.0768326, 0.232006)
        #c8 = z4 + P(0.106475, -0.321505)
        #z5 = z4 + P(1.01366, -0.0694168)
        #c9 = z5 + P(-0.297771, -0.0650025)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19146, -52)
        c1 = z1 + PP(3.33897, 180)
        c2 = z1 + PP(0.39012, 0)
        z2 = z1 + PP(0.653748, 42)
        c3 = z2 + PP(0.214143, -90)
        c4 = z2 + PP(0.215995, 89)
        z3 = z2 + PP(0.711967, 129)
        c5 = z3 + PP(0.237323, -4)
        c6 = z3 + PP(0.244397, 175)
        #z4 = z3 + PP(0.733192, -139)
        z4 = z5 - PP(1.01603, ta + 344)
        c7 = z4 + PP(0.244397, 108)
        #c8 = z4 + PP(0.338677, -71)
        #z5 = z4 + PP(1.01603, -3)
        #c9 = z5 + PP(0.304783, -167)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            #controlcurve(c8, c9),
            curve(),
            endknot(*z5, angle=ta)])

    @classmethod
    def path_SELCLs(cls, ta=None, **kwargs):
        #M 258.905,131.515 C 258.905,142.06 261.991,147.578 271.455,147.578 272.562,147.578 272.854,146.969 272.854,146.362 272.854,144.685 271.37502,143.88342 270.80102,144.47742 270.13602,145.16642 270.41883,146.60383 270.41883,147.55483

        #z0 = P(0, -0)
        #c0 = P(0, -3.72004)
        #c1 = P(1.08867, -5.66667)
        #z1 = P(4.42736, -5.66667)
        #c2 = P(4.81789, -5.66667)
        #c3 = P(4.9209, -5.45183)
        #z2 = P(4.9209, -5.23769)
        #c4 = P(4.9209, -4.64608)
        #c5 = P(4.39915, -4.3633)
        #z3 = P(4.19665, -4.57285)
        #c6 = P(3.96205, -4.81592)
        #c7 = P(4.06182, -5.323)
        z4 = P(4.06182, -5.6585)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.72004)
        #z1 = z0 + P(4.42736, -5.66667)
        #c1 = z1 + P(-3.33869, 0)
        #c2 = z1 + P(0.390525, 0)
        #z2 = z1 + P(0.493536, 0.428978)
        #c3 = z2 + P(0, -0.214136)
        #c4 = z2 + P(0, 0.591608)
        #z3 = z2 + P(-0.724246, 0.664838)
        #c5 = z3 + P(0.202494, 0.20955)
        #c6 = z3 + P(-0.234597, -0.243064)
        #z4 = z3 + P(-0.134828, -1.08564)
        #c7 = z4 + P(0, 0.335492)

        z0 = P(0, -0)
        c0 = z0 + PP(3.72004, -90)
        z1 = z0 + PP(7.19115, -51)
        c1 = z1 + PP(3.33869, 180)
        c2 = z1 + PP(0.390525, 0)
        z2 = z1 + PP(0.653911, 40)
        c3 = z2 + PP(0.214136, -90)
        c4 = z2 + PP(0.591608, 90)
        #z3 = z2 + PP(0.983128, 137)
        z3 = z4 - PP(1.09398, ta + -7)
        c5 = z3 + PP(0.291402, 45)
        #c6 = z3 + PP(0.33781, -133)
        #z4 = z3 + PP(1.09398, -97)
        #c7 = z4 + PP(0.335492, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLsl(cls, ta=None, **kwargs):
        #M 99.3525,262.614 C 99.3525,273.199 102.167,278.955 111.667,278.955 112.48649,278.955 113.02434,278.54498 113.02434,277.75025 113.02434,275.49291 109.47888,277.52329 108.841,278.758

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989184, -5.74321)
        #z1 = P(4.32805, -5.74321)
        #c2 = P(4.61607, -5.74321)
        #c3 = P(4.8051, -5.5991)
        #z2 = P(4.8051, -5.31978)
        #c4 = P(4.8051, -4.52642)
        #c5 = P(3.55902, -5.24002)
        z3 = P(3.33483, -5.67397)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32805, -5.74321)
        #c1 = z1 + P(-3.33887, 0)
        #c2 = z1 + P(0.288018, 0)
        #z2 = z1 + P(0.477051, 0.423421)
        #c3 = z2 + P(0, -0.279316)
        #c4 = z2 + P(0, 0.793364)
        #z3 = z2 + P(-1.47028, -0.354184)
        #c5 = z3 + P(0.224189, 0.433951)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19142, -52)
        c1 = z1 + PP(3.33887, 180)
        c2 = z1 + PP(0.288018, 0)
        #z2 = z1 + PP(0.637858, 41)
        z2 = z3 - PP(1.51234, ta + -48)
        c3 = z2 + PP(0.279316, -90)
        #c4 = z2 + PP(0.793364, 90)
        #z3 = z2 + PP(1.51234, -166)
        #c5 = z3 + PP(0.488441, 62)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SELCLsr(cls, ta=None, **kwargs):
        #M 151.364,262.614 C 151.364,273.199 154.178,278.955 163.678,278.955 164.789,278.955 165.16146,278.5635 165.061,277.71 164.96046,276.85582 163.20767,275.9803 162.50351,276.35629 161.45161,276.91797 162.40638,277.82898 163.29446,278.95181

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989008, -5.74321)
        #z1 = P(4.32788, -5.74321)
        #c2 = P(4.71835, -5.74321)
        #c3 = P(4.84925, -5.60561)
        #z2 = P(4.81395, -5.30564)
        #c4 = P(4.77861, -5.00543)
        #c5 = P(4.16257, -4.69772)
        #z3 = P(3.91509, -4.82986)
        #c6 = P(3.54539, -5.02727)
        #c7 = P(3.88095, -5.34745)
        z4 = P(4.19308, -5.74208)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32788, -5.74321)
        #c1 = z1 + P(-3.33887, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.486069, 0.437568)
        #c3 = z2 + P(0.0353077, -0.299971)
        #c4 = z2 + P(-0.0353358, 0.30021)
        #z3 = z2 + P(-0.898855, 0.475775)
        #c5 = z3 + P(0.247484, 0.132145)
        #c6 = z3 + P(-0.369701, -0.197408)
        #z4 = z3 + P(0.277987, -0.912221)
        #c7 = z4 + P(-0.312124, 0.39463)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19131, -52)
        c1 = z1 + PP(3.33887, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.65401, 41)
        c3 = z2 + PP(0.302042, -83)
        c4 = z2 + PP(0.302282, 96)
        #z3 = z2 + PP(1.01701, 152)
        z3 = z4 - PP(0.953637, ta + -21)
        c5 = z3 + PP(0.280554, 28)
        #c6 = z3 + PP(0.419104, -151)
        #z4 = z3 + PP(0.953637, -73)
        #c7 = z4 + PP(0.503144, 128)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLse(cls, ta=None, **kwargs):
        #M 47.3414,358.129 C 47.3414,368.714 50.1558,374.47 59.6556,374.47 60.7666,374.47 61.0384,373.83426 61.0384,373.225 61.0384,372.1495 59.275595,371.25827 58.570885,371.5231 57.519223,371.9183 59.105359,373.65736 59.6556,374.47

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989149, -5.74321)
        #z1 = P(4.32795, -5.74321)
        #c2 = P(4.71842, -5.74321)
        #c3 = P(4.81395, -5.51977)
        #z2 = P(4.81395, -5.30564)
        #c4 = P(4.81395, -4.92764)
        #c5 = P(4.19439, -4.61441)
        #z3 = P(3.94671, -4.70749)
        #c6 = P(3.5771, -4.84639)
        #c7 = P(4.13456, -5.4576)
        z4 = P(4.32795, -5.74321)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32795, -5.74321)
        #c1 = z1 + P(-3.3388, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.485999, 0.437568)
        #c3 = z2 + P(0, -0.21413)
        #c4 = z2 + P(0, 0.377995)
        #z3 = z2 + P(-0.867233, 0.59815)
        #c5 = z3 + P(0.247677, 0.0930771)
        #c6 = z3 + P(-0.369617, -0.138897)
        #z4 = z3 + P(0.381234, -1.03572)
        #c7 = z4 + P(-0.193388, 0.28561)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19135, -52)
        c1 = z1 + PP(3.3388, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.653957, 41)
        c3 = z2 + PP(0.21413, -90)
        c4 = z2 + PP(0.377995, 90)
        #z3 = z2 + PP(1.05351, 145)
        z3 = z4 - PP(1.10365, ta + -13)
        c5 = z3 + PP(0.264589, 20)
        #c6 = z3 + PP(0.394853, -159)
        #z4 = z3 + PP(1.10365, -69)
        #c7 = z4 + PP(0.344923, 124)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLser(cls, ta=None, **kwargs):
        #M 90.8486,358.129 C 90.8486,368.714 93.6629,374.47 103.163,374.47 104.274,374.47 104.57677,373.83334 104.546,373.225 104.47312,371.78403 101.00115,371.35458 100.85889,372.23568 100.66849,373.41493 102.7074,373.8678 103.7048,374.4076

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989114, -5.74321)
        #z1 = P(4.32802, -5.74321)
        #c2 = P(4.71849, -5.74321)
        #c3 = P(4.8249, -5.51945)
        #z2 = P(4.81409, -5.30564)
        #c4 = P(4.78847, -4.7992)
        #c5 = P(3.56821, -4.64826)
        #z3 = P(3.51822, -4.95793)
        #c6 = P(3.4513, -5.37239)
        #c7 = P(4.16789, -5.53156)
        z4 = P(4.51844, -5.72127)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32802, -5.74321)
        #c1 = z1 + P(-3.3389, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.486069, 0.437568)
        #c3 = z2 + P(0.0108144, -0.213807)
        #c4 = z2 + P(-0.0256144, 0.506443)
        #z3 = z2 + P(-1.29587, 0.347706)
        #c5 = z3 + P(0.0499987, 0.309671)
        #c6 = z3 + P(-0.066918, -0.414459)
        #z4 = z3 + P(1.00022, -0.763343)
        #c7 = z4 + P(-0.350546, 0.189718)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19139, -52)
        c1 = z1 + PP(3.3389, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.65401, 41)
        c3 = z2 + PP(0.21408, -87)
        c4 = z2 + PP(0.50709, 92)
        #z3 = z2 + PP(1.34171, 164)
        z3 = z4 - PP(1.25823, ta + -8)
        c5 = z3 + PP(0.313682, 80)
        #c6 = z3 + PP(0.419827, -99)
        #z4 = z3 + PP(1.25823, -37)
        #c7 = z4 + PP(0.398592, 151)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLsel(cls, ta=None, **kwargs):
        #M 140.025,358.129 C 140.025,368.714 142.839,374.47 152.339,374.47 153.45,374.47 153.78658,373.83086 153.722,373.225 153.65792,372.6239 153.26897,371.40064 152.47631,371.57978 151.38021,371.82751 150.71553,373.35163 150.62075,374.40158

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989008, -5.74321)
        #z1 = P(4.32788, -5.74321)
        #c2 = P(4.71835, -5.74321)
        #c3 = P(4.83664, -5.51857)
        #z2 = P(4.81395, -5.30564)
        #c4 = P(4.79142, -5.09438)
        #c5 = P(4.65472, -4.66445)
        #z3 = P(4.37614, -4.72741)
        #c6 = P(3.9909, -4.81448)
        #c7 = P(3.75729, -5.35014)
        z4 = P(3.72398, -5.71916)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32788, -5.74321)
        #c1 = z1 + P(-3.33887, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.486069, 0.437568)
        #c3 = z2 + P(0.0226973, -0.212935)
        #c4 = z2 + P(-0.0225215, 0.211263)
        #z3 = z2 + P(-0.43781, 0.578229)
        #c5 = z3 + P(0.278588, 0.0629605)
        #c6 = z3 + P(-0.385235, -0.0870672)
        #z4 = z3 + P(-0.652155, -0.991749)
        #c7 = z4 + P(0.0333114, 0.369015)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19131, -52)
        c1 = z1 + PP(3.33887, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.65401, 41)
        c3 = z2 + PP(0.214142, -83)
        c4 = z2 + PP(0.21246, 96)
        #z3 = z2 + PP(0.725277, 127)
        z3 = z4 - PP(1.18696, ta + -27)
        c5 = z3 + PP(0.285614, 12)
        #c6 = z3 + PP(0.394952, -167)
        #z4 = z3 + PP(1.18696, -123)
        #c7 = z4 + PP(0.370516, 84)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLsw(cls, ta=None, **kwargs):
        #M 47.3414,447.917 C 47.3414,458.502 50.1558,464.258 59.6556,464.258 60.7666,464.258 60.949914,463.41631 60.938405,462.80728 60.914052,461.51865 59.985014,461.08877 59.498616,461.84565 59.065229,462.52004 58.888305,463.2158 58.438665,464.22457

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989149, -5.74321)
        #z1 = P(4.32795, -5.74321)
        #c2 = P(4.71842, -5.74321)
        #c3 = P(4.78285, -5.44739)
        #z2 = P(4.7788, -5.23334)
        #c4 = P(4.77024, -4.78043)
        #c5 = P(4.44372, -4.62935)
        #z3 = P(4.27277, -4.89536)
        #c6 = P(4.12046, -5.13238)
        #c7 = P(4.05827, -5.37691)
        z4 = P(3.90024, -5.73146)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32795, -5.74321)
        #c1 = z1 + P(-3.3388, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.450854, 0.50987)
        #c3 = z2 + P(0.00404495, -0.21405)
        #c4 = z2 + P(-0.0085591, 0.452902)
        #z3 = z2 + P(-0.506028, 0.337974)
        #c5 = z3 + P(0.170949, 0.266013)
        #c6 = z3 + P(-0.152318, -0.237021)
        #z4 = z3 + P(-0.37253, -0.836095)
        #c7 = z4 + P(0.15803, 0.354542)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19135, -52)
        c1 = z1 + PP(3.3388, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.680615, 48)
        c3 = z2 + PP(0.214088, -88)
        c4 = z2 + PP(0.452983, 91)
        #z3 = z2 + PP(0.608515, 146)
        z3 = z4 - PP(0.915332, ta + 1)
        c5 = z3 + PP(0.316207, 57)
        #c6 = z3 + PP(0.281744, -122)
        #z4 = z3 + PP(0.915332, -114)
        #c7 = z4 + PP(0.388167, 65)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLswr(cls, ta=None, **kwargs):
        #M 95.4745,447.917 C 95.4745,458.502 98.2888,464.258 107.789,464.258 108.9,464.258 109.32452,463.60263 109.171,463.013 108.9399,462.12543 106.98785,461.7753 106.4059,462.2124 105.83377,462.64212 106.54291,463.35992 106.85783,464.23871

        #z0 = P(0, -0)
        #c0 = P(0, -3.7202)
        #c1 = P(0.989114, -5.74321)
        #z1 = P(4.32805, -5.74321)
        #c2 = P(4.71852, -5.74321)
        #c3 = P(4.86773, -5.51287)
        #z2 = P(4.81377, -5.30564)
        #c4 = P(4.73255, -4.99369)
        #c5 = P(4.04648, -4.87064)
        #z3 = P(3.84195, -5.02426)
        #c6 = P(3.64087, -5.17529)
        #c7 = P(3.8901, -5.42757)
        z4 = P(4.00078, -5.73643)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7202)
        #z1 = z0 + P(4.32805, -5.74321)
        #c1 = z1 + P(-3.33894, 0)
        #c2 = z1 + P(0.390472, 0)
        #z2 = z1 + P(0.485718, 0.437568)
        #c3 = z2 + P(0.0539561, -0.207231)
        #c4 = z2 + P(-0.0812224, 0.311945)
        #z3 = z2 + P(-0.971822, 0.281379)
        #c5 = z3 + P(0.204532, 0.153623)
        #c6 = z3 + P(-0.201081, -0.151029)
        #z4 = z3 + P(0.158835, -0.712167)
        #c7 = z4 + P(-0.110682, 0.308859)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7202, -90)
        z1 = z0 + PP(7.19142, -52)
        c1 = z1 + PP(3.33894, 180)
        c2 = z1 + PP(0.390472, 0)
        z2 = z1 + PP(0.653748, 42)
        c3 = z2 + PP(0.21414, -75)
        c4 = z2 + PP(0.322346, 104)
        #z3 = z2 + PP(1.01174, 163)
        z3 = z4 - PP(0.729664, ta + -6)
        c5 = z3 + PP(0.2558, 36)
        #c6 = z3 + PP(0.251482, -143)
        #z4 = z3 + PP(0.729664, -77)
        #c7 = z4 + PP(0.328092, 109)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SELCLswl(cls, ta=None, **kwargs):
        #M 216.354,377.405 C 216.354,387.951 219.44,393.469 228.904,393.469 230.011,393.469 230.067,393.23202 230.067,392.62502 230.067,390.35063 226.75468,391.80911 224.35968,392.92611

        #z0 = P(0, -0)
        #c0 = P(0, -3.7065)
        #c1 = P(1.08461, -5.64585)
        #z1 = P(4.41082, -5.64585)
        #c2 = P(4.79989, -5.64585)
        #c3 = P(4.81957, -5.56256)
        #z2 = P(4.81957, -5.34923)
        #c4 = P(4.81957, -4.54987)
        #c5 = P(3.65542, -5.06247)
        z3 = P(2.81368, -5.45505)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.7065)
        #z1 = z0 + P(4.41082, -5.64585)
        #c1 = z1 + P(-3.32622, 0)
        #c2 = z1 + P(0.389066, 0)
        #z2 = z1 + P(0.408748, 0.296625)
        #c3 = z2 + P(0, -0.213336)
        #c4 = z2 + P(0, 0.799357)
        #z3 = z2 + P(-2.00589, -0.105821)
        #c5 = z3 + P(0.841746, 0.392581)

        z0 = P(0, -0)
        c0 = z0 + PP(3.7065, -90)
        z1 = z0 + PP(7.16456, -52)
        c1 = z1 + PP(3.32622, 180)
        c2 = z1 + PP(0.389066, 0)
        #z2 = z1 + PP(0.505036, 35)
        z2 = z3 - PP(2.00868, ta + -21)
        c3 = z2 + PP(0.213336, -90)
        #c4 = z2 + PP(0.799357, 90)
        #z3 = z2 + PP(2.00868, -176)
        #c5 = z3 + PP(0.928793, 25)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SELCLE(cls, ta=None, **kwargs):
        #M 193.929,131.515 C 193.929,142.06 197.293,147.357 206.757,147.357 207.864,147.357 208.37078,146.83276 208.53078,146.23576 208.71278,145.60176 208.71341,144.79197 208.20281,144.49627 207.34673,144.0005 205.35261,144.48272 205.39959,145.47088 205.45061,146.54409 207.44496,146.23576 208.53078,146.23576 209.57762,146.23576 210.76742,146.18377 211.671,146.27827

        #z0 = P(0, -0)
        #c0 = P(0, -3.72004)
        #c1 = P(1.18674, -5.58871)
        #z1 = P(4.52543, -5.58871)
        #c2 = P(4.91596, -5.58871)
        #c3 = P(5.09474, -5.40377)
        #z2 = P(5.15118, -5.19316)
        #c4 = P(5.21539, -4.9695)
        #c5 = P(5.21561, -4.68382)
        #z3 = P(5.03548, -4.5795)
        #c6 = P(4.73348, -4.40461)
        #c7 = P(4.03, -4.57472)
        #z4 = P(4.04657, -4.92332)
        #c8 = P(4.06457, -5.30193)
        #c9 = P(4.76813, -5.19316)
        #z5 = P(5.15118, -5.19316)
        #c10 = P(5.52049, -5.19316)
        #c11 = P(5.94022, -5.17482)
        z6 = P(6.25898, -5.20815)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.72004)
        #z1 = z0 + P(4.52543, -5.58871)
        #c1 = z1 + P(-3.33869, 0)
        #c2 = z1 + P(0.390525, 0)
        #z2 = z1 + P(0.62575, 0.395549)
        #c3 = z2 + P(-0.0564444, -0.210608)
        #c4 = z2 + P(0.0642056, 0.223661)
        #z3 = z2 + P(-0.115701, 0.613653)
        #c5 = z3 + P(0.180128, -0.104316)
        #c6 = z3 + P(-0.302006, 0.174897)
        #z4 = z3 + P(-0.988914, -0.343821)
        #c7 = z4 + P(-0.0165735, 0.348601)
        #c8 = z4 + P(0.0179987, -0.378605)
        #z5 = z4 + P(1.10461, -0.269833)
        #c9 = z5 + P(-0.383053, 0)
        #c10 = z5 + P(0.369302, 0)
        #z6 = z5 + P(1.1078, -0.0149966)
        #c11 = z6 + P(-0.318763, 0.0333375)

        z0 = P(0, -0)
        c0 = z0 + PP(3.72004, -90)
        z1 = z0 + PP(7.19119, -51)
        c1 = z1 + PP(3.33869, 180)
        c2 = z1 + PP(0.390525, 0)
        z2 = z1 + PP(0.740285, 32)
        c3 = z2 + PP(0.218041, -105)
        c4 = z2 + PP(0.232694, 73)
        z3 = z2 + PP(0.624465, 100)
        c5 = z3 + PP(0.208154, -30)
        c6 = z3 + PP(0.348993, 149)
        z4 = z3 + PP(1.04698, -160)
        c7 = z4 + PP(0.348995, 92)
        c8 = z4 + PP(0.379032, -87)
        z5 = z4 + PP(1.13709, -13)
        #z5 = z6 - PP(1.1079, ta + 6)
        c9 = z5 + PP(0.383053, 180)
        c10 = z5 + PP(0.369302, 0)
        z6 = z5 + PP(1.1079, 0)
        c11 = z6 + PP(0.320501, 174)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            #curve(),
            endknot(*z6)])

class CharHin(CharHi):
    def __init__(self, name='hin', kana='ひん',
                 model='SEL8CL1E1F', head_type='SEL',
                 tail_type='EF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_SELCLE()]

class CharHitsu(CharHi):
    def __init__(self, name='hitsu', kana='ひつ',
                 model='SEL8CL1SW1F', head_type='SEL',
                 tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {}

    @classmethod
    def path_SELCLSWF(cls, ta=None, **kwargs):
        #M 298.12,131.515 C 298.12,142.06 301.206,147.578 310.67,147.578 311.777,147.578 311.97479,146.75121 311.961,146.145 311.93179,144.86114 310.5188,144.24933 310.16599,145.09051 309.79963,145.964 309.45597,146.72052 309.176,147.54451 308.83939,148.5352 308.35474,149.48137 308.05286,150.3689
        z5 = P(3.50409, -6.65124)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -3.72004)
        #z1 = z0 + P(4.42736, -5.66667)
        #c1 = z1 + P(-3.33869, 0)
        #c2 = z1 + P(0.390525, 0)
        #z2 = z1 + P(0.455436, 0.505531)
        #c3 = z2 + P(0.00486481, -0.213857)
        #c4 = z2 + P(-0.0103046, 0.452917)
        #z3 = z2 + P(-0.63324, 0.372001)
        #c5 = z3 + P(0.124464, 0.29675)
        #c6 = z3 + P(-0.129244, -0.308148)
        #z4 = z3 + P(-0.349246, -0.865717)
        #c7 = z4 + P(0.0987672, 0.290685)
        #c8 = z4 + P(-0.118749, -0.349493)
        #z5 = z4 + P(-0.396219, -0.996382)
        #c9 = z5 + P(0.106497, 0.313101)

        z0 = P(0, -0)
        c0 = z0 + PP(3.72004, -90)
        z1 = z0 + PP(7.19115, -51)
        c1 = z1 + PP(3.33869, 180)
        c2 = z1 + PP(0.390525, 0)
        z2 = z1 + PP(0.680429, 47)
        c3 = z2 + PP(0.213913, -88)
        c4 = z2 + PP(0.453034, 91)
        z3 = z2 + PP(0.734423, 149)
        c5 = z3 + PP(0.321794, 67)
        c6 = z3 + PP(0.334154, -112)
        z4 = z3 + PP(0.933509, -111)
        #z4 = z5 - PP(1.07227, ta + -2)
        c7 = z4 + PP(0.307006, 71)
        c8 = z4 + PP(0.369116, -108)
        z5 = z4 + PP(1.07227, -111)
        c9 = z5 + PP(0.330717, 71)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

class CharHitsuyou(CharHitsu):
    def __init__(self, name='hitsuyou', kana='ひつよう',
                 model='SEL8CL1SW1F', head_type='SEL',
                 tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharHiro(CharHitsu):
    def __init__(self, name='hiro', kana='ひろ',
                 model='SEL8CL1SW1F', head_type='SEL',
                 tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)