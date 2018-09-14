import numpy as np


print("Welcome to the Great Translator! \nType exit at any time to leave.")
while True:
    start = input("Enter a phrase:")
    if start == "exit":
        break
    n = start.split()
    n = np.array(n)
    p = []
    for i in range(len(n)):
        k = n[i]
        k = k[0]
        p.append(k)
    l = np.array(p)
    j = l[len(l)-1]
    l = np.delete(l,(len(l)-1))
    l = np.insert(l,0,j)
    final = []
    for i in range(len(n)):
        k = n[i]
        k = k[1:]
        k = list(k)
        k.insert(0,l[i])
        k = "".join(k)
        final.append(k)
    final = " ".join(final)
    print(final)