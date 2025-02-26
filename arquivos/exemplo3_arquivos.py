import random

times = ["Palmeiras", "São Paulo", "Corinthians", "Portuguesa", "Juventus", "Nacional"]

arq = open('resultados.txt', mode="w")

for f in range(0, len(times)):
    fixo = times[f]
    for i in range(f + 1, len(times)):
        g1 = random.randint(0, 7)
        g2 = random.randint(0, 7)
        arq.write(f"{fixo} {g1} X {g2} {times[i]}\n")

for f in range(len(times) - 1, -1, -1):
    fixo = times[f]
    for i in range(f - 1, - 1, -1):
        g1 = random.randint(0, 7)
        g2 = random.randint(0, 7)
        arq.write(f"{fixo} {g1} X {g2} {times[i]}\n")

arq.close()

