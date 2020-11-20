import random

def sujet():
  s = open("lexique_sujets.txt")
  sujet = s.readlines()
  s.close()
  last = 50
  rnd = random.randint(0, last)
  print(sujet[rnd]),
  
def verbe():
  v = open("lexique_verbes.txt")
  verbe = v.readlines()
  v.close()
  last = 999
  rnd = random.randint(0, last)
  print(verbe[rnd]),
 
def complement():
  c = open("lexique_complements.txt")
  complement = c.readlines()
  c.close()
  last = 999
  rnd = random.randint(0, last)
  print(complement[rnd]),

def phrase():
  print(' ')
  sujet()
  verbe()
  complement()
  print('.')

def chapitre():
 for _ in range(1250):
    phrase()

sujet()
chapitre()
