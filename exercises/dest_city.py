# Problem with solution: https://www.youtube.com/watch?v=qnSF8YaPx78&t=364s

def destCity(paths) -> str:
    cities = []
    for path in paths:
        cities.extend(path)

    for city in set(cities):
        if cities.count(city) == 1 and cities.index(city) % 2:
            return city

paths = [["B","C"],["C","A"],["L","D"],["D","B"]]

print(destCity(paths))