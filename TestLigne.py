

import csv
from FonctionExo8 import datevalide

with open('Donnees_Projet.xlsx.csv', newline = '') as csvfile:
    lecture = csv.reader(csvfile, delimiter = ',')
    lignes = list(lecture)
    
date = lignes[1][3]
date = date.replace('-', '/').replace('.', '/').replace(',', '/').replace(';', '/').replace(':', '/')
date = date.split("/")
print(date[0])
note = ''
note = lignes[1][5]
note = note.split('#')


def linevalide(n):
    num = lignes[n][0]
    testprenom = 2 
    testclasse =2
    testnum = 2
    testnom = 2
    Testline = 2
    
    if num.isalnum() and num.isupper() and not num.isalpha() and len(num) == 7:
        testnum = 1
    #else:
        #print("Numero non valide")
    nom = lignes[n][1]
    if nom.isalnum():
        if nom[0].isalpha() and len(nom) >= 2:
            testnom = 1
    #else:
        #print("Le nom est invalide")
    prenom = lignes[n][2]
    if prenom.isalnum():
        if prenom[0].isalpha() and len(prenom) >= 3:
            testprenom = 1
    #else:
        #print("Le prenom est invalide")
    classe = lignes[n][4]
    if not classe:
        #print('Le champ classe est vide')
        Test = 0
    else:
        if (classe[0] == '3' or classe[0] == '4' or classe[0] == '5' or classe[0] == '6') and ((classe[len(classe) - 1] == 'B') or (classe[len(classe) - 1] == 'A')):
            testclasse = 1
        #else:
            #print("La classe est invalide")
    date = lignes[n][3]
    if not date:
        #print("La liste est vide")
        Test = 0
    else:
        date = date.replace('-', '/').replace('.', '/').replace(',', '/').replace(';', '/').replace(':', '/')
        testdate = datevalide()
        if testnum == 1 and testnom == 1 and testprenom == 1 and testdate == 1 and testclasse == 1:
            Testline = 1
        else:
            Testline = 0
            
    return Testline
    

