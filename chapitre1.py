# Ce fichier génère le premier chapitre du livre à partir des lexiques créés pour l'occasion. Y sont définis plusieurs types de phrases.
import random

# Définition des phrases sujet-verbe-complément en "Je"

def phrase_svc_je():
    s = open("lexique_sujets.txt")
    v = open("lexique_verbes.txt")
    c = open("lexique_complements.txt")
    sujet = s.readlines()
    verbe = v.readlines()
    complement = c.readlines()
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    print(sujet_r.capitalize(), verbe_r, complement_r, '. ')
    
 # Définition des phrases Adverbe, sujet verbe intransitif en "Je"

def phrase_asv_je():
    s = open("lexique_sujets.txt")
    v = open("lexique_verbes.txt")
    a = open("lexique_adverbes.txt")
    sujet = s.readlines()
    verbe = v.readlines()
    adverbe = a.readlines()
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    adverbe_r = random.choice(adverbe)
    if adverbe_r is none:
        adverbe_r = random.choice(adverbe)
    else:
        print(sujet_r.capitalize(), verbe_r, adverbe_r, '. ')

def chapitre():
 for _ in range(250):
    print(phrase_svc_je(), phrase_asv_je())

chapitre()
