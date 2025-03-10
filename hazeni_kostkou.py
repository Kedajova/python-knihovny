import sys
import random

def hod_kostkou(pocet_sten, pocet_hodu):
    try:
        pocet_sten = int(pocet_sten)
        pocet_hodu = int(pocet_hodu)
        hody = [random.randint(0,pocet_sten) for hod in range(pocet_hodu)]
        return hody
    except ValueError:
        exit(f"Usage: {sys.argv[0]} <pocet stran> <pocet hodu>")

print(hod_kostkou((sys.argv[1]), (sys.argv[2])))