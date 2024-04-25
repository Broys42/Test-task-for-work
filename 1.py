def findClosestPoint(favoritesPlaces, jack):
    minDistance = 999999999
    closest = 0
    for i in favoritesPlaces:
        if abs(i - jack) <= minDistance:
            minDistance = abs(i - jack)
            closest = i
    return closest

s = [str(x) for x in input() if len(str(x)) >= 1 and len(str(x)) <= 100000]

jack, result = 0, 0

favoritesPlaces = []

for index, i in enumerate(s):
    if i == "X":
        favoritesPlaces.append(index+1)

    if i == "O":
        jack = index+1

while favoritesPlaces:
    minDistance = findClosestPoint(favoritesPlaces , jack)
    print(f"Элемент {minDistance} список {favoritesPlaces}")
    favoritesPlaces.remove(minDistance)
    result += abs(jack-minDistance)
    jack = minDistance

print(result)
