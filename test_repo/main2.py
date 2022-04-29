duplicatedMass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
s=0

def f1(mass):
    for i in range(len(mass)):

        for j in range(i+1, len(mass)):
            s += j
            if mass[i] == mass[j]:
                print(i, j)


f1(duplicatedMass)
print(s)