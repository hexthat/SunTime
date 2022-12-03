import math
import time

Latitude = 36
Longitude = -119
timezone = -8
timesec = time.time()

def hrmn(time):
    hr = time * 24
    mn = hr - math.floor(hr)
    mn = int(round(mn * 60 / 100, 2)  * 100)
    return "{:02d}:{:02d}".format(math.floor(hr), mn)

def sunlight(Latitude, Longitude, timesec):
    E2 = 0.1/24
    # Julian Day
    JD = (timesec / 86400.0) + 2440587.5 + E2 - timezone/24
    # Julian Century
    JC = (JD-2451545)/36525
    # Geom Mean Long Sun (deg)
    GMLS = 280.46646+JC*(36000.76983+JC*0.0003032)
    GMLS = GMLS % 360
    # Geom Mean Anom Sun (deg)
    GMAS = 357.52911+JC*(35999.05029-0.0001537*JC)
    # Sun Eq of Ctr
    SEC = math.sin(math.radians(GMAS))*(1.914602-JC*(
        0.004817+0.000014*JC))+math.sin(math.radians(2*GMAS))*(
            0.019993-0.000101*JC)+math.sin(math.radians(3*GMAS))*0.000289
    # Sun True Long (deg)
    STL = GMLS + SEC
    # Sun True Anom (deg)
    SAL = STL-0.00569-0.00478*math.sin(math.radians(125.04-1934.136*JC))
    # Mean Obliq Ecliptic
    MOE = 23+(26+((21.448-JC*(46.815+JC*(0.00059-JC*0.001813))))/60)/60
    # Obliq Corr (deg)
    OC = MOE+0.00256*math.cos(math.radians(125.04-1934.136*JC))
    # Sun Declin
    SD = math.degrees(math.asin(math.sin(math.radians(OC))*math.sin(math.radians(SAL))))
    # HA sunrise (deg)
    sunrised = math.degrees(math.acos(math.cos(math.radians(90.833))/(
        math.cos(math.radians(Latitude))*math.cos(math.radians(SD)))-math.tan(
            math.radians(Latitude))*math.tan(math.radians(SD))))
    # Eccent Earth Orbit
    EEO = round(0.016708634 - JC * (0.000042037 + 0.0000001267 * JC), 2)
    vary = round(math.tan(math.radians(OC/2))*math.tan(math.radians(OC/2)), 2)
    # Eq of Time (minutes)
    ET = 4*math.degrees(vary*math.sin(2*math.radians(GMLS))-2*EEO*math.sin(math.radians(
        GMAS))+4*EEO*vary*math.sin(math.radians(GMAS))*math.cos(2*math.radians(GMLS)
            )-0.5*vary*vary*math.sin(4*math.radians(GMLS))-1.25*EEO*EEO*math.sin(2*math.radians(GMAS)))
    noon =(720-4*Longitude-ET+timezone*60)/1440
    sunrise = noon-sunrised*4/1440
    sunset = noon+sunrised*4/1440
    duration = 8*sunrised
    return [duration, sunrise, noon, sunset]
print(sunlight(Latitude, Longitude, timesec))

dayhours = sunlight(Latitude, Longitude, timesec)[0] / 6
nighthours = (1440 - sunlight(Latitude, Longitude, timesec)[0]) / 6
print('Day segment lenght',dayhours)
print('Night segment lenght',nighthours)

d1 = sunlight(Latitude, Longitude, timesec)[1] * 24 * 60
earlymorning = []
daylight = []
night = []
for x in range(3):
    m1 = d1 - (nighthours * (3 - x))
    m1 = math.fabs(m1) / 60 / 24 
    earlymorning += [hrmn(m1)]
for x in range(6):
    dz = d1 + (dayhours * x)
    dz = dz / 60 / 24
    daylight += [hrmn(dz)]
dz = d1 + (dayhours * 6)
for x in range(3):
    m1 = dz + (nighthours * x)
    m1 = m1 / 60 / 24 
    night += [hrmn(m1)]

times = earlymorning + daylight + night
print('Rat:',times[0])
print('Ox:',times[1])
print('Tiger:',times[2])
print('Rabit:',times[3])
print('Dragon:',times[4])
print('Snake:',times[5])
print('Horse:',times[6])
print('Sheep:',times[7])
print('Monkey:',times[8])
print('Bird:',times[9])
print('Dog:',times[10])
print('Boar:',times[11])
