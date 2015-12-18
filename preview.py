rubix = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
miniface = 0
for x in rubix[0]:
    miniface += 1
    if miniface == 1 or miniface == 4 or miniface == 7:
        print("       "+str(z)+",", end = "")
    elif miniface % 3 == 0:
        print(z)
    else:
        print(str(z)+",", end = "")
print("")
rows = []
for g in range(1, 4):
    for n in range(1, 5):
        for c in rubix[n][(g*3 - 3):(g*3)]:
            rows.append(c)
counter = 0
for sd in rows:
    counter += 1
    if counter % 12 == 0:
        print(sd)
    else:
        if counter % 3 == 0:
            print(sd, end="  ")
        else:
            print(str(sd)+",", end="")
print("")
miniface = 0       
for s in rubix[5]:
    miniface += 1
    if miniface == 1 or miniface == 4 or miniface == 7:
        print("       "+str(s)+",", end = "")
    elif miniface % 3 == 0:
        print(s)
    else:
        print(str(s)+",", end = "")
