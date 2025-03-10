import sys

def vymen_znak(retezec):
    znak_ke_zmene = " "
    nahradni_znak = "_"
    novy_retezec = retezec.replace(znak_ke_zmene, nahradni_znak)
    return novy_retezec

print(vymen_znak(sys.argv[1]))

