# Ce fichier génère le premier chapitre du livre à partir des lexiques créés pour l'occasion. Y sont définis plusieurs types de phrases.
# On commence par importer le module random

import random

# Définition des phrases transitives : sujet-verbe-complément en "Je"

def phrase_svc_je():
    # Ouverture des fichiers pour chaque type de mots dans une variable
    v = open("lex/lexique_v_trans_je.txt")
    c = open("lex/lexique_objets_det.txt")
    # Lecture des fichiers dans une variable
    verbe = v.read().splitlines()
    complement = c.read().splitlines()
    # Sélection d'une ligne aléatoire des fichiers
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    voyelles = ["a", "e", "i", "o", "u", "y", "é"]
    if verbe_r[0] in voyelles:
        sujet_r = "j\'"
    else:
        sujet_r = "je" 
    # Impression des lignes sélectionnées, dans l'ordre spécifé, avec ajout de majuscule.
    print(sujet_r.capitalize(), verbe_r, complement_r, ".", end =" ")

# Définition des phrases avec complément temporel passé, "cela" et verbe intransitif à l'imparfait

def phrase_cela_imp_intrans():
    c = open("lex/lexique_comp_t_p.txt")
    v = open("lex/lexique_v_intrans_iel_imp.txt")
    complement = c.read().splitlines()
    verbe = v.read().splitlines()
    complement_r = random.choice(complement)
    verbe_r = random.choice(verbe)
    print(complement_r.capitalize(), ", ", "cela", verbe_r, ".", end=" ")
    
 # Définition des phrases instransitives en "Je" avec adverbe.

def phrase_asv_je():
    v = open("lex/lexique_v_intrans_je.txt")
    a = open("lex/lexique_adverbes.txt")
    verbe = v.read().splitlines()
    adverbe = a.read().splitlines()
    verbe_r = random.choice(verbe)
    adverbe_r = random.choice(adverbe)
    voyelles = ["a", "e", "i", "o", "u", "y", "é"]
    if verbe_r[0] in voyelles:
        sujet_r = "j\'"
    else:
        sujet_r = "je"   
    print(sujet_r.capitalize(), verbe_r, adverbe_r, ".", end =" ")
        
# Définition des phrases ditransitives en "Je"

def phrase_svcc_je():
    v = open("lex/lexique_v_ditrans_je.txt")
    c = open("lex/lexique_objets_det.txt")
    c2 = open ("lex/lexique_objets_a.txt")
    verbe = v.read().splitlines()
    complement = c.read().splitlines()
    complement2 = c2.read().splitlines()
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)
    complement2_r = random.choice(complement2)
    voyelles = ["a", "e", "i", "o", "u", "y", "é"]
    if verbe_r[0] in voyelles:
        sujet_r = "j\'"
    else:
        sujet_r = "je"   
    print(sujet_r.capitalize(), verbe_r, complement_r, complement2_r, ".", end =" ")

# Définition des phrases transitives avec sujet concept singulier masculin
    
def phrase_svc_conc_m_s():
    s = open("lex/lexique_concepts_det_m_s.txt")
    v = open("lex/lexique_v_trans_iel.txt")
    c = open("lex/lexique_objets_det.txt")
    sujet = s.read().splitlines()
    verbe = v.read().splitlines()
    complement = c.read().splitlines()
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)   
    print(sujet_r.capitalize(), verbe_r, complement_r, ".", end =" ")
    
# Définition des phrases transitives avec sujet objet concept singulier féminin
    
def phrase_svc_conc_f_s():
    s = open("lex/lexique_objets_det.txt")
    v = open("lex/lexique_v_trans_iel.txt")
    c = open("lex/lexique_concepts_det_m_s.txt")
    sujet = s.read().splitlines()
    verbe = v.read().splitlines()
    complement = c.read().splitlines()
    sujet_r = random.choice(sujet)
    verbe_r = random.choice(verbe)
    complement_r = random.choice(complement)   
    print(sujet_r.capitalize(), verbe_r, complement_r, ".", end =" ")

    
for _ in range (20):
  p1 = phrase_svc_je()
  p2 = phrase_asv_je()
  p3 = phrase_svcc_je()
  p4 = phrase_svc_conc_m_s()
  p5 = phrase_svc_conc_f_s()
  p6 = phrase_cela_imp_intrans()
  list_p = (p1, p2, p3, p4, p5, p6)
  random.choices(list_p)
