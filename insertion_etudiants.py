from openpyxl import load_workbook
classeur=load_workbook("exemple.xlsx")
etudiants=classeur["etudiants"]
matricule=int(input("Entrez votre matricule: "))
nom=input("Entrez votre nom: ")
postnom=input("Entrez votre postnom: ")
prenom=input("Entrez votre prenom: ")
dateNaissance=input("Entrez votre date de naissance: ")
lieuNaissance=input("Entrez votre lieu de naissance: ")
identite=[matricule,nom,postnom,prenom,dateNaissance,lieuNaissance]
etudiants.append(identite)
classeur.save('exemple.xlsx')