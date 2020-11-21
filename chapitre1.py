# Ce fichier génère le premier chapitre du livre à partir des lexiques créés pour l'occasion. Y sont définis plusieurs types de phrases.
# On commence par importer le module random

import random

# Définition des phrases transitives : sujet-verbe-complément en "Je"

def phrase_svc_je():
    # Ouverture des fichiers pour chaque type de mots dans une variable
    s = open("lexique_sujets.txt")
    v = open("lexique_v_trans.txt")
    c = open("lexique_complements.txt")
    # Lecture des fichiers dans une variable
    sujet = s.readlines()
    verbe = v.readlines()
    complement = c.readlines()
    # Sélection d'une ligne aléatoire des fichiers
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    # Impression des lignes sélectionnées, dans l'ordre spécifé, sans retour à la ligne, avec ajout de majuscule.
    print(str(sujet_r.capitalize().splitlines()), str(verbe_r.splitlines()), str(complement_r.splitlines()))
    
 # Définition des phrases instransitives en "Je" avec adverbe en entrée.

def phrase_asv_je():
    s = open("lexique_sujets.txt")
    v = open("lexique_v_intrans.txt")
    a = open("lexique_adverbes.txt")
    sujet = s.readlines()
    verbe = v.readlines()
    adverbe = a.readlines()
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    adverbe_r = random.choice(adverbe)
  # Ne pas mettre d'adverbe si la valeur est None
    if adverbe_r is None:
        print(sujet_r.capitalize(), verbe_r, '. ')
    else:
        print(sujet_r.capitalize(), verbe_r, adverbe_r, '. ')
        
# Définition des phrases ditransitivrs en "Je"

def phrase_svcc_je():
    s = open("lexique_sujets.txt")
    v = open("lexique_v_trans.txt")
    c = open("lexique_complements.txt")
    sujet = s.readlines()
    verbe = v.readlines()
    complement = c.readlines()
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    complement2_r = random.choice(complement)
    print(sujet_r.capitalize(), verbe_r, complement_r, ' à ', complement2_r, '. ')

def chapitre():
 for _ in range(250):
    phrase_svc_je(), phrase_asv_je(), phrase_svcc_je()

chapitre()
