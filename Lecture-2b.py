

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', '-Ceres', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_dist = [     0.39,    0.72,     1.0,   1.52,     2.77,       5.2,     9.55,    19.22,     30.11]

k_list = [-999999999999999]
k_list += list(range(0,8))

# Just to see what these are
print(list(range(0,8)))
print(k_list)

for name, dist, k in zip(planet_names, planets_dist, k_list):

    # Titius-Bode law predicted distance
    bode = 0.4 + 0.3*2**k

    percent_diff = (dist - bode)/bode * 100

    print(name, dist, bode, str(round(percent_diff, 2)) + '%')