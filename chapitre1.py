# Ce fichier génère le premier chapitre du livre à partir des lexiques créés pour l'occasion. Y sont définis plusieurs types de phrases.
# On commence par importer le module random

import random

# Définition des phrases transitives : sujet-verbe-complément en "Je"

def phrase_svc_je():
    # Ouverture des fichiers pour chaque type de mots dans une variable
    v = open("lexique_v_trans.txt")
    c = open("lexique_complements.txt")
    # Lecture des fichiers dans une variable
    verbe = v.read().splitlines()
    complement = c.read().splitlines()
    # Sélection d'une ligne aléatoire des fichiers
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    voyelles = ["a", "e", "i", "o", "u", "y"]
    if verbe_r[0] in voyelles:
        sujet_r = "j\'"
    else:
        sujet_r = "je" 
    # Impression des lignes sélectionnées, dans l'ordre spécifé, avec ajout de majuscule.
    return(sujet_r.capitalize(), verbe_r, complement_r, ". ")
    
 # Définition des phrases instransitives en "Je" avec adverbe.

def phrase_asv_je():
    v = open("lexique_v_intrans.txt")
    a = open("lexique_adverbes.txt")
    verbe = v.read().splitlines()
    adverbe = a.read().splitlines()
    verbe_r = random.choice(verbe)
    adverbe_r = random.choice(adverbe)
    voyelles = ["a", "e", "i", "o", "u", "y"]
    if verbe_r[0] in voyelles:
        sujet_r = "j\'"
    else:
        sujet_r = "je"   
    return(sujet_r.capitalize(), verbe_r, adverbe_r, '. ')
        
# Définition des phrases ditransitives en "Je"

def phrase_svcc_je():
    v = open("lexique_v_ditrans.txt")
    c = open("lexique_complements.txt")
    c2 = open ("lexique_complements_a.txt")
    verbe = v.read().splitlines()
    complement = c.read().splitlines()
    complement2 = c2.read().splitlines()
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    complement2_r = random.choice(complement2)
    voyelles = ["a", "e", "i", "o", "u", "y"]
    if verbe_r[0] in voyelles:
        sujet_r = "j\'"
    else:
        sujet_r = "je"   
    return(sujet_r.capitalize(), verbe_r, complement_r, complement2_r, '. ')
    
    
def chapitre():
   for _ in range(250):
     print(phrase_svc_je(), phrase_asv_je(), phrase_svcc_je())

chapitre()
