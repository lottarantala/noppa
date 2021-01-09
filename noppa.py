import random as r

def noppa():
    luvut = [1, 2, 3, 4, 5, 6]
    luku = r.choice(luvut)
    print(luku)

if __name__ == "__main__":
    print("Tämä on noppa")
    while True:
        heitto = input("Valitse x heittääksesi nopan: ")
        heitto = heitto.lower()
        if heitto == "x":
            noppa()
        else:
            print("Et valinnut x!")