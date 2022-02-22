

import csv
import itertools
from posixpath import split
from string import ascii_letters
from TestLigne import linevalide

#Importation du fichier csv contenant les données à traiter

with open('Donnees_Projet.xlsx.csv', newline = '') as csvfile:
    lecture = csv.reader(csvfile, delimiter = ',')
    lignes = list(lecture)     

def calculmoyenne(n):
    Bultin = []
    Bultin = {}
    infos = ["Numero", "Nom", "Prenom", "Date", "Classe"]
    MoyMat = {}
    
    for i in range(5):
        inf = infos[i]
        if i == 3:
            lignes[n][i] = lignes[n][i].replace('-', '/').replace('.', '/').replace(',', '/').replace(';', '/').replace(':', '/').replace(' ', '/')
        Bultin[inf] = lignes[n][i]
    matiere = lignes[n][5]
    matiere = matiere.split('#')
    Test = 2
    MoyMat = {}
    SomMat = 0
    for car in matiere:
        car = car.strip(' ')
        car = car.replace(',', '.')
        if car != '':
            carnm = ''
            l = 0
            while car[l] != '['and car[l] != ']' and car[l] != ':':
                carnm = carnm + car[l]
                l = l + 1
            carnm = carnm.upper()
            
            l = l + 1
            if l < len(car):
                somdev = 0
                n = 0
                while l < len(car) and car[l] != ':' and car[l] != ']':
                    dev = ''
                    test1 = 0
                    while car[l] != ':' and car[l] != ';' and car[l] != ']' and l < len(car):
                        dev += car[l]
                        l += 1
                        if car[l] != ".":
                            test = 1
                        else:
                            test1 += 1
                    x = len(car)
                    n += 1
                    if car[l] == ';':
                        l += 1
                    if test != 1:
                        if not dev.isdigit():
                            Test = 0
                            break
                    else:
                        if test1 <= 1:
                            if float(dev) <= 20:
                                somdev += float(dev)
                            else:
                                Test = 0
                                break
                cc = somdev/n
                l = l + 1
                exam = ''
                while (l<=(len(car)-1))and(car[l] != ']'):
                    exam = exam + car[l]
                    l = l + 1
                l += 1
                if exam == '':
                    exam = 0
                if not str(exam).isdigit() or float(exam) > 20:
                    Test = 0
                    break
                else:
                    moy = round((cc + 2*float(exam))/3, 2)
                    MoyMat[carnm] = moy
                    if carnm == "MATH" or carnm == "MATHS":
                        SomMat += 4*moy
                    else:
                        if carnm == "PC" or carnm == "SCIENCE_PHYSIQUE" or carnm == "SVT":
                            SomMat += 3*moy
                        else:
                            SomMat += 2*moy
    MoySem = round(SomMat/16, 2)
    MoyMat["MoySem"] = MoySem
    Bultin.update(MoyMat)
    if Test != 0:
        return Bultin

l = 0
n = 0
MoySem = ""
DonneesValides = []
DonneesInvalides = []
for i in range(221):
    x = linevalide(i)
    if x == 1:
        moy = calculmoyenne(i)
        if moy is not None:
            DonneesValides.append(moy)
        else:
            DonneesInvalides.append(lignes[i])
    else:
        DonneesInvalides.append(lignes[i])

sup = 0
supMax = 20
k = 0
RangEleve = []
while k <= 221:
    x = linevalide(k)
    if DonneesValides[k] is not None:
        sup = 0
        for i in range(113):
            if DonneesValides[i] is not None:
                if sup <= DonneesValides[i]["MoySem"] and DonneesValides[i]["MoySem"] < supMax:
                    sup = DonneesValides[i]["MoySem"]
                    indice = i
        if sup == 0:
            break
        supMax = sup
        k += 1
        RangEleve.append(DonneesValides[indice])
    else:
        k += 1
        l += 1
    if sup == 0:
        break
Choice = 5
while True:
    print()
    print("Veuillez choisir ce que vous voulez afficher :")
    print("   1. Affichage des données vallides.")
    print("   2. Affichage des données invalides.")
    print("   3. Affichage des 5 premier de l'école.")
    print("   Tapez 0 pour quitter.")
    Choice = input("Choix : ")
    print()
    if Choice == "3":
        for i in range(5):
            print(RangEleve[i])
    else:
        if Choice =="2":
            for i in DonneesInvalides:
                print(i)
        else:
            if Choice =="1":
                for i in DonneesValides:
                    print(i)
            else:
                if Choice == '0':
                    break
                else:
                    print("Erreur! Veuillez reessayer.")