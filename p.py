import math


def euclideanDistance(p1, p2):
    distance_squared = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    distance = math.sqrt(distance_squared)
    return distance


points = list()
distances = list()

while True:
    x = int(input("X'i girin: "))
    y = int(input("Y'i girin: "))
    points.append((x, y))

    check = input("Bir nokta daha eklemek ister misiniz?")

    if check.lower() == "h":
        break

while len(points) > 1:
    i = 1
    while True:
        distances.append(euclideanDistance(points[0], points[i]))
        i = i + 1

        if i == len(points):
            break
    points.pop(0)

minimum = distances[0]

for i in distances:
    if minimum > i:
        minimum = i

print(f"Girdiginiz noktalar arasindaki en kisa mesafe sudur: {minimum}")
