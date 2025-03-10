import sys

def had_na_velbdlouda(retezec):
    hadi_znak = "_"
    rozdeleny_retezec = retezec.split(hadi_znak)
    camel_case = rozdeleny_retezec[0] + ''.join(slovo.capitalize() for slovo in rozdeleny_retezec[1:])
    return camel_case

print(had_na_velbdlouda(sys.argv[1]))