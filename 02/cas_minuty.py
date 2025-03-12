import sys
def cas_minuty(cas_hodiny, cas_minuty):
    hodiny = int(cas_hodiny)
    minuty = int(cas_minuty)
    cas = minuty + hodiny*60
    return cas

try:
    print(cas_minuty((sys.argv[1]), (sys.argv[2])))
except IndexError:
    exit(f"Usage: {sys.argv[0]} <hodiny> <minuty>")




