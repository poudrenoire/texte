import random
def phrase():
    s = open("lexique_sujets.txt")
    v = open("lexique_verbes.txt")
    c = open("lexique_complements.txt")
    sujet = s.readlines()
    verbe = v.readlines()
    complement = c.readlines()
    print(random.choice(sujet), random.choice(verbe), random.choice(complement), '. ')

def chapitre():
 for _ in range(1250):
    phrase()

chapitre()
