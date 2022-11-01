import time
import threading as t
from fam import *
from otch import *
from ism import *

i1 = t.Thread(target=ism)
f1 = t.Thread(target=familiya)
o1 = t.Thread(target=otchestvo)

i1.start()
f1.start()
o1.start()

son = input("Sonni kiriting: ")

if son == "1":
    print(otchestvo(), "qizi")
    
elif son == "2":
    print(otchestvo(), "o'g'li")
