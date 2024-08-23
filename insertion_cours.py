from openpyxl import load_workbook
classeur=load_workbook("exemple.xlsx")
list_cours=classeur["cours"]
sigle=input("Entrez le sigle du cours: ")
intitule=input("Entrez l'intitulé du cours: ")
cours=[sigle,intitule]
list_cours.append(cours)
classeur.save('exemple.xlsx')