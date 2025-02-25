arq = open('arq.txt', 'w')
for i in range(1, 10):
    for j in range(1, 5):
        arq.write(f"({i},  {j})\n")

arq.close()



