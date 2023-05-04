# Patient Data Processing Module
This module is designed to process patient data for a medical clinic. It includes functions for importing patient data from a file, calculating the body mass index (BMI) of patients, and generating reports.

## Part 1: Importing Patient Data
The import_lignes function takes a file name as input and returns a list of lines from the file. The cree_patient function takes a line of patient data as input and returns a dictionary containing the patient's name, weight, and height. The liste_patients_from_nom_fichier function takes a file name as input, imports the patient data from the file using the import_lignes function, and creates a list of patient dictionaries using the cree_patient function.

## Part 2: Calculating BMI and Generating Reports
The imc function takes a patient dictionary as input and returns the patient's BMI. The imc_moyen function takes a list of patient dictionaries as input and returns the average BMI of all the patients. The liste_noms_patients_en_corpulence_normale function takes a list of patient dictionaries as input and returns a list of the names of all patients with a BMI in the normal range.

The produire_chaine function takes a patient dictionary as input and returns a string containing the patient's name and BMI. The ecrire_imc function takes a list of patient dictionaries and a file name as input and writes a report to the file containing each patient's name and BMI, the average BMI of all patients, and the names of all patients with a BMI in the normal range.

The traitement_complet_donnees function takes a file name for patient data and a file name for the report as input, imports the patient data using the liste_patients_from_nom_fichier function, and writes a report using the ecrire_imc function.


