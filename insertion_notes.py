from openpyxl import load_workbook
classeur=load_workbook("exemple.xlsx")
list_notes=classeur["notes"]
matricule=int(input("Entrez le matricule de l'étudiant': "))
sigle=input("Entrez le sigle du cours: ")
note=int(input("Entrez la note de l'étudiant: "))
notes=[matricule,note]
list_notes.append(notes)
classeur.save('exemple.xlsx') 