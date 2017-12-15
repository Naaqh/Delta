from math import *
import sys

#--- On demande les valeurs à l'utilisateur ---#
A = int(input("Que vaut A ?"))
B = int(input("Que vaut B ?"))
C = int(input("Que vaut C ?"))


#--- Calcul de Delta et on l'affiche ---#
delta = (B*B)-4*(A)*(C)
print("Delta vaut",delta,".")

if A == 0 :
    print("Division par zéro impossible, veuillez recommencer.")
    sys.exit()

#--- On définit les 3 conditions ---#
if delta > 0:
    x1 = (-B-sqrt(delta))/(2*A)
    x2 = (-B+sqrt(delta))/(2*A)
    print("Premiere solution vaut",x1,"deuxieme solution vaut",x2,".")

if delta == 0:
    x0 = -B/(2*A)
    print("L'unique solution vaut",x0,".")

if delta < 0:
    print("Delta < 0, pas de solution")




