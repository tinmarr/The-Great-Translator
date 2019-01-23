import numpy as np
from sys import exit

vowels = np.array(["a","e","i","o","u"])

print("Welcome to the Great Translator!\nType exit at any time to leave.")
while True:
    start = input("Enter a phrase:")
    if start == "exit":
        exit()
    n = start.split()
    n = np.array(n)
    p = []
    v = []
    for i in range(len(n)):
        k = n[i]
        for j in range(len(k)):
          if k[j] in vowels:
            v.append(j)
        k = k[:v[i]]
        p.append(k)
    l = np.array(p)
    m = l[len(l)-1]
    l = np.delete(l,(len(l)-1))
    l = np.insert(l,0,m)
    final = []
    for i in range(len(n)):
        k = n[i]
        k = k[v[i]:]
        k = list(k)
        k.insert(0,l[i])
        k = "".join(k)
        final.append(k)
    final = " ".join(final)
    print(final)